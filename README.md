# *What is this?*

This repository contains the data for my Linguistics 508 project, which allows users to ping its API (or use a helpful web page) for the purposes of pulling up information on words in bahasa Indonesia.

Currently, this is in a proof-of-concept stage, and will only return true results with the words "untuk", "laki-laki", and "belajar".

Additionally, it currently only returns the following unlabeled details:
1. The simplified surface form, which only differentiates between "e" pronunciation and maintains bahasa Indonesia spelling (see "belajar").
2. The International Phonetic Alphabet form.  (The words "laki-laki" and "belajar" provide more distinct examples from their original spellings.)
3. The original language where the word came from.  Currently, as is the case with most words in bahasa Indonesia, the three examples are all from bahasa Malay.

# *How do I run this?*

Clone the project onto your device using ```git clone``` and then use ```docker-compose up``` from the corresponding directory.  (If you want to, you can even open up the project to view the source code yourself in an IDE like PyCharm!)  Once the Docker containers are running, you can make http requests to it in order to pull up information on the word of your choosing.

There are currently two commands that can be executed on port 5000.  I have them listed as with example [httpie](https://httpie.io/) commands for reference:
* test_flask: This is a GET command which will confirm that the Flask container is working.  Example: ```http GET localhost:5000/test_flask```
* get_word_details: This is a POST command which will let you request details on a word in bahasa.  Example: ```http POST localhost:/get_word_details data="belajar"```

# *What's next?*
I plan to expand this project by integrating a full Indonesian word database, improve efficiency by having the SQL calls made on a call-by-call basis rather than having the whole database loaded into memory, and perhaps even make my original word segmentation and phonics goals become a reality, even though I set them aside for other goals for now.  I also consider it essential that I get functionality for multiple word Senses up and running long-term.

The framework for this software is something that I also hope to make more "portable" and able to be adapted for other languages and language types.  Right now, all of the SQL database stuff is "baked in", but I would like to make it more modular.  That is beyond the scope of the course that this project was for, of course, but it is something that I would love to make happen! :)


