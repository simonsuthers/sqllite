import pytest
import os
import sqlite3
from src.create_database import CreateDatabase
from src.product import Product

class Test_TestProduct():

    @pytest.fixture
    def sql_database(self) -> str:
        return "file:cachedb?mode=memory&cache=shared"


    def test_Product_insert_product_returns_id(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)

        # act
        id1 = product._insert_product("Piano1", "Keyboard", 4700, "GBP")

        # assert
        assert id1 == 1


    def test_Product_insert_product_returns_correct_id_for_multiple_inserts(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)

        # act
        id1 = product._insert_product("Piano", "Keyboard", 4700, "GBP")
        id2 = product._insert_product("Piano1", "Keyboard", 4700, "GBP")
        
        # assert
        assert id1 == 1
        assert id2 == 2


    def test_Product_insert_product_returns_unique_exception(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)

        with pytest.raises(sqlite3.IntegrityError):
            # act
            id1 = product._insert_product("Piano", "Keyboard", 4700, "GBP")
            id2 = product._insert_product("Piano", "Keyboard", 4700, "GBP")
        

    def test_Product_get_product_id_returns_correct_id(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)
        id1 = product._insert_product("Piano", "Keyboard", 4700, "GBP")

        # act
        id2 = product._get_product_id("Piano")
        
        # assert
        assert id1 == id2


    def test_Product_add_product_returns_correct_id(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)
       
        # act
        id1 = product.add_product("Piano", "Keyboard", 4700, "GBP")
        
        # assert
        assert id1 == 1


    def test_Product_add_product_returns_correct_id_when_record_exists(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)
        id1 = product._insert_product("Piano", "Keyboard", 4700, "GBP")

        # act
        id2 = product.add_product("Piano", "Keyboard", 4700, "GBP")
        
        # assert
        assert id1 == id2


    def test_Product_get_all_products_returns_correct_results(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        product = Product(conn)

        id1 = product._insert_product("Piano", "Keyboard", 4700, "GBP")
        id1 = product._insert_product("Piano1", "Keyboard", 4700, "GBP")
        
        # act
        results = product.get_all_products()

        # assert
        assert len(results) == 2


