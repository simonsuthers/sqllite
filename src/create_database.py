import sqlite3


class CreateDatabase:

    def __init__(self, dbname: str='mydb.db'):    
        try:
            self._dbname = dbname
            self._connection = sqlite3.connect(dbname)
        except:
            print('Error')


    @property 
    def dbname(self):
        return self._dbname

    @property 
    def Connection(self) -> sqlite3.Connection:
        return self._connection


    def create_all_objects(self):
        self.create_clients_table()
        self.create_products_table()
        self.create_orders_table()


    def create_orders_table(self):
        self._connection.execute('''DROP TABLE IF EXISTS Orders;''')

        self._connection.execute('''
                                CREATE TABLE Orders
                                (
                                [OrderId] INTEGER PRIMARY KEY AUTOINCREMENT, 
                                [OrderNumber] INTEGER NOT NULL, 
                                [ClientId] INTEGER NOT NULL,
                                [ProductId] INTEGER NOT NULL,
                                [ProductQuantity] INTEGER NOT NULL,
                                [PaymentType] TEXT NOT NULL,
                                [PaymentBillingCode] TEXT NOT NULL,
                                [PaymentDate] TEXT NOT NULL,
                                UNIQUE([OrderNumber]),
                                UNIQUE([ClientId], [ProductId], [PaymentDate]),
                                FOREIGN KEY(ClientId) REFERENCES Clients(ClientId),
                                FOREIGN KEY(ProductId) REFERENCES Products(ProductId)
                                )
                                ''')

        self._connection.commit()


    def create_products_table(self):

        self._connection.execute('''DROP TABLE IF EXISTS Products;''')
        
        self._connection.execute('''
                CREATE TABLE Products
                (
                [ProductId] INTEGER PRIMARY KEY AUTOINCREMENT,
                [ProductName] TEXT NOT NULL,
                [ProductType] TEXT NOT NULL,
                [UnitPrice] REAL NOT NULL,
                [Currency] TEXT NOT NULL,
                UNIQUE([ProductName])
                );
                ''')

        self._connection.commit()


    def create_clients_table(self):
        self._connection.execute('''DROP TABLE IF EXISTS Clients;''')

        self._connection.execute('''
                            CREATE TABLE Clients
                            (
                            [ClientId] INTEGER PRIMARY KEY, 
                            [ClientName] TEXT NOT NULL,
                            [DeliveryAddress] TEXT NOT NULL,
                            [DeliveryCity] TEXT NOT NULL,
                            [DeliveryPostcode] TEXT NOT NULL,
                            [DeliveryCountry] TEXT NOT NULL,
                            [DeliveryContactNumber] TEXT NULL,
                            UNIQUE([ClientName])
                            )
                            ''')

        self._connection.commit()


                     
