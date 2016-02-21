import cherrypy

from .rest import Rest
from .models import User


class Main(object):

    @cherrypy.expose
    def index(self):
        return 'Main page'

tree = {
    '/user': Rest(User)
}
