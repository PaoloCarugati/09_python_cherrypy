import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        #http://localhost:8080
        return "index"

    @cherrypy.expose
    def path2(self):
        #http://localhost:8080/path2
        return "path2"

cherrypy.quickstart(Root())
