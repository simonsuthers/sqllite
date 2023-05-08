import sqlite3
import logging
from typing import Optional, Any

from src.create_database import CreateDatabase
from src.product import Product
from src.client import Client


class Order:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)


    @property
    def Connection(self) -> sqlite3.Connection:
        return self._connection


    def add_order(self, 
                    order_number: str, 
                    client_id: int, 
                    product_id: int, 
                    product_quantity: int,
                    payment_type: str,
                    payment_billing_code: str,
                    payment_date: str) -> int:

        sql = ''' INSERT INTO Orders
                (OrderNumber, ClientId, ProductId, ProductQuantity, PaymentType, PaymentBillingCode, PaymentDate)
                VALUES(?,?,?,?,?,?,?) '''
        cur = self._connection.cursor()
        cur.execute(sql, (order_number, client_id, product_id, product_quantity, payment_type, payment_billing_code, payment_date))
        self._connection.commit()

        return cur.lastrowid


    def get_all_orders(self) -> list[Any]:
        sql = ''' SELECT * FROM Orders '''
        cur = self._connection.cursor()
        result = cur.execute(sql).fetchall()
        self._connection.commit()

        return result

        
if __name__ == "__main__":
    database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
    database.create_all_objects()
    conn = database.Connection
    product = Product(conn)
    client = Client(conn)
    order = Order(conn)
    #id = product.get_product_id("Piano")
    product_id = product.add_product("Piano", "Keyboard", 4700, "GBP")
    print(product_id)
    client_id = client.add_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
    print(client_id)
    order_id = order.add_order("PO0060504-1", client_id, product_id, 3, "Debit", "PO0060504-20210321", "21/03/2021")
    print(order_id)
    print(order.get_all_orders())