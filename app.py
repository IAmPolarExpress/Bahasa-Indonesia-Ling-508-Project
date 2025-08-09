### This file covers API communication and will be where Flask comes in! :)

## Imports shamelessly stolen from our example code as instructed :)
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

## Imports from app.services.py:
#from app.services import *
from app.services import WordServices
#from services import WordServices



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
#services = services.WordServices()




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
    print("bahasa_word_data = " + str(bahasa_word_data))
    if bahasa_word_data:
        return "Meap!"
    else:
        return '{"msg": "epic fail"}'

        ## Takes JSON input, converts it to a Python dictionary, and assigns it to "jdata":
        #jdata = request.get_json()
        #if jdata:
        #    ## Appends "jdata" to "data" list:
        #    #print("\n\nimported 'jdata' = " + str(jdata))
        #    #print("\n'data' list pre-update = " + str(data))
        #    data.append(jdata)
        #    #print("\n\nupdated 'data' = " + str(data))
        #    return '{"msg": "success"}'
        #else:
        #    return '{"msg": "failure"}'

#@app.route("/get_word_details", methods=["GET"])
#def data_get():
#    ## Returns Jsonified contents of data
#    json_data = jsonify(data)
#    #print("\n\nFeel the rhythm, feel the rhyme!  Come on now, it's debug time!\n\ndata:\n" + str(data) + "\n\njson_data:\n" + str(json_data))
#    return json_data


### Example from class code:
#@app.route("/generate", methods=["GET"])
#def generate_words():
#    services.generate_words()
#    app.logger.info("/generate - Generated words.")
#    return jsonify({"msg": "success"})

## Starts up the Flask server
if __name__ == "__main__":
    app.run(host='0.0.0.0')