import sqlite3
from pathlib import Path
from typing import Generator

import pytest

from corekit import sqlite_utils


@pytest.fixture
def temp_db_path(tmp_path: Path, request) -> Generator[Path, None, None]:
    """Fixture to create a temporary database path."""
    db_path = tmp_path / f"test_{request.node.name}.db"
    yield db_path

    # Cleanup after tests
    if db_path.exists():
        db_path.unlink()


class TestConnectToDb:
    def test_successful_connection(self, temp_db_path):
        """Test successful database connection."""
        conn = sqlite_utils.connect_to_db(temp_db_path)
        try:
            assert isinstance(conn, sqlite3.Connection)
            assert conn.total_changes == 0  # Fresh connection

            # Verify we can execute a simple query
            cursor = conn.cursor()
            cursor.execute("SELECT sqlite_version()")
            result = cursor.fetchone()
            assert result is not None
        finally:
            conn.close()

    def test_invalid_path(self):
        """Test connection with invalid path."""
        # It's invalid because the dir doesn't even exists
        invalid_path = "/nonexistent/path/to/db.sqlite"
        with pytest.raises(sqlite3.Error):
            sqlite_utils.connect_to_db(invalid_path)

    def test_empty_path(self):
        """Test connection with empty path."""
        with pytest.raises(ValueError):
            sqlite_utils.connect_to_db("")

    def test_connection_creates_new_db(self, temp_db_path):
        """Test that connection creates new database if it doesn't exist."""
        assert not temp_db_path.exists()
        conn = sqlite_utils.connect_to_db(temp_db_path)
        try:
            assert temp_db_path.exists()
            assert temp_db_path.is_file()
        finally:
            conn.close()

    def test_concurrent_connections(self, temp_db_path):
        """Test multiple concurrent connections to the same database."""
        conn1 = sqlite_utils.connect_to_db(temp_db_path)
        conn2 = sqlite_utils.connect_to_db(temp_db_path)
        try:
            assert isinstance(conn1, sqlite3.Connection)
            assert isinstance(conn2, sqlite3.Connection)
            assert conn1 != conn2  # Different connection objects
        finally:
            conn1.close()
            conn2.close()

    def test_connection_with_special_characters(self, tmp_path):
        """Test connection with special characters in path."""
        db_path = tmp_path / "test!@#$%.db"
        conn = sqlite_utils.connect_to_db(db_path)
        try:
            assert isinstance(conn, sqlite3.Connection)
        finally:
            conn.close()


class TestExecuteQuery:
    def test_empty_query(self, temp_db_path):
        """Test empty query"""
        conn = sqlite_utils.connect_to_db(temp_db_path)
        try:
            with pytest.raises(ValueError):
                sqlite_utils.execute_query(conn, "")
        finally:
            conn.close()

    def test_execute_valid_query(self, temp_db_path):
        """Test executing a valid query."""
        conn = sqlite_utils.connect_to_db(temp_db_path)
        try:
            create_table_query = "CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)"
            sqlite_utils.execute_query(conn, create_table_query)

            insert_query = "INSERT INTO test (name) VALUES (?)"
            sqlite_utils.execute_query(conn, insert_query, ("test_name",))

            cursor = conn.cursor()
            cursor.execute("SELECT name FROM test WHERE id = 1")
            result = cursor.fetchone()
            assert result == ("test_name",)
        finally:
            conn.close()

    def test_invalid_sql_query(self, temp_db_path):
        """Test executing an invalid SQL query raises sqlite3.Error."""
        conn = sqlite_utils.connect_to_db(temp_db_path)
        try:
            with pytest.raises(sqlite3.Error):
                sqlite_utils.execute_query(conn, "INVALID SQL QUERY")
        finally:
            conn.close()
