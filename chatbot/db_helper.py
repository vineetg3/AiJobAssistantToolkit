import sqlite3
from typing import List, Dict, Any
from pathlib import Path

class SQLiteDBReader:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._validate_db_path()
        
    def _validate_db_path(self) -> None:
        if not Path(self.db_path).exists():
            raise FileNotFoundError(f"Database file not found: {self.db_path}")
            
    def _get_connection(self) -> sqlite3.Connection:
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            raise Exception(f"Error connecting to database: {str(e)}")
            
    def get_all_tables(self) -> List[str]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Query to get all table names
                query = """
                    SELECT name FROM sqlite_master 
                    WHERE type='table' 
                    AND name NOT LIKE 'sqlite_%';
                """
                cursor.execute(query)
                return [table[0] for table in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error getting tables: {str(e)}")
            
    def get_table_columns(self, table_name: str) -> List[str]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Get column information
                cursor.execute(f"PRAGMA table_info({table_name});")
                return [column[1] for column in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error getting columns for table {table_name}: {str(e)}")
            
    def get_table_data(self, table_name: str) -> List[Dict[str, Any]]:
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Get columns first
                columns = self.get_table_columns(table_name)
                
                # Get all data
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                
                # Convert to list of dictionaries
                return [
                    dict(zip(columns, row))
                    for row in rows
                ]
        except sqlite3.Error as e:
            raise Exception(f"Error getting data from table {table_name}: {str(e)}")
            
    def get_all_tables_data(self) -> Dict[str, List[Dict[str, Any]]]:
        try:
            tables = self.get_all_tables()
            return {
                table: self.get_table_data(table)
                for table in tables
            }
        except Exception as e:
            raise Exception(f"Error getting all tables data: {str(e)}")


# def get_database_data(db_path: str) -> Dict[str, List[Dict[str, Any]]]:
#     """Helper function to get all data from a SQLite database"""
#     reader = SQLiteDBReader(db_path)
#     return reader.get_all_tables_data()
