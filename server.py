import json
import Product
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class MyServer(BaseHTTPRequestHandler):
    # Gestione delle richieste GET
    def do_GET(self):
        if self.path == '/api/resource':
            # Logica per ottenere tutte le risorse
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Invio delle risorse come JSON
            resources = [{'id': 1, 'name': 'Resource 1'}, {'id': 2, 'name': 'Resource 2'}]
            self.wfile.write(json.dumps(resources).encode())
        elif self.path.startswith('/api/resource/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            # Logica per ottenere una singola risorsa con ID specifico
            resource = {'id': resource_id, 'name': f'Resource {resource_id}'}
            if resource_id in [1, 2]:#indica per lindice del json sopra
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(resource).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Resource not found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste POST
    def do_POST(self):
        if self.path == '/api/resource':
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])#lunghezza del corpo in byte
            post_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            new_resource = json.loads(post_data)
            # Simulazione di salvataggio della nuova risorsa nel database
            # Qui potresti effettuare un'operazione di scrittura nel database
            self.send_response(201)
            self.end_headers()
            self.wfile.write(b'Resource created successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste PUT
    def do_PUT(self):
        if self.path.startswith('/api/resource/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            updated_resource = json.loads(put_data)
            # Simulazione di aggiornamento della risorsa nel database
            # Qui potresti effettuare un'operazione di aggiornamento nel database
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Resource updated successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste DELETE
    def do_DELETE(self):
        if self.path.startswith('/api/resource/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            # Simulazione di eliminazione della risorsa dal database
            # Qui potresti effettuare un'operazione di eliminazione nel database
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Resource deleted successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')
if __name__ == "__main__":
    # Definizione dell'host e della porta del server
    hostName = "localhost"
    serverPort = 8080

    # Creazione dell'istanza del server HTTP, specificando host, porta e classe handler
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Avvio del server, che rimane in ascolto per le richieste
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Gestione di un'interruzione da tastiera per fermare il server in modo pulito
        pass

    # Chiusura del server
    webServer.server_close()
    # Stampaggio a console del messaggio di chiusura del server
    print("Server stopped.")

