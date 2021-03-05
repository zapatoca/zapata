from datetime import datetime

import pandas as pd


def transform(table, conn) -> None:
    df = pd.read_sql_table("income", conn)
    total_payments = sum([df["Jan"], df["Feb"], df["Mar"]])

    df["Monthly"] = (df["Amount"] / 12).astype(int)
    df["Balance"] = df["Amount"] - total_payments

    currentMonth = datetime.now().month
    df["Alert"] = currentMonth * df["Monthly"] > total_payments

    df.to_sql("income", con=conn, if_exists="replace", index=False)
