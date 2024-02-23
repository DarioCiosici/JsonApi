import DBManager
class Product:

    
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    def get_brand(self):
        return self._brand
    def set_brand(self, brand):
        self._brand = brand
    
    def FetchAll():
        cursore=dbmanager.Create()
        cursore.execute("SELECT * FROM products")
        prodotti = cursor.fetchall()
        cursore.Close()
        return prodotti
    def Find(id):
        cursore=dbmanager.Create()
        cursore.execute("SELECT * FROM products where id=%s", (id,))
        prodotto = cursor.fetchone()
        cursore.Close()
        return prodotto
    def Delete(id):
        cursore=dbmanager.Create()
        cursore.execute("DELETE * FROM products where id=%s", (id))
        cursore.commit()
        cursore.Close()
    def Create(name,price,brand):
        cursore=dbmanager.Create()
        cursore.execute("INSERT INTO products (nome, prezzo, marca) VALUES (%s, %s, %s)", (name, price, brand))
        cursore.commit()
        cursore.Close()
    def Update(name,price,brand,id):
        cursore=dbmanager.Create()
        if(name is None):
            cursore.execute("UPDATE products SET prezzo = %s, marca = %s WHERE id = %s", (price, brand, id))
        if(price is None):
            cursore.execute("UPDATE products SET nome = %s, marca = %s WHERE id = %s", (name, brand, id))
        if(brand is None):
            cursore.execute("UPDATE products SET prezzo = %s WHERE id = %s", (name, price, id))
        else:
            cursore.execute("UPDATE products SET nome = %s, prezzo = %s, marca = %s WHERE id = %s", (name, price, brand, id))
        cursore.commit()
        cursore.Close()

        
