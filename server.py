import json
import Product
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class MyServer(BaseHTTPRequestHandler):
    # Gestione delle richieste GET
    def do_GET(self):
        if self.path == '/products':
            # Logica per ottenere tutte le risorse
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Invio delle risorse come JSON
            resources =Product.FetchAll()
            self.wfile.write(json.dumps(resources).encode())
        elif self.path.startswith('/product/'):#{'id': id_product, 'name': f'Resource {id_product}'}
            # Estrai l'ID della risorsa dalla richiesta
            id_product = int(self.path.split('/')[-1])
            # Logica per ottenere una singola risorsa con ID specifico
            products =Product.Find(id_product)
            if products is not None:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                jsondata={'id':products['id'],'name':products['name'],'brand':products['brand'],'price':products['price']}
                self.wfile.write(json.dumps(jsondata).encode())
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
        if self.path == '/product':
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])#lunghezza del corpo in byte
            post_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            product = json.loads(post_data)
            Product.Create(product['name'],product['brand'],product['price'])
            self.send_response(201)
            self.end_headers()
            self.wfile.write(b'Resource created successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste PUT
    def do_PATCH(self):
        if self.path.startswith('/product/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            product = json.loads(put_data)
            Product.Update(product['name'],product['brand'],product['price'],resource_id)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Resource updated successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste DELETE
    def do_DELETE(self):
        if self.path.startswith('/produtc/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            Product.Delete(resource_id)
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

