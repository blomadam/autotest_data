import pytest
import sys
import psycopg2
import configparser

config = configparser.ConfigParser()


@pytest.fixture(scope="session")
def db_conn():
    connection_string = config["passwords"]["aact_db_connection_string"]
    with psycopg2.connect(connection_string) as conn:
        yield conn


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
