import psycopg2
import time

def init_db():
    try:
        conn = psycopg2.connect(
            host="db",
            database="db",
            user="admin",
            password="secret",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS system_logs (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                log_text TEXT NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("База даних успішно ініціалізована.")
    except Exception as e:
        print(f"Помилка ініціалізації: {e}")

def insert_custom_log(log_message: str):
    try:
        conn = psycopg2.connect(host="db", database="db", user="admin", password="secret", port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO system_logs (log_text) VALUES (%s);", (log_message,))
        conn.commit()
        print(f"Записано лог: '{log_message}'")
    except Exception as e:
        print(f"Помилка запису: {e}")
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    print("Очікування запуску БД (5 секунд)...")
    time.sleep(5) # Даємо базі даних час на запуск
    
    init_db()
    
    counter = 1
    while True:
        insert_custom_log(f"Автоматичний запис №{counter} з контейнера додатку")
        counter += 1
        time.sleep(10)