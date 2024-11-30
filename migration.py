import os
from app.utils.db import initialize_pool, get_connection


initialize_pool()


def create_migrations_table():
    query = """
    CREATE TABLE IF NOT EXISTS migrations (
        id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        filename TEXT NOT NULL UNIQUE,
        applied_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
    finally:
        conn.close()


def get_applied_migrations():
    query = "SELECT filename FROM migrations ORDER BY id;"
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return {row[0] for row in cur.fetchall()}
    finally:
        conn.close()
        

def apply_migration(filename, query):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                cur.execute(
                    "INSERT INTO migrations (filename) VALUES (%s)", (filename,)
                )
    except Exception as e:
        print(f"Error applying migration: {filename}. Rolling back...")
        conn.rollback()
        raise e
    finally:
        conn.close()


def rollback_migration(name, query):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            cur.execute("DELETE FROM migrations WHERE migration_name = %s;", (name,))
        conn.commit()


def run_migrations():
    migration_folder = os.path.join(os.path.dirname(__file__), "migrations")
    migration_files = sorted(f for f in os.listdir(migration_folder) if f.endswith(".sql"))

    applied_migrations = get_applied_migrations()

    for filename in migration_files:
        if filename not in applied_migrations:
            filepath = os.path.join(migration_folder, filename)
            with open(filepath, "r") as f:
                sql = f.read()
            try:
                print(f"Applying migration: {filename}")
                apply_migration(filename, sql)
                print(f"Successfully applied migration: {filename}")
            except Exception as e:
                print(f"Migration failed: {filename}. Error: {e}")
                break


def extract_rollback_sql(lines):
    rollback_sql = []
    in_rollback = False
    for line in lines:
        if line.strip() == "-- ROLLBACK START":
            in_rollback = True
            continue
        if line.strip() == "-- ROLLBACK END":
            in_rollback = False
            continue
        if in_rollback:
            rollback_sql.append(line)
    return "".join(rollback_sql) if rollback_sql else None


def rollback(filename):
    migration_folder = os.path.join(os.path.dirname(__file__), "migrations")
    filepath = os.path.join(migration_folder, filename)

    with open(filepath, "r") as f:
        lines = f.readlines()

    rollback_sql = extract_rollback_sql(lines)

    if rollback_sql:
        try:
            print(f"Rolling back migration: {filename}")
            rollback_migration(filename, rollback_sql)
            print(f"Successfully rolled back: {filename}")
        except Exception as e:
            print(f"Error during rollback of {filename}: {e}")
    else:
        print(f"No rollback SQL provided for {filename}. Manual intervention may be required.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run or rollback migrations.")
    parser.add_argument(
        "--run", 
        action="store_true", 
        help="Run all pending migrations."
    )
    parser.add_argument(
        "--rollback",
        metavar="FILENAME",
        help="Rollback a specific migration by filename."
    )
    args = parser.parse_args()

    create_migrations_table()

    if args.run:
        print("Running migrations...")
        run_migrations()
    elif args.rollback:
        print(f"Rolling back migration: {args.rollback}")
        rollback(args.rollback)
    else:
        print("No valid arguments provided. Use --help for options.")