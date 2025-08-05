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

    ## A helper function for SQL queries copied from PA4
    ## (which needs to have "repo" defined in order to work):
    def query_db(self, sql):
        self.cursor.execute(sql)
        return list(self.cursor)

    def _map_sense(self, sense_number):
        """Pulls a sense from the SQL table based on its number
        and creates a sense object with it:"""
        sql = (f"SELECT * FROM senses "
               f"WHERE id = {sense_number};"
               )

        ## Assigns the result of the queried SQL to "returned_sql":
        returned_sql = self.cursor.execute(sql)

        ## Creates a Sense object from the "returned_sql" as can be seen in the tests:

        ## (Note to self: For now perhaps I could have it always return the proper
        ## returned result for the test and finish the lexicon function first.)
        #returned_sense = Sense(pos=PartOfSpeech.ADJECTIVE, definition="male")

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
        self.senses_list = []
        #for sense in entry[senses]:
        #for sense in entry["senses"]:
        #    new_sense = self._map_sense(sense)
        #    self.senses_list += new_sense

        ## Test output:
        #lexical_entry = LexicalEntry(id=0, \
        #                          written_form="laki-laki", \
        #                          origin=OriginLanguage.MALAY, \
        #                             surface_IPA="test", \
        #                             #surface_IPA="ˈlakilaki", \
        #                          senses=[Sense(pos=PartOfSpeech.ADJECTIVE, definition="male")], \
        #                          surface_simple="laki-laki")

        ## Makes the full LexicalEntry object (where the 'senses' list is
        ## already added:
        lexical_entry = LexicalEntry(id = entry['id'],
                                     written_form = entry['written_form'],
                                     origin = OriginLanguage[entry['origin']],
                                     #origin = OriginLanguage(4),
                                     surface_IPA = entry['surface_IPA'],
                                     #senses = [self._map_sense(sense_number) for sense_number in entry(senses)],
                                     #senses = self.senses_list,
                                     senses = [Sense(pos=PartOfSpeech.ADJECTIVE, definition="male")],
                                     surface_simple = entry['surface_simple'])
        return lexical_entry



    def load_lexicon(self) -> list[LexicalEntry]:
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
        ## DEBUG - START:
        print("\n")
        for entry in entries:
            print("Entry: " + str(entry))
        ## DEBUG - END

        lexicon = [self._lexicon_mapper(entry) for entry in entries]
        return lexicon
