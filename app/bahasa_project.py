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

class Sense:

    def __init__(self, pos: PartOfSpeech, definition: str):
        self.pos = pos
        self.definition = definition

    #def print_sense(self):
    #    return "pos = " + str(self.pos) + "\ndefinition = " + str(self.definition)

class LexicalEntry:

    def __init__(self, id: str, written_form: str, origin: OriginLanguage, surface_IPA: str, \
                 senses: [Sense]=[], surface_simple: str="NULL"):
        """Uses the input to create the chosen LexicalEntry:
        
        NOTE: If 'surface_simple' is unknown at the outset, it is set to 'NULL'
        by default so that the simple output can be determined using the
        'get_surface_simple()' function below."""
        ## Defines the values:
        self.id = id
        self.written_form = written_form
        self.origin = origin
        self.senses = senses
        self.surface_IPA = surface_IPA
        if surface_simple != "NULL":
            self.surface_simple = surface_simple
        else:
            self.surface_simple = self.get_surface_simple()

    def __eq__(self, other):
        #return self.id == other.id and self.written_form == other.written_form and \
        #    self.origin == other.origin and self.senses == other.senses and \
        #    self.surface_IPA == other.surface_IPA and self.surface_simple == other.surface_simple

        ## DEBUG - START
        ## id
        print("self.id = " + str(self.id) + "\nother.id = " + str(other.id) + "\n[Not compared]\n")
        ## written_form
        print("self.written_form = " + str(self.written_form) + "\nother.written_form = " \
              + str(other.written_form) + "\nResult of \"self.written_form == other.written_form\" = " \
              + str(self.written_form == other.written_form) + "\n")
        ## origin
        print("self.origin = " + str(self.origin) + "\nother.origin = " \
              + str(other.origin) + "\nResult of \"self.origin == other.origin\" = " \
              + str(self.origin == other.origin) + "\n")
        ## surface_IPA
        print("self.surface_IPA = " + str(self.surface_IPA) + "\nother.surface_IPA = " \
              + str(other.surface_IPA) + "\nResult of \"self.surface_IPA == other.surface_IPA\" = " \
              + str(self.surface_IPA == other.surface_IPA) + "\n")
        ## DEBUG - END

        return self.written_form == other.written_form and self.origin == other.origin and \
            self.surface_IPA == other.surface_IPA

    def get_surface_simple(self):
        """Uses the IPA to check for present 'e' or 'ə' characters and overwrites the
        'e's in the word which should be schwas to the correct 'ə' symbol.  This is
        designed to help non-IPA users see pronunciation in a simpler way:

        NOTICE: NOT YET IMPLEMENTED"""
        raise NotImplementedError