import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nemisha@10",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None
class EmployeeManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None

connection_instance=DbConnect()
connection_instance.get_connection()