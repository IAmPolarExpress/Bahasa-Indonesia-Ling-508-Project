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

## CLASS CREATION METHODS:
def make_lexical_entry(word,language) -> LexicalEntry:
    res = LexicalEntry(written_form=word, origin=language)
    return res