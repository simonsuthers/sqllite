import pytest

from src.add_data import AddData
from src.client import Client
from src.product import Product
from src.order import Order
from src.create_database import CreateDatabase


class Test_TestAddData():

    @pytest.fixture
    def sql_database(self) -> str:
        return "file:cachedb?mode=memory&cache=shared"


    def test_AddData_adds_orders_from_excel(self, sql_database):

        # arrange
        database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
        database.create_all_objects()
        conn = database.Connection

        product1 = Product(conn)
        client1 = Client(conn)
        order1 = Order(conn)

        # act
        add_data = AddData(conn)
        add_data.add_orders_from_excel("src/Orders2023.xlsx")

        # assert
        assert len(client1.get_all_clients()) == 11
        assert len(product1.get_all_products()) == 16
        assert len(order1.get_all_orders()) == 26

