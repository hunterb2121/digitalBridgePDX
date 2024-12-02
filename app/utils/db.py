import os
import psycopg2.pool


connection_pool = None


def initialize_pool(minconn=1, maxconn=20):
    print("Running initialize_pool() from app/utils/db.py")
    global connection_pool
    try:
        print("Attempting to get connection")
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn,
            maxconn,
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT")
        )
        print("Got connection")
    except Exception as e:
        print("Error initializing connection pool:", e)


def get_connection():
    print("Running get_connection() from app/utils/db.py")
    try:
        print("Getting connection")
        return connection_pool.getconn()
    except Exception as e:
        print("Error getting connection from pool:", e)
        return None
    

def return_connection(conn):
    print("Running return_connection(conn) from app/utils/db.py")
    if conn:
        print("Returning connection")
        connection_pool.putconn(conn)
    

def execute_query(query, parameters):
    print(f"Running execute_query({query}, {parameters}) from app/utils/db.py")
    conn = get_connection()
    if not conn:
        print("No connection from get_connection()")
        return None
    
    try:
        print("Got connection")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, parameters if parameters else ())
                conn.commit()
                return True
    except Exception as e:
        conn.rollback()
        print("Error executing query:", e)
        return None
    finally:
        return_connection(conn)


def get_all_results(query, parameters):
    print(f"Running get_all_results({query}, {parameters}) from app/utils/db.py")
    conn = get_connection()
    if not conn:
        print("No connection from get_connection()")
        return None
    
    try:
        print("Got connection")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, parameters if parameters else ())
                return cur.fetchall()
    except Exception as e:
        print("Error fetching all results:", e)
        return None
    finally:
        return_connection(conn)


def get_one_result(query, parameters):
    print(f"Running get_one_result({query}, {parameters}) from app/utils/db.py")
    conn = get_connection()
    if not conn:
        print("No connection from get_connection()")
        return None
    
    try:
        print("Got connection")
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, parameters if parameters else ())
                return cur.fetchone()
    except Exception as e:
        print("Error fetching one result:", e)
        return None
    finally:
        return_connection(conn)
