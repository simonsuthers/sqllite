# SQL Lite demo database

[![CI - Build and run tests](https://github.com/simonsuthers/sqllite/actions/workflows/ci.yml/badge.svg)](https://github.com/simonsuthers/sqllite/actions/workflows/ci.yml)

To run the tests, run the following scripts:
```
pytest -s tests/test_create_database.py
pytest -s tests/test_client.py
pytest -s tests/test_product.py
pytest -s tests/test_order.py
pytest -s tests/test_add_data.py
```