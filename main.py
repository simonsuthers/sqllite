from src.add_data import AddData
from src.client import Client
from src.product import Product
from src.order import Order
from src.create_database import CreateDatabase


if __name__ == "__main__":
    database = CreateDatabase("mydb.db")
    database.create_all_objects()
    conn = database.Connection

    add_data = AddData(conn)
    add_data.add_orders_from_excel("src/Orders2023.xlsx")

    # see results
    product = Product(conn)
    client = Client(conn)
    order = Order(conn)

    print(client.get_all_clients())
    print(product.get_all_products())
    print(order.get_all_orders())