import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "index"

#questo if significa che esegue il blocco se il file è eseguito come script ma non se è importato come modulo
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,              #utilizzo la sessione
            'tools.sessions.timeout': 60,           #definisco la durata della sessione (60 minuti)
            #'response.timeout': 6000,              #definisce il tempo massimo di risposta
            #'response.stream': True,               #utilizzato quando devo restituire uno stream di dati
        }
    }

    #cherrypy.config.update({'server.socket_host': '64.72.221.48'})
    cherrypy.config.update({'server.socket_port': 80})

    cherrypy.quickstart(Root(), '/', conf)
 