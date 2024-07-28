from app.bahasa_project import *
import pytest

def test_lexical_entry():
    """Tests the creation of the LexicalEntry class:"""
    le = LexicalEntry(written_form="untuk", origin=OriginLanguage.MALAY)
    assert le.written_form == "untuk"
    assert le.origin == OriginLanguage.MALAY

    le2 = LexicalEntry(written_form="emoji", origin=OriginLanguage.JAPANESE)
    assert le2.written_form == "emoji"
    assert le2.origin == OriginLanguage.JAPANESE

def test_make_sense():
    """Creates a Sense subclass of LexicalEntry and confirms its creation:"""
    sense1 = Sense(written_form="advocat", origin=OriginLanguage.DUTCH, \
                   pos=PartOfSpeech.NOUN, \
                   definition="lawyer")
    assert sense1.pos == PartOfSpeech.NOUN
    assert sense1.definition == "lawyer"
    assert sense1.written_form == "advocat"

def test_spoken_word():
    """Tests the ability to create a spoken word entry:"""
    spokenword1 = SpokenWord(written_form="sedikit", origin=OriginLanguage.MALAY, \
                             pos=PartOfSpeech.ADJECTIVE, \
                             definition="little", es_in_word=1, \
                             e_type_list=["ɘ"], surface_IPA="sɘˈdikit", \
                             surface_simple="sɘdikit")
    assert spokenword1.surface_IPA == "sɘˈdikit"
    assert spokenword1.surface_simple == "sɘdikit"
    assert spokenword1.e_type_list == ["ɘ"]
    assert spokenword1.es_in_word == 1
    assert spokenword1.written_form == "sedikit"
    assert spokenword1.origin == OriginLanguage.MALAY
    assert spokenword1.pos == PartOfSpeech.ADJECTIVE
    assert spokenword1.definition == "little"
