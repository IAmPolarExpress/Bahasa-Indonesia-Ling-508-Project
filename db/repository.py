### IMPORTS:

## Imports the abstract method function:
import abc

## Imports the LexicalEntry class from my main thread.  I may eventually move
## these class definitions elsewhere, but for now this is where it is at:
from app.bahasa_project import LexicalEntry


### REPOSITORY ABSTRACT CLASS:

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def _load_lexicon(self) -> list[LexicalEntry]:
        """All repositories must create a load_lexicon method overwriting this
        one in order to function:"""
        raise NotImplementedError