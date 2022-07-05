from flask import Flask
from requests import request
#from apiRoutes import configure_routes
from apiRoutes import configure_routes

import json
import pytest

#These need improvment, this is my first time writing 
#python bar a single function i wrote a few years back
#Need to come back to this 

def test_dummy_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/dummy'

    status = client.get(url)
    assert status.status_code == 200

def test_healthz_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/healthz'

    status = client.get(url)

    json_data = json.loads(status.data)
    assert 'db_healthy' in json_data
    assert status.status_code == 200

def test_count_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/count'

    status = client.get(url)
    assert status.status_code == 200

if __name__ == "__main__":
    pytest.main