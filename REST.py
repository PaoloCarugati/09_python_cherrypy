import cherrypy

@cherrypy.expose
class StringGeneratorWebService(object):
    dischi = [
        {
        "id": 1,
        "title": "Songs in the key of life",
        "artist": "Stevie Wonder",
        "year": 1976,
        "company": "Motown"
        },
        {
        "id": 2,
        "title": "Kind of Blue",
        "artist": "Miles Davis",
        "year": 1959,
        "company": "Columbia"      
        },
        {
        "id": 3,
        "title": "Synchronicity",
        "artist": "The Police",
        "year": 1983,
        "company": "A&M"      
        },
        {
        "id": 4,
        "title": "Bach - Goldberg Variations",
        "artist": "Glenn Gould",
        "year": 1955,
        "company": "Sony Classical"      
        }    
    ]


    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def GET(self, id=-1):
        if (int(id) == -1):
            return self.dischi
        else:
            return self.dischi[int(id)]


    def POST(self, disco):
        self.dischi.append(disco)
        return len(self.dischi) -1


    def PUT(self, id=-1, **kwargs):
        #TODO
        return int(id)


    def DELETE(self, id=-1):
        self.dischi.pop(int(id))
        return 0


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }  

cherrypy.quickstart(StringGeneratorWebService(), '/dischi', conf)