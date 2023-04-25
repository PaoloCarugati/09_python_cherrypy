import cherrypy
#import cherrypy_cors

@cherrypy.expose
class MyController(object):
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

    USR = "Paolo"
    #PWD = "Qu&st@M1S€mbr@Un@P@$$w0rdS1cur@"
    PWD = "Password123"
    RLM = "BasicAuthREST"

    def validate_password(self, username, password):
        if (username == MyController.USR and password == MyController.PWD):
            return True
        else:
            return False

    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def GET(self, id=-1):
        print("ciao")
        if (int(id) == -1):
            return self.dischi
        else:
            #return self.dischi[int(id)]
            disco = [d for d in self.dischi if d["id"] == int(id)]
            if (len(disco) == 1):
                return (disco[0])
            else:
                cherrypy.response.status = 404
                return {} 


    #def POST(self, disco):
    #    self.dischi.append(disco)
    #    return len(self.dischi) -1


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        self.dischi.append(data)
        return {}


    @cherrypy.tools.json_out()
    def PUT(self, id=-1, **kwargs):
        #TODO
        return int(id)


    @cherrypy.tools.json_out()
    def DELETE(self, id=-1):
        index = -1
        for d in range(0, len(self.dischi)) :
            if self.dischi[d]["id"] == int(id):
                index = d
                break
        if index != -1:
            self.dischi.pop(index)
        return 0


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            #'tools.response_headers.headers': [('Content-Type', 'application/json')]
            #devo aggiungere l'header "Access-Control-Allow-Origin" per abilitare le richieste da un dominio differente
            'tools.response_headers.headers': [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')],
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': MyController.RLM,
            'tools.auth_basic.checkpassword': MyController.validate_password
        }
    }  

    cherrypy.quickstart(MyController(), '/dischi', conf)