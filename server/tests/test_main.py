import pytest
import webtest

from rafter.server import application


@pytest.fixture()
def http():
    return webtest.TestApp(application())


class TestApplicationMain(object):

    def test_get_request(self, http):
        resp = http.get('/')
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert resp.json == {}

    def test_post_request(self, http):
        obj = {'a': True, 'b': False}
        resp = http.post_json('/', obj)
        assert resp.status_int == 200

        resp = http.get('/')
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert resp.json == obj

    def test_get_post_request(self, http):
        resp = http.get('/')
        assert resp.json == {}

        obj = {'a': True, 'b': False}
        resp = http.post_json('/', obj)

        resp = http.get('/')
        assert resp.json == obj

    def test_invalid(self, http):
        resp = http.get('/invalid_endpoint', status=404)
        assert resp.status_int == 404
