import sqlite3
import logging
from typing import Optional

from src.create_database import CreateDatabase


class Product:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)


    @property
    def Connection(self) -> sqlite3.Connection:
        return self._connection


    def add_product(self, product_name: str, product_type: str, unit_price: float, currency: str) -> int:
        id = self._get_product_id(product_name)

        if id is not None: 
            return id
        else:
            return self._insert_product(product_name, product_type, unit_price, currency)


    def _insert_product(self, product_name: str, product_type: str, unit_price: float, currency: str) -> int:
        sql = ''' INSERT INTO Products
                (ProductName, ProductType, UnitPrice, Currency)
                VALUES(?,?,?,?) '''
        cur = self._connection.cursor()
        cur.execute(sql, (product_name, product_type, unit_price, currency))
        self._connection.commit()

        return cur.lastrowid


    def _get_product_id(self, product_name: str) -> Optional[int]:
        sql = ''' SELECT ProductId FROM Products WHERE ProductName = ? '''
        cur = self._connection.cursor()
        result = cur.execute(sql, (product_name, )).fetchone()
        self._connection.commit()

        if result is not None:
            return result[0]

        return None


    def get_all_products(self):
        sql = ''' SELECT * FROM Products '''
        cur = self._connection.cursor()
        result = cur.execute(sql).fetchall()
        self._connection.commit()

        return result

        
if __name__ == "__main__":
    #database = CreateDatabase("temp.db")
    database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
    database.create_all_objects()
    conn = database.Connection
    product = Product(conn)
    #id = product.get_product_id("Piano")
    id = product.add_product("Piano1", "Keyboard", 4700, "GBP")
    print(id)
    id1 = product.add_product("Piano1", "Keyboard", 4700, "GBP")
    print(id1)