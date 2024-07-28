## This is the main document to track data-class creation in my Bahasa Indonesia project:

## IMPORTS:
from enum import Enum

## ENUMERATIONS:

class OriginLanguage(Enum):
    DUTCH = 1
    JAPANESE = 2
    ENGLISH = 3
    MALAY = 4
    OTHER = 5

class PartOfSpeech(Enum):
    NOUN = 1
    VERB = 2
    ADJECTIVE = 3
    ADVERB = 4
    PREPOSITION = 5
    CONJUNCTION = 6
    INTERJECTION = 7

## CLASS DEFINITIONS:

class LexicalEntry:

    def __init__(self, written_form: str, origin: OriginLanguage):
        """Uses the input to create the chosen LexicalEntry:"""
        ## Defines the values:
        self.written_form = written_form
        self.origin = origin

class Sense(LexicalEntry):

    def __init__(self, written_form: str, origin: OriginLanguage, pos: PartOfSpeech, definition: str):
        super().__init__(written_form, origin)
        self.pos = PartOfSpeech(pos)
        self.definition = definition

class SpokenWord(Sense):

    def __init__(self, written_form: str, origin: OriginLanguage, pos: PartOfSpeech, \
                 definition: str, es_in_word: int, e_type_list: list, surface_IPA: str, \
                 surface_simple: str):
        super().__init__(written_form, origin, pos, definition)
        self.es_in_word = es_in_word
        self.e_type_list = e_type_list
        self.surface_IPA = surface_IPA
        self.surface_simple = surface_simple

## CLASS CREATION METHODS:
def make_lexical_entry(word,language) -> LexicalEntry:
    res = LexicalEntry(written_form=word, origin=language)
    return res