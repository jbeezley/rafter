import pytest
import webtest

from rafter.config import mongo_config
from rafter.server import application
from rafter.db import get_connection

mongo_config['MONGO_DBNAME'] = 'rafter-test'


@pytest.fixture(scope='module')
def http():
    get_connection().drop_database(mongo_config['MONGO_DBNAME'])
    return webtest.TestApp(application())
