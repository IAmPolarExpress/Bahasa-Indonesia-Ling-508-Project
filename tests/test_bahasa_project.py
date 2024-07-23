from app.bahasa_project import *
import pytest

def test_lexical_entry():
    """Tests the creation of the LexicalEntry class:"""
    le = LexicalEntry(written_form="untuk", origin=3)
    assert le.written_form == "untuk"
    assert le.origin == 3

    le2 = LexicalEntry(written_form="emoji", origin=1)
    assert le2.written_form == "emoji"
    assert le2.origin == 1

def test_make_sense():
    """Creates a Sense subclass of LexicalEntry and confirms its creation:"""
    sense1 = Sense(written_form="advocat", origin=0, pos=0, definition="lawyer")
    assert sense1.pos == 0
    assert sense1.definition == "lawyer"
    assert sense1.written_form == "advocat"

#def test_test():
#    testdata = TestData()
#    assert testdata.four == 4

def test_spoken_word():
    """Tests the ability to create a spoken word entry:"""
    spokenword1 = SpokenWord(written_form="sedikit", origin=3, pos=2, definition="little", es_in_word=1, \
                             e_type_list=["ɘ"], surface_IPA="sɘˈdikit", surface_simple="sɘdikit")
    assert spokenword1.surface_IPA == "sɘˈdikit"
    assert spokenword1.surface_simple == "sɘdikit"
    assert spokenword1.e_type_list == ["ɘ"]
    assert spokenword1.es_in_word == 1
    assert spokenword1.written_form == "sedikit"
    assert spokenword1.origin == 3
    assert spokenword1.pos == 2
    assert spokenword1.definition == "little"




"""
def sanity_check():
    #This is mainly a joke but I am using it to remind myself to take breaks:
    options = ["sane","insane"]
    me_right_now = options[0]
    assert me_right_now == "sane"
"""

"""   ORIGINAL TESTS
## Test make_lexical_entry():
def test_make_lexical_entry():
    assert make_lexical_entry("untuk",3) == LexicalEntry(written_form="untuk", origin=3)
    assert make_lexical_entry("tidak",3) == LexicalEntry(written_form="tidak", origin=3)
    assert make_lexical_entry("emoji",1) == LexicalEntry(written_form="emoji", origin=1)
    assert make_lexical_entry("advokat",0) == LexicalEntry(written_form="advokat", origin=0)

## Tests trickier words, like reduplicated ones:
def test_tricky_lexical_entry():
    assert make_lexical_entry("laki-laki",3) == LexicalEntry(written_form="laki-laki", origin=3)

## Tests to make sure that too few or too many arguments returns an error:
def test_make_lexical_entry_wrong_arg_number():
    with pytest.raises(ValueError):
        make_lexical_entry("sedikit")
    with pytest.raises(ValueError):
        make_lexical_entry("sedikit",3,"meep")

## Tests to make sure that an incorrect language number or argument order fails:
def test_make_lexical_entry_wrong_arg_types():
    with pytest.raises(ValueError):
        make_lexical_entry("sedikit",8)
    with pytest.raises(ValueError):
        make_lexical_entry(3,"sedikit")
"""


