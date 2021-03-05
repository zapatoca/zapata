import pandas as pd
from flask import Blueprint, render_template

import transform
from database import db
from routers.utils import render

index_router = Blueprint("index", __name__)


@index_router.route("/", methods=["GET"])
def _index() -> str:
    with db.engine.begin() as conn:
        transform.transform("income", conn)

        df = pd.read_sql_table("fees", conn)
        total_payments = sum([df["Jan"], df["Feb"], df["Mar"]])
        df["Balance"] = df["Amount"] - total_payments
        df["Alert"] = df["Balance"] != 0
        df.to_sql("fees", con=conn, if_exists="replace", index=False)

    with db.engine.begin() as conn:
        df1 = pd.read_sql_table("income", conn)
        df2 = pd.read_sql_table("incidents", conn)
        df3 = pd.read_sql_table("buildings", conn)
        df4 = pd.read_sql_table("fees", conn)

    return render_template(
        "index.html",
        income=render(df1, "income"),
        incidents=render(df2, "incidents"),
        buildings=render(df3, "buildings"),
        projects=render(df4, "fees"),
    )
