import sqlite3
from os import PathLike
from pathlib import Path


# Helper function to establish connection and handle errors
def connect_to_db(db_name: str | Path | PathLike) -> sqlite3.Connection:
    if not db_name or (isinstance(db_name, (str, Path)) and not str(db_name).strip()):
        raise ValueError("Database name cannot be empty.")
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise


# Generic function to execute a query with optional parameters
def execute_query(conn: sqlite3.Connection, query: str, params: tuple | None = ()) -> None:
    if len(query) == 0:
        raise ValueError("Query cannot be empty.")
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error executing query: {query} with params {params}\n{e}")
        raise


# Generic function to execute a script (multiple queries)
def execute_script(conn: sqlite3.Connection, script: str) -> None:
    try:
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error executing script: {script}\n{e}")
        raise


# Generic function to fetch data
def fetch_data(conn: sqlite3.Connection, query: str, params: tuple | None = ()) -> list[tuple]:
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching data: {query} with params {params}\n{e}")
        raise
