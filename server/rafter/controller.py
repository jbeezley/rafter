import cherrypy


class Main(object):
    exposed = True

    def __init__(self):
        self._saved = {}

    @cherrypy.tools.json_out()
    def GET(self):
        return self._saved

    def DELETE(self):
        self._saved = {}

    @cherrypy.tools.json_in()
    def POST(self):
        self._saved = cherrypy.request.json
