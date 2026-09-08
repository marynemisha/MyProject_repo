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
    pass

connection_instance=DbConnect()
connection_instance.get_connection()