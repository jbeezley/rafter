class TestApplicationMain(object):

    def test_get_request(self, http):
        resp = http.get('/')
        assert resp.status_int == 200

    def test_invalid(self, http):
        resp = http.get('/invalid_endpoint', status=404)
        assert resp.status_int == 404
