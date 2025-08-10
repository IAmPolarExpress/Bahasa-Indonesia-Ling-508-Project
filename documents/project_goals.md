# *Original Goals*

As listed in Milestone 1, I wanted my project to return information about a word entered from bahasa Indonesia.  In my original project outline, that included these four goals and example outputs:

1. Returns the class of the word entered:
   Input: belajar
   Output: verb
2. Returns the syllabic breakdown of the word:
   Input: belajar
   Output: ["be","la","jar"]
3. Returns the phoneme of "e" used in the word, with the schwa replacing the "e" if applicable:
   Input: belajar
   Output: bəlajar
4. Returns information on if the word is a loan word from a stored database and what language it is from:
   Input: advokat
   Output: from Dutch "advocaat" meaning "lawyer"

# *Updated Goals*

As I consulted with the professor and further moved throughout the course, I focused on a narrower set of goals, while still leaving the door open for more complex stuff (like syllabic breakdowns) later on down the line.

I am now focusing on three use cases, with a fourth that I plan to implement more fully after I get multiple Sense objects implemented for a single word:

1. Returns the simplified phonetic spelling of a word for bahasa Indonesia speakers (only replacing certain "e" letters with the schwa as appropriate and maintaining the Indonesian spellings):
   Input: belajar
   Output: bəlajar
2. Returns the International Phonetic Alphabet spelling of a word:
   Input: belajar
   Output: bəˈladʒar
3. Returns the origin language of the word:
   Input: belajar
   Output: OriginLanguage.MALAY
       NOTE: In the near future, I would like to make this output more readable, only returning a simple "Original language is Malay." or something like that.

# *Short-Term Bonus Goal*

While I am not necessarily using this as a goal for the purpose of this course at the moment, I plan to shortly implement a way of reading out a list of word senses and the categories that they occupy.  This bonus goal is as follows:

4. Returns a list of word senses:
   Input: advocaat
   Output: [noun, lawyer]


