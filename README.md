# api_reader
This project is a simple Python package that interacts with a PostgreSQL database using SQLAlchemy.

## Installation
To use this package, ensure you have Python and PostgreSQL installed. You will also need to install the required dependencies. You can do this using pip:

```
pip install sqlalchemy psycopg2
```

## Configuration
Before running the package, update the `DATABASE_URL` in `db_class.py` with your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://your_user:your_password@localhost/my_database"
```

## Usage
To execute the database operations defined in this package, run the `db_class.py` file:

```
python db_class.py
```

This will connect to the database, execute a SELECT query on the `users` table, and print the results.

## License
This project is licensed under the MIT License.