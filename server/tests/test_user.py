class TestUserAPI(object):

    users = [
        {
            'name': 'name1',
            'password': 'password1'
        }, {
            'name': 'name2',
            'password': 'password2'
        }, {
            'name': 'name3',
            'password': 'password3'
        }
    ]

    def test_empty_list(self, http):
        resp = http.get('/user')
        assert resp.json == []

    def test_invalid_id(self, http):
        resp = http.get('/user/1', status=404)
        assert resp.status_int == 404

    def test_create_users(self, http):
        for user in self.users:
            resp = http.post_json('/user', user)
            assert resp.json.get('_id') is not None
            user['_id'] = resp.json['_id']
            assert resp.json == user

    def test_list_3users(self, http):
        resp = http.get('/user')
        assert resp.json == self.users

    def test_delete_user(self, http):
        resp = http.delete('/user/' + self.users[1]['_id'])
        assert resp.json is True

    def test_list_2users(self, http):
        resp = http.get('/user')
        assert resp.json == [self.users[0], self.users[2]]

    def test_modify_user(self, http):
        user = {
            'name': 'John Doe',
            'password': 'newpassword'
        }
        resp = http.put_json('/user/' + self.users[0]['_id'], user)
        assert resp.status_int == 200

        resp = http.get('/user/' + self.users[0]['_id'])
        assert resp.json['_id'] == self.users[0]['_id']
        assert resp.json['name'] == user['name']
        assert resp.json['password'] == user['password']

    def test_delete_modified_user(self, http):
        resp = http.delete('/user/' + self.users[0]['_id'])
        assert resp.json is True

        resp = http.get('/user')
        assert resp.json == [self.users[2]]

    def test_invalid(self, http):
        resp = http.get('/invalid_endpoint', status=404)
        assert resp.status_int == 404
