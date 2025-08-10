#from app.bahasa_project import * # This is now imported already from db.mysql_repository.py
#from db.mysql_repository import * # This is now imported already from app.services
import app.services
from app.services import *
import pytest

def test_easy_wins():
    """Gives a motivational boost. If this fails, something is seriously wrong:"""
    print("\n\n\nYou got this!!!\n         :D\n\n\n\n\nNOTE: THESE TESTS WILL ONLY COOPERATE WHEN \
    'mysql_repository.py' is configured to run locally and you are running 'docker-compose up' from the terminal.\n")
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
    test_lexicon = repo.load_lexicon()

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
                                  #surface_IPA="test", \
                                  senses=[Sense(pos=PartOfSpeech.ADJECTIVE, definition="male")], \
                                  surface_simple="laki-laki")
                                  #surface_simple="test2")
    assert laki_laki_test in test_lexicon

def test_service_layer_word_origin():
    ## Word "untuk" should return origin "MALAY":
    untuktest = app.services.WordServices()
    untuktestresult = untuktest.find_word_origin("untuk")
    assert untuktestresult == OriginLanguage.MALAY

def test_service_layer_word_details():
    ## Returns all currently implemented word details in list form using the "find_word_details()" method:
    ##
    ## NOTE: This test will need to be updated as I improve and revise the "find_word_details()" method!
    belajartest = app.services.WordServices()
    belajartestresult = belajartest.find_word_details("belajar")
    assert belajartestresult == ["bəlajar","bəˈladʒar",OriginLanguage.MALAY]
