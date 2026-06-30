import sqlite3


class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            priority TEXT,
            due_date TEXT,
            status TEXT
        )
        """)

        self.conn.commit()

    def add_task(self, task):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO tasks
        (title, description, priority,
         due_date, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            task.title,
            task.description,
            task.priority,
            task.due_date,
            task.status
        ))

        self.conn.commit()

    def get_tasks(self):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks"
        )

        return cursor.fetchall()

    def update_task(self, task_id, field, value):

        cursor = self.conn.cursor()

        query = f"UPDATE tasks SET {field} = ? WHERE id = ?"

        cursor.execute(
            query,
            (value, task_id)
        )

        self.conn.commit()

    def delete_task(self, task_id):

        cursor = self.conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        self.conn.commit()

    def mark_complete(self, task_id):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET status = 'completed'
            WHERE id = ?
            """,
            (task_id,)
        )

        self.conn.commit()

    def search_tasks(self, keyword):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE title LIKE ?
            OR description LIKE ?
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        return cursor.fetchall()

    def filter_by_status(self, status):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE status = ?
            """,
            (status,)
        )

        return cursor.fetchall()

    def filter_by_priority(self, priority):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tasks
            WHERE priority = ?
            """,
            (priority,)
        )

        return cursor.fetchall()