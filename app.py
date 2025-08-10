### This file covers API communication and will be where Flask comes in! :)

## Imports shamelessly stolen from our example code as instructed :)
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

## Imports from app.services.py:
from app.services import *



## More shamelessly ripped off code from the course examples, per official recommendation:
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

## Calls the WordServices() function under "services" here:
services = WordServices()



## I could use this if I add documentation like in the Sanskrit demo:
@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()

## Returns a simple "OK" message to test if the Flask integration is working for my bahasa project:
@app.route("/test_flask", methods=["GET"])
def runner_of_the_flask():
    app.logger.info("/test_flask - Tested Flask integration.")
    #return jsonify({"msg": "OK"})
    return "OK"

## Returns word details on the submitted word, as long as it exists:
@app.route("/get_word_details", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def word_detail_getter():
    ## Takes bahasa Indonesia word input and returns a list of displayable word details:
    bahasa_word_data = request.get_json()
    app.logger.info("/get_word_details - bahasa_word_data = " + str(bahasa_word_data) + ".")
    if bahasa_word_data:
        ## Checks if the word exists in list of words in the database, then returns Jsonified word details if it exists,
        ## but returns an error message if the word is not in the database:
        ##
        ## The post request should be sent as "data='WORD'":
        word_to_analyze = bahasa_word_data["word"]
        app.logger.info("/get_word_details - word_to_analyze = " + str(word_to_analyze))
        result = services.find_word_details(word_to_analyze)
        app.logger.info("/get_word_details - result of 'services.find_word_details(word_to_analyze)':\n" + str(result))
        ## If the word does not exist in the database, all of its list entries will be None:
        if result[0] is None:
            return jsonify("word not in database")
        else:
            ## Converts each item in the original list to a string for compatibility reasons - and returns the list:
            result_list = [str(item) for item in result]
            return jsonify(result_list)
    else:
        return jsonify("epic fail")

## Starts up the Flask server
if __name__ == "__main__":
    app.run(host='0.0.0.0')