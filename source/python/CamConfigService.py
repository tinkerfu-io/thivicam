import cherrypy


class CamConfigService(object):
    @cherrypy.expose
    def index(self):
        return "Hello Pi"

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
                       
cherrypy.quickstart(CamConfigService())
