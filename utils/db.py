import os
import psycopg2


def initialize_pool(minconn=1, maxconn=20):
    global connection_pool
    try:
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn,
            maxconn,
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"]
        )
    except Exception as e:
        print("Error initializing connection pool:", e)


def get_connection():
    try:
        return connection_pool.getconn()
    except Exception as e:
        print("Error getting connection from pool:", e)
        return None
    

def return_connection(conn):
    if conn:
        connection_pool.putconn(conn)
    

def execute_query(query, parameters):
    conn = get_connection()
    if not conn:
        return None
    
    try:
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
    conn = get_connection()
    if not conn:
        return None
    
    try:
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
    conn = get_connection()
    if not conn:
        return None
    
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, parameters if parameters else ())
                return cur.fetchone()
    except Exception as e:
        print("Error fetching one result:", e)
        return None
    finally:
        return_connection(conn)