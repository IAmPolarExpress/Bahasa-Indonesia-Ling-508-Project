# *API Documentation*

## Before Connecting

Remember to use ```git clone``` to clone the repository to your local device, then use your terminal and Docker to build and launch the necessary containers using ```docker-compose up```.  (For convenience, you can even view this whole project in an IDE like PyCharm!)  Check out the ReadMe for further details on initial setup.

Everything will run on your local device on port 5000.  So you can make all your http requests on ```localhost:5000```.

# *Direct API Connection Method*

## Confirming the API was Launched with "test_flask":

If you want to confirm that everything is running properly, you can launch a ```GET``` request using ```test_flask``` to ensure everything is working.  If you get an ```OK``` response, that means that everything is working properly!

Here is an example [httpie](https://httpie.io/) request:
```http GET localhost:5000/test_flask```

Here is the expected output if all is working properly:
```OK```

## Returning Word Details Using ```get_word_details```:

You can currently receive details on three Indonesian words, although I plan to expand this in the future.  If you try to use a word that does not exist, you will get an error telling you that the word was not in the database.

To send the word that you want to get details on, you will need to include the word as a string attached to "word" in a ```POST``` request.

Here is an example httpie request:
```http POST localhost:/get_word_details word="belajar"```

Here is the expected output for that input:
```
[
    "bəlajar",
    "bəˈladʒar",
    "OriginLanguage.MALAY"
]
```

It is possible to send a request on a word that does not exist in the database, such as this:
```http POST localhost:/get_word_details word="supercalifragilisticexpialidocious"```

The output you will get in that case is this:
```("msg": "word not in database"}```

# *Using the HTML Page*

## Opening ```bahasa.html```:

Included in this project is a simple HTML page that you can open in your preferred web browser, like Mozilla Firefox or Google Chrome!  It is located in the ```web/bahasa.html``` directory.  Most operating systems will allow you to launch it by double-clicking the file within your file explorer.

Please note that you will still need to start up the docker containers, as listed above, before utilizing the webpage.

Once the webpage is open, you can type the word that you want to look up and it will return details on it after you click submit.

For example, you might type ```belajar``` and in the dedicated output portion of the webpage it will return:
```
[
    "bəlajar",
    "bəˈladʒar",
    "OriginLanguage.MALAY"
]
```

This makes it an even more convenient way to do searches than utilizing the API for many people!

