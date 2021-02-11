import mysql.connector

import mysql.connector


class Connector:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host='localhost',
            user='root',
            password='just_code',
            port='3308'
        )
        self.cursor = self.connector.cursor()

    def get_hello_message(self):
        self.cursor.execute("SELECT message FROM admin_message")
