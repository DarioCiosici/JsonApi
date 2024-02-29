
import mysql.connector 
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
        try:
            con=mysql.connector.connect(host="localhost", user="root",password="",port="3306",database="ecommerce5e")
            cursore=con.cursor()
            cursore.execute("SELECT * FROM products")

            prodotti = cursore.fetchall()
            return prodotti
        except Exception as e:
            print(f"Errore durante l'elaborazione della query: {e}")           
    def Find(id):
        con=mysql.connector.connect(host="localhost", user="root",password="",port="3306",database="ecommerce5e")
        cursore=con.cursor()
        cursore.execute("SELECT * FROM products where id=%s", (id,))
        prodotto = cursore.fetchone()
        cursore.close()
        return prodotto
    def Delete(id):
        con=mysql.connector.connect(host="localhost", user="root",password="",port="3306",database="ecommerce5e")
        cursore=con.cursor()
        cursore.execute("DELETE FROM products where id = %s", (id,))
        con.commit()
        cursore.close()
        con.close()
    def Create(name,price,brand):
        con=mysql.connector.connect(host="localhost", user="root",password="",port="3306",database="ecommerce5e")
        cursore=con.cursor()
        cursore.execute("INSERT INTO products (nome, prezzo, marca) VALUES (%s, %s, %s)", (name, price, brand,))
        con.commit()
        cursore.close()
        con.close()
    def Update(name,price,brand,id):
        con=mysql.connector.connect(host="localhost", user="root",password="",port="3306",database="ecommerce5e")
        cursore=con.cursor()
        if(name is None):
            cursore.execute("UPDATE products SET prezzo = %s, marca = %s WHERE id = %s", (price, brand, id,))
        elif(price is None):
            cursore.execute("UPDATE products SET nome = %s, marca = %s WHERE id = %s", (name, brand, id,))
        elif(brand is None):
            cursore.execute("UPDATE products SET prezzo = %s WHERE id = %s", (name, price, id,))
        elif(name is None and price is None): 
            cursore.execute("UPDATE products SET marca = %s WHERE id = %s", (brand, id,))
        elif(price is None and brand is None) :
            cursore.execute("UPDATE products SET nome = %s WHERE id = %s", (name, id,))
        elif(name is None and brand is None):
            cursore.execute("UPDATE products SET prezzo = %s WHERE id = %s", (price, id,))
        else:
            cursore.execute("UPDATE products SET nome = %s, prezzo = %s, marca = %s WHERE id = %s", (name, price, brand, id,))
        con.commit()
        
        cursore.close()

        