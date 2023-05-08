import sqlite3
import logging
from typing import Optional, Any




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

