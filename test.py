import requests,json
import hashlib
import Product
json_data = {
    'nome':'ciao',
    'prezzo': 120,
    'marca': 'ciao'
}

response = requests.get('http://localhost:8081/products')
print(response.text) 
print(response)
response=requests.post('http://localhost:8081/products',json.dumps(json_data).encode('utf-8'))
print(response.text) 
print(response)
response=requests.delete('http://localhost:8081/products/2')
print(response.text) 
print(response)
response=requests.patch('http://localhost:8081/products/4',json.dumps(json_data).encode('utf-8'))
print(response.text) 
# Stampa il testo della risposta
print(response)  # Stampa il contenuto della risposta come JSON
