import mysql.connector


class MysqlRepository:

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',  # When you run this on your machine change it to 'localhost'
            #'host': 'localhost',
            'port': '3306',  # When you run this on your machine change it to '32000'
            #'port': '32000',
            'database': 'bahasa'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def map_part_of_speech(self):
        raise NotImplmentedError
