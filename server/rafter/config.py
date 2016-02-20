import cherrypy


def app_config(root, extra):

    cfg = extra.copy()
    cfg.update({
        '/': {
            'tools.staticdir.root': root,
            'tools.db.on': True,
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static'
        }
    })
    return cfg
