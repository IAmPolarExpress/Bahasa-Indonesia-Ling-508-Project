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

    def map_sense(self):
        ## Added this since I think sql functions like this will be needed but also
        ## left them unimplemented because I still do not understand how all of the
        ## code for SQL and Python relates to each other.
        raise NotImplementedError

    def map_lexical_entry(self):
        raise NotImplementedError

    def load_lexicon(self):
        raise NotImplementedError
