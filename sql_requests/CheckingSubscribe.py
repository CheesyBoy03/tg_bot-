from sql_requests.Connector import Connector


class Checking(Connector):
    def on_check(self) -> None:
        self.cursor.execute("INSERT INTO checking VALUE (1)")
        self.connector.commit()

    def off_check(self) -> None:
        self.cursor.execute("INSERT INTO checking VALUE (0)")
        self.connector.commit()

    def delete_row(self) -> None:
        self.cursor.execute("DELETE FROM checking WHERE verification_of_subscription = 0 OR verification_of_subscription = 1;")
        self.connector.commit()

    def get_status(self) -> bool:
        self.cursor.execute("SELECT * FROM checking")
        return bool(self.cursor.fetchall()[0][0])

    def get_channel(self) -> str:
        self.cursor.execute("SELECT * FROM channels")
        return self.cursor.fetchall()[0][0]

    def change_channel(self, channel_id: str) -> None:
        self.cursor.execute("DELETE FROM channels WHERE channel != ''")
        self.connector.commit()
        self.cursor.execute("INSERT INTO channels VALUE ('@%s')" % channel_id)
        self.connector.commit()

    def get_all_services(self) -> list:
        self.cursor.execute("SELECT (name_for_btn, price) FROM services")
        return [self.cursor.fetchall()]
