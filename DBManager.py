import _mysql_connector
class dbmanager:
    def Create():
        con=_mysql_connector.MySQL()
        con.connect(user="ciosici_dario",password="Scythians.lutes.gregariousnesss.",host="192.168.2.200:8081",database="ciosici_dario_ecommerce5E" )
        return con.cursor()
    def Close():
        cursor.close()
        con.close()
        


