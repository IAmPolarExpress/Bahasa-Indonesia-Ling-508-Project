## Tests the Flask integration into the project, similar to how Programming Assignment 6 did so:
import pytest
import json
from app.app import *

#### NOTE: I CAN ALSO TEST THINGS MANUALLY

## Hangs the fixtures to make the room look nicer /s
@pytest.fixture
def client():
    a = create_app()
    with a.test_client() as client:
        yield client

def test_flask_integration():
    ## Makes a call to a simple Flask test function that returns a basic "OK" message:
    def test_hello(client):
        """1,000,000-point test"""
        #rv = client.get('/test_flask')
        assert rv == "OK"
        #response = json.loads(rv.data)
        #if response.get("msg") == "OK":
        #    print("It worked!")
        #else:
        #    print("It didn't work!")
        #assert response.get("msg") == "OK"