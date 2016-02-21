import cherrypy


class Rest(object):
    exposed = True
    config = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }

    def __init__(self, Model):
        self.model = Model()

    @cherrypy.tools.json_out()
    def GET(self, id=None):
        return self.model.read(id)

    @cherrypy.tools.json_out()
    def DELETE(self, id):
        return self.model.delete(id)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        return self.model.create(
            cherrypy.request.json
        )

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, id):
        return self.model.update(
            id,
            cherrypy.request.json
        )
