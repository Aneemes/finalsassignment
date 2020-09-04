import mysql.connector

class DbConnection:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost", user="root", password="1990", database="python2")
        self.cursor=self.con.cursor()


    def insert(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def update(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def delete(self,query,values):
        self.cursor.execute(query,values)
        self.con.commit()

    def select(self,query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.con.commit()


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python2',
                                         user='root',
                                         password='1990')
    mySql_insert_query = """INSERT INTO customertier (customerid, customername, tier) 
                           VALUES 
                           ('17','Ram Prasad','gold') """





    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Customer tier table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Customer tier table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")