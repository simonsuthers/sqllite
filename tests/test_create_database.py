import pytest
from src.create_database import CreateDatabase

class Test_TestCreateDatabase():

    def test_CreateDatabase_creates_tables(self):

        # arrange
        db = CreateDatabase()
        db.create_products_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Products' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_clients_table(self):

        # arrange
        db = CreateDatabase()
        db.create_clients_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Clients' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_orders_table(self):

        # arrange
        db = CreateDatabase()
        db.create_orders_table()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Orders' ''').fetchone()

        # assert
        assert result[0] == 1


    def test_CreateDatabase_creates_all_tables(self):

        # arrange
        db = CreateDatabase()
        db.create_all_objects()
        c = db.connection.cursor()

        # act
        result = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name IN ('Orders', 'Clients', 'Products') ''').fetchone()

        # assert
        assert result[0] == 3