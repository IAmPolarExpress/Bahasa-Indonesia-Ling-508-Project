from app.bahasa_project import *
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
    le = LexicalEntry(written_form="untuk", origin=OriginLanguage.MALAY, \
                      surface_IPA="ˈuntuk", \
                      senses=[Sense(pos=PartOfSpeech.PREPOSITION, definition="but")], \
                      surface_simple="untuk")
    assert le.written_form == "untuk"
    assert le.origin == OriginLanguage.MALAY
    assert le.surface_IPA == "ˈuntuk"
    assert le.surface_simple == "untuk"

    ## Tests that Sense classes can have their data pulled from a LexicalEntry class:
    #assert le.senses[0] == Sense(pos=PartOfSpeech.PREPOSITION, definition="but")
