import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        #http://localhost:8080
        return "<h1>index</h1>"

    @cherrypy.expose
    def path2(self):
        #http://localhost:8080/path2
        return "<h1>path2</h1>"

#cherrypy.quickstart(Root())
cherrypy.quickstart(Root(), '/root')