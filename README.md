# SQL Lite demo database

[![CI - Build and run tests](https://github.com/simonsuthers/sqllite/actions/workflows/ci.yml/badge.svg)](https://github.com/simonsuthers/sqllite/actions/workflows/ci.yml)

## Entry point
To run the script, execute the file in the root folder:
```
main.py
```

This has been tested with Python 3.9

The *main.py* file does the following:
* Builds database using create_database.py
* Adds data to database using add_data.py
* Displays data added to the database

The class *AddData* in add_data.py has two main methods:
* add_orders_from_excel
    * Adds data from a given xlsx workbook
* add_orders_from_csv
    * Adds data from a given csv file

## Tests

To run the tests, run the following scripts:
```
pytest -s tests/test_create_database.py
pytest -s tests/test_client.py
pytest -s tests/test_product.py
pytest -s tests/test_order.py
pytest -s tests/test_add_data.py
```