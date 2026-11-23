import sqlite3

DB_NAME = "applications.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                city TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT NOT NULL,
                date_applied TEXT NOT NULL,
                notes TEXT
            )
        """)


def add_application(company, city, role, status, date_applied, notes):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO applications (company, city, role, status, date_applied, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (company, city, role, status, date_applied, notes))


def get_all_applications():
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM applications ORDER BY date_applied DESC")
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_status_counts():
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT status, COUNT(*) as count 
            FROM applications 
            GROUP BY status
        """)
        return dict(cursor.fetchall())


def update_status(app_id, new_status):
    with get_connection() as conn:
        conn.execute("UPDATE applications SET status = ? WHERE id = ?", (new_status, app_id))


def delete_application(app_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
