import pytest
import subprocess
from random import choice
import time
import string

from sqlalchemy import text

from app.database import DatabaseProvider


# @pytest.fixture(scope="session", autouse=True)
# def docker_compose():
#     # Start Docker Compose
#     subprocess.run(["docker-compose", "up", "-d"], check=True)

#     # Ensure the service is healthy
#     max_retries = 10
#     for i in range(max_retries):
#         result = subprocess.run(
#             ["docker", "exec", "postgres", "pg_isready", "-U", "test_user"],
#             capture_output=True,
#         )
#         if result.returncode == 0:
#             break
#         time.sleep(5)
#     else:
#         subprocess.run(["docker-compose", "down"], check=True)
#         raise RuntimeError

#     yield
#     # Tear down Docker Compose
#     subprocess.run(["docker-compose", "down"], check=True)


@pytest.fixture()
def schema_name():
    yield "".join(choice(string.ascii_lowercase) for i in range(10))


@pytest.fixture(scope="module")
def provider():
    # Use the Docker container connection details
    provider = DatabaseProvider(
        database="test_db",
        user="test_user",
        password="test_pass",
        host="localhost",
        port=5432,
    )
    yield provider
    # Cleanup after tests
    provider.engine.dispose()


@pytest.mark.integration
def test_create_schema(provider, schema_name):
    try:
        provider.create_schema(schema_name)

        # Ensure the schema is present in the database
        with provider.engine.connect() as conn:
            result = conn.execute(
                text(f"""
                    SELECT schema_name
                    FROM information_schema.schemata
                    WHERE schema_name = '{schema_name}'
                """)
            ).fetchone()
            assert result
    finally:
        # Ensure we drop the schema when we are done
        with provider.engine.connect() as conn:
            conn.execute(
                text(f"""
                    DROP SCHEMA IF EXISTS {schema_name}
                """)
            )
            conn.commit()
