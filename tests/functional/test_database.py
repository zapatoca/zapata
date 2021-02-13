import pandas as pd
from sqlalchemy import create_engine


def test_rows_number(init_db):
    SQLALCHEMY_DATABASE_URL = (
        "postgresql://zapata:zapata@localhost:5432/zapata"
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    with engine.begin() as conn:
        df = pd.read_sql_table("income", conn)
        assert len(df) == 19
