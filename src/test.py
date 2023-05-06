import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import insert, select
import pandas as pd
from mapper import Product, Client
import logging


class AddData:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///mydb.db', echo = True)

        root = logging.getLogger()
        root.setLevel(logging.DEBUG)


    def add_products(self, excel_path: str = "src/Orders2023.xlsx"):

        df: pd.DataFrame = pd.read_excel(excel_path)

        for index, row in df.iterrows():
            self._add_product(row)


    def _add_product(self, row: pd.Series) -> None:
        try:
            stmt = insert(Product).values(ProductName=row["ProductName"], 
                                        ProductType=row["ProductType"], 
                                        #UnitPrice=row["UnitPrice"], 
                                        Currency=row["Currency"])

            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()

        except Exception as e:
            logging.info(f"The following row has not been added: {row}. {e}")






# conn = engine.connect()
# conn.execute(insert(Product), [
#    {'ProductName':'Rajiv', 'ProductType' : 'Khanna', 'UnitPrice' : 10, 'Currency' : 'Khanna'},
#    {'ProductName':'Komal','ProductType' : 'Bhandari', 'UnitPrice' : 11, 'Currency' : 'Khanna'},
#    {'ProductName':'Abdul','ProductType' : 'Sattar', 'UnitPrice' : 12, 'Currency' : 'Khanna'},
#    {'ProductName':'Priya','ProductType' : 'Rajhans', 'UnitPrice' : 13},
# ])
# conn.commit()

if __name__ == "__main__":

    add = AddData()
    add.add_products()

    engine = create_engine('sqlite:///mydb.db', echo = True)
    conn = engine.connect()

    p = select(Product)
    result = conn.execute(p)

    for row in result:
        print(row)


