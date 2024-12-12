from sqlalchemy import create_engine, text


class DatabaseProvider:
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.connection_string = (
            f"postgresql://{user}:{password}@{host}:{port}/{database}"
        )
        self.engine = self.connect()

    def connect(self):
        return create_engine(self.connection_string)

    def create_schema(self, schema_name: str):
        with self.engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA {schema_name};"))
            conn.commit()
