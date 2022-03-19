import mysql.connector


class DB:
    def __init__(self) -> None:
        self.mydb = self.connect()

    def connect(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="isha@1",
                database="automation"
            )
            print("Connected :)")
            return mydb
        except Exception:
            print("Error while connecting to database...")

    def retrive(self, query):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
            myresult = cursor.fetchall()
            return myresult
        except Exception:
            print("Error while querying table")

    def update(self, query):
        try:
            mycursor = self.mydb.cursor()
            mycursor.execute(query)
            self.mydb.commit()
        except Exception as e:
            print(e)
            print("Error while updating table")

    def quit_connection(self):
        self.mydb.close()
