### This file covers API communication and will be where Flask comes in! :)

## Imports shamelessly stolen from our example code as instructed :)
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#from logging.config import dictConfig

from app.services import WordServices