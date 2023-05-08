import pytest
import os
import sqlite3
from src.create_database import CreateDatabase
from src.client import Client

class Test_TestClient():

    @pytest.fixture
    def sql_database(self) -> str:
        return "file:cachedb?mode=memory&cache=shared"


    def test_Client_insert_client_returns_id(self, sql_database):

        # arrange
        database = CreateDatabase("file:cachedb?mode=memory&cache=shared")
        #database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)

        # act
        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")

        # assert
        assert id1 == 1


    def test_Client_insert_client_returns_correct_id_for_multiple_inserts(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)

        # act
        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        id2 = client._insert_client("MacGyver Inc2", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        
        # assert
        assert id1 == 1
        assert id2 == 2


    def test_Client_insert_client_returns_unique_exception(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)

        with pytest.raises(sqlite3.IntegrityError):
            # act
            id = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
            id2 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        

    def test_Client_get_client_id_returns_correct_id(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)
        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")

        # act
        id2 = client._get_client_id("MacGyver Inc")
        
        # assert
        assert id1 == id2


    def test_Client_get_client_id_returns_correct_id_for_multiple_inserts(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)
        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        id2 = client._insert_client("MacGyver Inc2", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")

        # act
        id3 = client._get_client_id("MacGyver Inc2")
        
        # assert
        assert id2 == id3
        assert id1 != id3


    def test_Client_add_client_returns_correct_id(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)
       
        # act
        id1 = client.add_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        
        # assert
        assert id1 == 1


    def test_Client_add_client_returns_correct_id_when_record_exists(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)
        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
       
        # act
        id2 = client.add_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        
        # assert
        assert id1 == id2


    def test_Client_get_all_client_returns_correct_results(self, sql_database):

        # arrange
        database = CreateDatabase(sql_database)
        database.create_all_objects()
        conn = database.Connection
        client = Client(conn)

        id1 = client._insert_client("MacGyver Inc", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        id2 = client._insert_client("MacGyver Inc2", "72 Academy Street", "Swindon", "SN4 9QP", "United Kingdom", "+44 7911 843910")
        
        # act
        results = client.get_all_clients()

        # assert
        assert len(results) == 2


