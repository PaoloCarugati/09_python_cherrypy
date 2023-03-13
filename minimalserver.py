import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "index"

#questo if significa che esegue il blocco se il file è eseguito come script ma non se è importato come modulo
if __name__ == '__main__':
    cherrypy.quickstart(Root())
    #posso modificare il rooting della richiesta commentando la riga precedente e togliendo il commento da quella sotto
    #cherrypy.quickstart(Root(), '/root')
