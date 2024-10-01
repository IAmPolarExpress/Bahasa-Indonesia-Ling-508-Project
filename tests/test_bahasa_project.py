#from app.bahasa_project import * # This is now imported already from db.mysql_repository.py
from db.mysql_repository import *
import pytest

def test_easy_wins():
    """Gives a motivational boost. If this fails, something is seriously wrong:"""
    print("\n\n\nYou got this!!!\n         :D\n")
    pass

def test_make_sense():
    """Creates a Sense class and confirms its creation:"""
    sense1 = Sense(pos=PartOfSpeech.NOUN, definition="lawyer")
    assert sense1.pos == PartOfSpeech.NOUN
    assert sense1.definition == "lawyer"

def test_lexical_entry():
    """Tests the creation of the LexicalEntry class:"""
    le = LexicalEntry(id=0, written_form="untuk", origin=OriginLanguage.MALAY, \
                      surface_IPA="ˈuntuk", \
                      senses=[Sense(pos=PartOfSpeech.PREPOSITION, definition="but")], \
                      surface_simple="untuk")
    assert le.id == 0
    assert le.written_form == "untuk"
    assert le.origin == OriginLanguage.MALAY
    assert le.surface_IPA == "ˈuntuk"
    assert le.surface_simple == "untuk"

    ## Tests that Sense classes can have their data pulled from a LexicalEntry class:
    #assert le.senses[0] == Sense(pos=PartOfSpeech.PREPOSITION, definition="but")
    #first_sense = le.senses[0]
    #test_print_sense = first_sense.print_sense
    #print(test_print_sense)

def test_SQL_import():
    """Tests if data can be properly pulled from the database that SQL
    initialized:"""
    ## Uses '_load_lexicon' to load the lexicon from the SQL server:
    repo = MySQLRepository()
    test_lexicon = repo._load_lexicon()

    ## Asserts that there are more than zero entries in the lexicon:
    assert len(test_lexicon) >= 1
    if len(test_lexicon) >= 1:
        print("\n\nThere is more than one line in 'test_lexicon'!\n     This is good!\n\n")
        print("Number of lines in 'test_lexicon' = " + str(len(test_lexicon)))

    ## Asserts that the lexical entry for "laki-laki" is present:
    laki_laki_test = LexicalEntry(id=0, \
                                  written_form="laki-laki", \
                                  origin=OriginLanguage.MALAY, \
                                  surface_IPA="ˈlakilaki", \
                                  #surface_IPA="debugtest", \
                                  senses=[Sense(pos=PartOfSpeech.ADJECTIVE, definition="male")], \
                                  surface_simple="laki-laki")
    assert laki_laki_test in test_lexicon
