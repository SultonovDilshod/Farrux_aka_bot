import sqlite3


class DataBase:
    def __init__(self, path_to_db="datas.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name varchar(255) NOT NULL,
            student_group varchar(255) NOT NULL,
            student_birth varchar(255) NOT NULL
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, student_name: str, student_group: int, student_birth: str):
        # def add_user(self, id: int, full_name: str, username: str = None, telegram_id: int, email_db: str, tel_num: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(student_id, student_name, student_group, student_birth) VALUES(NULL, ?, ?, ?)
        """
        self.execute(sql, parameters=(student_name, student_group, student_birth), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self, student_id):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def delete_user(self, student_id):
        self.execute(f"DELETE FROM Users WHERE student_id = {student_id}", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
