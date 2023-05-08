import pytest
import os
import sqlite3
from src.create_database import CreateDatabase
from src.client import Client
from src.product import Product
from src.order import Order

class Test_TestOrder():

    @pytest.fixture
    def sql_database(self) -> str:
        return "file:cachedb?mode=memory&cache=shared"


    def test_Order_add_order_returns_id(self, sql_database):

        # arrange
        database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)
        client = Client(conn)
        
        product_id = product.add_product("Piano", "Keyboard", 4700, "GBP")
        client_id = client.add_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")

        # act
        order = Order(conn)
        order_id = order.add_order("PO0060504-1", client_id, product_id, 3, "Debit", "PO0060504-20210321", "21/03/2021")

        # assert
        assert order_id == 1


    def test_Order_get_all_orders_returns_results(self, sql_database):

        # arrange
        database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)
        client = Client(conn)
        
        product_id = product.add_product("Piano", "Keyboard", 4700, "GBP")
        client_id = client.add_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")

        order = Order(conn)
        order_id = order.add_order("PO0060504-1", client_id, product_id, 3, "Debit", "PO0060504-20210321", "21/03/2021")

        # act
        orders = order.get_all_orders()

        # assert
        assert len(orders) == 1



