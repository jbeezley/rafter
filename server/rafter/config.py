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
