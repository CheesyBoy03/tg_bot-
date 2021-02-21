from sql_requests.Connector import Connector


class HelloMessage(Connector):
    def get_hello_message(self):
        self.cursor.execute("SELECT * FROM hello_msg")
        res = self.cursor.fetchall()
        if res:
            return res[0][0]
        else:
            return False

    def add_hello_message(self, msg_text):
        request = "INSERT INTO hello_msg VALUE (%s)"
        self.cursor.execute(request, (msg_text,))
        self.connector.commit()

    def delete_hello_message(self):
        self.cursor.execute("UPDATE hello_msg SET hello_msg = '' WHERE hello_msg != '';")
        self.cursor.execute("DELETE FROM hello_msg WHERE hello_msg='';")
        self.connector.commit()
