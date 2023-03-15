import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self, param="niente"):
    #def index(self, param):
        html = """
            <h1>index</h1>
            <p style='font-size: 22px;'>
                param = """, param, "</p>"
        return html

    @cherrypy.expose
    def index2(self, param1="niente", param2="niente"):
        html = """
            <h1>index</h1>
            <p>
                param1 = """, param1, """
                <br />
                param2 = """, param2, "</p>"
        return html

cherrypy.quickstart(Root())
