from db.repository import *
import mysql.connector


class MySQLRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            #'host': 'db',  # When you run this on your machine change it to 'localhost'
            'host': 'localhost',
            #'port': '3306',  # When you run this on your machine change it to '32000'
            'port': '32000',
            #'database': 'bahasa' # Change this to the main bahasa database before pushing
            'database': 'demobahasa'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def _map_sense(self, sense_number):
        """Pulls a sense from the SQL table based on its number
        and creates a sense object with it:"""
        sql = ("SELECT * FROM senses "
               "WHERE id = " + str(sense_number) + " "
               ";"
               )
        self.cursor.execute(sql)
        returned_sense = {
            'id': id,
            'pos': pos,
            'definition': definition
        }
        return returned_sense

    def _map_lexical_entry(self):
        ## Tbh I will probs remove this soon as it has pretty much been
        ## superceded by the '_lexicon_mapper' method below
        raise NotImplementedError

    def _lexicon_mapper(self, entry: dict) -> LexicalEntry:
        """Takes a dict of data and turns it into a LexicalEntry class,
        formulated properly:"""
        ## First matches up and appends any senses as Sense objects
        ## to the 'self.senses_list' list:
        senses_list = []
        for sense in entry[senses]:
            new_sense = self._map_sense(sense)
            senses_list += new_sense

        ## Makes the full LexicalEntry object (where the 'senses' list is
        ## already added:
        lexical_entry = LexicalEntry(written_form = entry[written_form],
                                     origin = entry[origin],
                                     surface_IPA = entry[surface_IPA],
                                     #senses = [self._map_sense(sense_number) for sense_number in entry(senses)],
                                     senses = senses_list,
                                     surface_simple = entry[surface_simple])
        return lexical_entry



    def _load_lexicon(self) -> list[LexicalEntry]:
        """Pulls data from the SQL database and converts it to a list of
        LexicalEntry classes by making requests to the 'mapper()' method:"""
        sql = 'SELECT * FROM lexicon'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'written_form': form,
                    'origin': origin,
                    'surface_IPA': surface_ipa,
                    ## Must turn the list of senses into a Python list:
                    'senses': senses,
                    'surface_simple': surface_simple
                    } for (id, form, origin, surface_ipa, senses, \
                           surface_simple) in self.cursor]
        lexicon = [self._lexicon_mapper(entry) for entry in entries]
        return lexicon
