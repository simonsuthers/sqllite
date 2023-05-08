import sqlite3
import logging
from typing import Optional, Any


class Client:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)


    @property
    def Connection(self) -> sqlite3.Connection:
        return self._connection


    def add_client(self,                     
                client_name: str, 
                delivery_address: str, 
                delivery_city: str, 
                delivery_postcode: str, 
                delivery_country: str,
                delivery_contact_number: str) -> int:

        id = self._get_client_id(client_name)

        if id is not None: 
            return id
        else:
            return self._insert_client(client_name, delivery_address, delivery_city, delivery_postcode, delivery_country, delivery_contact_number)


    def _insert_client(self, 
                    client_name: str, 
                    delivery_address: str, 
                    delivery_city: str, 
                    delivery_postcode: str, 
                    delivery_country: str,
                    delivery_contact_number: str) -> int:

        delivery_country = delivery_country.title()
        delivery_city = delivery_city.title()

        sql = ''' INSERT INTO Clients
                (ClientName, DeliveryAddress, DeliveryCity, DeliveryPostcode, DeliveryCountry, DeliveryContactNumber)
                VALUES(?,?,?,?,?,?) '''
        cur = self._connection.cursor()
        cur.execute(sql, (client_name, delivery_address, delivery_city, delivery_postcode, delivery_country, delivery_contact_number))
        self._connection.commit()

        return cur.lastrowid


    def _get_client_id(self, client_name: str) -> Optional[int]:
        sql = ''' SELECT ClientId FROM Clients WHERE ClientName = ? '''
        cur = self._connection.cursor()
        result = cur.execute(sql, (client_name, )).fetchone()
        self._connection.commit()

        if result is not None:
            return result[0]

        return None

    
    def get_all_clients(self) -> list[Any]:
        sql = ''' SELECT * FROM Clients '''
        cur = self._connection.cursor()
        result = cur.execute(sql).fetchall()
        self._connection.commit()

        return result

        