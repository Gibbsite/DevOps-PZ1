import psycopg2

def insert_custom_log(log_message: str):
    """
    Connects to the database and inserts a custom log string.
    """
    try:
        # Establish the database connection
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="db",
            user="admin",
            password="secret",
            port="5433"
        )
        cur = conn.cursor()

        # Create the logs table if it doesn't already exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS system_logs (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                log_text TEXT NOT NULL
            );
        """)

        # Insert the custom log safely using parameterized queries
        insert_query = "INSERT INTO system_logs (log_text) VALUES (%s);"
        cur.execute(insert_query, (log_message,))
        
        # Commit the transaction
        conn.commit()
        print(f"Successfully inserted log: '{log_message}'")

    except psycopg2.Error as e:
        print(f"Database error occurred: {e}")
        
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

def read_logs():
    """
    Connects to the database and reads all logs from the system_logs table.
    """
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="db",
            user="admin",
            password="secret",
            port="5433"
        )
        cur = conn.cursor()

        cur.execute("SELECT id, created_at, log_text FROM system_logs;")
        logs = cur.fetchall()
        
        print("System Logs:")
        for log in logs:
            print(f"ID: {log[0]}, Created At: {log[1]}, Log Text: {log[2]}")

    except psycopg2.Error as e:
        print(f"Database error occurred: {e}")
        
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# --- Example Usage ---
if __name__ == "__main__":
    insert_custom_log("Hello, World!")
    insert_custom_log("Goodbye, World!")
    read_logs()