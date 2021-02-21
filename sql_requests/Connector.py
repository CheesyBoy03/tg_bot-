import mysql.connector


class Connector:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host='localhost',
            user='root',
            password='just_code03',
            port='3306',
            database='for_admin',
        )
        self.cursor = self.connector.cursor(buffered=True)
