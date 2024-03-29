import sqlite3
class DatabaseConnection:
    def __init__(self,host):
        self.connection=None
        self.host=host

    def __enter__(self)->sqlite3.connection:
        self.connection=sqlite3.connect(self.host)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.commit()
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()



