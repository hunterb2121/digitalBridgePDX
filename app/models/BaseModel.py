from ..utils.db import execute_query, get_all_results, get_one_result


class BaseModel:
    """
    BaseModel class provides common methods for interacting with the database.
    Each model will inherit from this and use the common methods for CRUD operations.
    """

    @classmethod
    def execute_query(cls, query, parameters=None):
        return execute_query(query, parameters)
    
    @classmethod
    def get_all(cls, query, parameters=None):
        return get_all_results(query, parameters)
    
    @classmethod
    def get_one(cls, query, parameters=None):
        return get_one_result(query, parameters)
    
    @classmethod
    def get_all_records(cls):
        result = cls.get_all(f"SELECT * FROM {cls.table}")
        return result if result else []
    
    @classmethod
    def insert(cls, columns, values):
        """
        Insert a new record into a table.
        table: str - the table name
        columns: list - columns for the insert
        values: tuple - values for the columns
        """

        placeholders = ', '.join(['%s'] * len(values))
        columns_str = ', '.join(columns)
        query = f'INSERT INTO {cls.table} ({columns_str}) VALUES ({placeholders})'
        cls.execute_query(query, values)

    @classmethod
    def insert_return_id(cls, columns, values):
        """
        Insert a new record into a table and return the id.
        table: str - the table name
        columns: list - columns for the insert
        values: tuple - values for the columns
        """

        placeholders = ', '.join(['%s'] * len(values))
        columns_str = ', '.join(columns)
        query = f'INSERT INTO {cls.table} ({columns_str}) VALUES ({placeholders}) RETURNING id'
        return cls.get_one(query, values)

    @classmethod
    def update(cls, columns, values, condition):
        """
        Update an existing record in a table.
        table: str - the table name
        columns: list - columns to update
        values: tuple - new values for the columns
        condition: str - the WHERE condition for the update
        """

        set_clause = ', '.join([f'{col} = %s' for col in columns])
        query = f'UPDATE {cls.table} SET {set_clause} WHERE {condition}'
        cls.execute_query(query, values)

    @classmethod
    def delete (cls, condition, values=None):
        """
        Delete a record from a table.
        table: str - the table name
        condition: str - the WHERE condition for the delete
        values: tuple - values for the condition
        """

        query = f'DELETE FROM {cls.table} WHERE {condition}'
        cls.execute_query(query, values)