## This is the main document to track data-class creation in my Bahasa Indonesia project:

## CLASS DEFINITIONS:
class LexicalEntry:

    def __init__(self, written_form:str, origin:int):
        """Uses the input to create the chosen LexicalEntry:"""
        self.written_form = written_form
        self.origin = origin

class Sense(LexicalEntry):

    def __init__(self, written_form:str, origin:int, pos:int, definition:str):
        super().__init__(written_form, origin)
        self.pos = pos
        self.definition = definition

class SpokenWord(Sense):

    def __init__(self, written_form:str, origin:int, pos:int, definition:str, \
                 es_in_word:int, e_type_list:list, surface_IPA:str, surface_simple:str):
        super().__init__(written_form, origin, pos, definition)
        self.es_in_word = es_in_word
        self.e_type_list = e_type_list
        self.surface_IPA = surface_IPA
        self.surface_simple = surface_simple

class TestData():
    def __init__(self):
        self.four = 4

## CLASS CREATION METHODS:
def make_lexical_entry(word,language) -> LexicalEntry:
    res = LexicalEntry(written_form=word, origin=language)
    return res