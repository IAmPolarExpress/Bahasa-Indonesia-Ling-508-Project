## This is the file that will manage the services layer, once I add that.

## This is where I can implement my use cases, which will in turn call the other data that has been written.
## I will wait to write code here until after I have reviewed Unit 5.  I think checking out the Week 5 branch of the
## Sanskrit course demo could help here too:
## https://github.com/jjberry-508/sanskrit-508/blob/week5/app/services.py

from db.mysql_repository import *

class WordServices:

    ## Init code shamelessly ripped off from the course Sanskrit code :)
    def __init__(self):
        ## Sets the repo to use MySQLRepository
        self.workingrepo = MySQLRepository

        ## Sets up the working_lexicon using the MySQLRepository's "_load_lexicon()" feature:
        self.working_lexicon = self.workingrepo().load_lexicon()
        print(self.working_lexicon)

    ### MASTER CALL FOR ALL IMPLEMENTED WORD DETAILS ###
    def find_word_details(self, word: str):
        ## Returns all implemented word details methods from the Services layer
        return [self.find_surface_simple(word),self.find_IPA(word),self.find_word_origin(word)]

    ### USE CASE 1: Returns word class (verb, noun, etc. in the form of text) ###
    def find_word_class(self, word: str) -> PartOfSpeech:
        raise NotImplementedError

    ### USE CASE 2: Returns a syllabic breakdown of the word ###
    def find_syllables(self, word: str):
        ## This is not yet coded into my system, and I may remove this feature before finishing the project, although
        ## it was one of my original goals.  Even if I do remove it, I would like to add it later, so I am going to
        ## leave this here for the future.
        raise NotImplementedError

    ### USE CASE 3: Returns the simplified surface form, which replaces "e" with a schwa based on the IPA spelling ###
    def find_surface_simple(self, word: str) -> str:
        for entry in self.working_lexicon:
            if entry.written_form == word:
                return entry.surface_simple

    ### USE CASE 3.5: Returns the IPA form of the word (which is what I shifted towards after I started to replace USE CASE 2 ###
    def find_IPA(self, word: str) -> str:
        for entry in self.working_lexicon:
            if entry.written_form == word:
                return entry.surface_IPA

    ### USE CASE 4: Returns the origin of the word entered ###
    def find_word_origin(self, word: str) -> OriginLanguage:
        ## Prints the current word being used for debug purposes:
        print("current word = " + str(word))
        ## Takes the list of LexicalEntries in the Lexicon and returns the OriginLanguage of the matching string or
        ## returns an error if the word is not in the Lexicon:
        for entry in self.working_lexicon:
            if entry.written_form == word:
                return entry.origin