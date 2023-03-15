import cherrypy

class Root(object):
    @cherrypy.expose
    def html(self):
        #se non specifico nulla per quanto riguarda il content type si assume che sia in formato HTML
        return "<i>html</i>"
    
    @cherrypy.expose
    def plaintext(self):
        #questa è l'impostazione per il content type in formato testo
        cherrypy.response.headers['Content-Type'] = "text/plain"
        return "<i>plaintext</i>"

    @cherrypy.expose
    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def json(self):
        #questa è l'impostazione per il content type in formato JSON
        #(in realtà la riga sotto non serve, si usava nelle vecchie versioni di cherrypy)
        #cherrypy.response.headers['Content-Type'] = "application/json"
        message = { "message" : "ciao" }
        return message

    @cherrypy.expose
    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def jsonlista(self):
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
        return dischi

cherrypy.quickstart(Root())
