from app.bahasa_project import *
import pytest

def test_lexical_entry():
    """Tests the creation of the LexicalEntry class:"""
    le = LexicalEntry(written_form="untuk", origin=3)
    assert le.written_form == "untuk"
    assert le.origin == "Malay"

    le2 = LexicalEntry(written_form="emoji", origin=1)
    assert le2.written_form == "emoji"
    assert le2.origin == "Japanese"

def test_make_sense():
    """Creates a Sense subclass of LexicalEntry and confirms its creation:"""
    sense1 = Sense(written_form="advocat", origin=0, pos=0, definition="lawyer")
    assert sense1.pos == "Noun"
    assert sense1.definition == "lawyer"
    assert sense1.written_form == "advocat"

def test_spoken_word():
    """Tests the ability to create a spoken word entry:"""
    spokenword1 = SpokenWord(written_form="sedikit", origin=3, pos=2, definition="little", es_in_word=1, \
                             e_type_list=["ɘ"], surface_IPA="sɘˈdikit", surface_simple="sɘdikit")
    assert spokenword1.surface_IPA == "sɘˈdikit"
    assert spokenword1.surface_simple == "sɘdikit"
    assert spokenword1.e_type_list == ["ɘ"]
    assert spokenword1.es_in_word == 1
    assert spokenword1.written_form == "sedikit"
    assert spokenword1.origin == "Malay"
    assert spokenword1.pos == "Adjective"
    assert spokenword1.definition == "little"
