import sqlite3
from typing import Optional, Any
import pandas as pd
import logging

from product import Product
from client import Client
from order import Order
from create_database import CreateDatabase


class AddData:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)


    @property
    def Connection(self) -> sqlite3.Connection:
        return self._connection


    def add_orders_from_excel(self, excel_path: str = "src/Orders2023.xlsx"):

        df: pd.DataFrame = pd.read_excel(excel_path)

        for index, row in df.iterrows():
            self._add_order(row)


    def _add_order(self, row: pd.Series) -> None:
        try:
            client = Client(self._connection)  
            client_id = client.add_client(client_name=row["ClientName"], 
                                    delivery_address=row["DeliveryAddress"], 
                                    delivery_city=row["DeliveryCity"], 
                                    delivery_postcode=row["DeliveryPostcode"], 
                                    delivery_country=row["DeliveryCountry"], 
                                    delivery_contact_number=row["DeliveryContactNumber"])

            product = Product(self._connection)  
            product_id = product.add_product(product_name=row["ProductName"],
                                            product_type=row["ProductType"],
                                            unit_price=row["UnitPrice"],
                                            currency=row["Currency"])

            order = Order(self._connection)
            order_id = order.add_order(order_number=row["OrderNumber"],
                                        client_id=client_id,
                                        product_id=product_id,
                                        product_quantity=row["ProductQuantity"],
                                        payment_type=row["PaymentType"],
                                        payment_billing_code=row["PaymentBillingCode"],
                                        payment_date=row["PaymentDate"].strftime('%Y-%m-%d %X')
                                        )


        except Exception as e:
            logging.info(f"The following row has not been added: {row}. {e}")



if __name__ == "__main__":

    database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
    database.create_all_objects()
    conn = database.Connection
    product1 = Product(conn)
    client1 = Client(conn)
    order1 = Order(conn)
    add_data = AddData(conn)

    add = AddData(conn)
    add.add_orders_from_excel("src/Orders2023.xlsx")
    print(client1.get_all_clients())
    print(product1.get_all_products())
    print(order1.get_all_orders())


