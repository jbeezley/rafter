def app_config(root, extra):

    cfg = extra.copy()
    cfg.update({
        '/': {
            'tools.staticdir.root': root
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static'
        }
    })
    return cfg

mongo_config = {
    'MONGO_HOST': '127.0.0.1',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'rafter'
}
