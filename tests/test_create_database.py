import pytest
from src.create_database import CreateDatabase

class Test_TestCreateDatabase():

    @pytest.fixture
    def sql_database(self) -> str:
        return "'file:cachedb?mode=memory&cache=shared'"


    def test_CreateDatabase_creates_product_table(self, sql_database):

        # arrange
        db = CreateDatabase(sql_database)
        db.create_products_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Products' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_product_table_with_correct_columns(self, sql_database):

        # arrange
        db = CreateDatabase(sql_database)
        db.create_products_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' pragma table_info(Products) ''').fetchall()

        # assert
        assert len(result) == 5
        assert result[0][1] == "ProductId"
        assert result[1][1] == "ProductName"
        assert result[2][1] == "ProductType"
        assert result[3][1] == "UnitPrice"
        assert result[4][1] == "Currency"


    def test_CreateDatabase_creates_clients_table(self, sql_database):

        # arrange
        db = CreateDatabase(sql_database)
        db.create_clients_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Clients' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_orders_table(self, sql_database):

        # arrange
        db = CreateDatabase(sql_database)
        db.create_orders_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Orders' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_all_tables(self, sql_database):

        # arrange
        db = CreateDatabase(sql_database)
        db.create_all_objects()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name IN ('Orders', 'Clients', 'Products') ''').fetchone()

        # assert
        assert result[0] == 3