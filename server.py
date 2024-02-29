import json
import hashlib
from Product import *
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
            products=[]
            products = Product.FetchAll()
            json_temp2 = []
            for p in products:
                json_temp = {
                    "type": "products",
                    "id": p["id"],
                    "attributes": {
                        "nome": p["name"],
                        "marca": p["brand"],
                        "prezzo": p["price"],
                    },
                }
            json_temp2.append(json_temp)
            json_s = {"data": json_temp2}
            self.wfile.write(json.dumps(json_s).encode('utf-8'))
        elif self.path.startswith('/products/'):#{'id': id_product, 'name': f'Resource {id_product}'}
            # Estrai l'ID della risorsa dalla richiesta
            id_product = int(self.path.split('/')[-1])
            # Logica per ottenere una singola risorsa con ID specifico
            products =Product.Find(id_product)
            if products is not None:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                jsondata={'data:{type:"products",id:':id_product,',attributes:{nome':products[1],'marca':products[3],'prezzo':products[2]}
                self.wfile.write(json.dumps(jsondata).encode('utf-8'))
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
        if self.path == '/products':
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])#lunghezza del corpo in byte
            post_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            product = json.loads(post_data)
            Product.Create(product['nome'],product['prezzo'],product['marca'])
            self.send_response(201)
            self.end_headers()
            jsondata={'data:{type:"products",attributes:{name':product['nome'],'brand':product['prezzo'],'price':product['marca']}
            self.wfile.write(json.dumps(jsondata).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste PATCH
    def do_PATCH(self):
        if self.path.startswith('/products/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            # Ottieni il corpo della richiesta
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            # Analizza i dati JSON inviati nel corpo della richiesta
            product = json.loads(put_data)
            Product.Update(product['nome'],product['prezzo'],product['marca'],resource_id)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Resource updated successfully')
            products =Product.Find(resource_id)
            jsondata={'data:{type:"products",attributes:{name':products[1],'brand':products[3],'price':products[2]}
            self.wfile.write(json.dumps(jsondata).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')

    # Gestione delle richieste DELETE
    def do_DELETE(self):
        if self.path.startswith('/products/'):
            # Estrai l'ID della risorsa dalla richiesta
            resource_id = int(self.path.split('/')[-1])
            Product.Delete(resource_id)
            self.send_response(204)
            self.end_headers()
            self.wfile.write(b'Resource deleted successfully')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'URL not found')
if __name__ == "__main__":
    # Definizione dell'host e della porta del server
    hostName = "localhost"
    serverPort = 8081

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

