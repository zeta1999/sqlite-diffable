import pytest
import sqlite_utils


@pytest.fixture
def one_table_db(tmpdir):
    path = str(tmpdir / "one_table.db")
    db = sqlite_utils.Database(path)
    db["one_table"].insert_all(
        [
            {"id": 1, "name": "Stacey"},
            {"id": 2, "name": "Tilda"},
            {"id": 3, "name": "Bartek"},
        ],
        pk="id",
    )
    return path


@pytest.fixture
def two_tables_db(one_table_db):
    db = sqlite_utils.Database(one_table_db)
    db["second_table"].insert_all([{"id": 1, "name": "Cleo"}], pk="id")
    return one_table_db
