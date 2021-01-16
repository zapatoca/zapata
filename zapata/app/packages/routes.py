from datetime import datetime

import pandas as pd
from flask import render_template


def configure_routes(app, db):
    def render(df) -> str:
        df = df[["Total", "Monthly", "January", "Balance", "Alert"]]

        props = [("border", "2px solid black")]

        styles = [
            {"selector": "table, th, td", "props": props},
        ]

        return (
            df.style.hide_columns(["Alert"])
            .set_properties(
                **{
                    "background-color": "white",
                    "color": "black",
                }
            )
            .apply(color_negative_red, axis=1)
            .format("₪ {}")
            .set_table_styles(styles)
            .render()
        )

    def color_negative_red(row) -> list[str]:
        return [
            "background-color: red"
            if row["Alert"] and index == "January"
            else "background-color: white"
            for index, val in row.items()
        ]

    @app.route("/", methods=["GET"])
    def index() -> str:
        with db.engine.begin() as connection:
            df = pd.read_sql_table("income", connection)
            df["Monthly"] = (df["Total"] / 12).astype(int)
            df["Balance"] = df["Total"] - sum([df["January"]])

            currentMonth = datetime.now().month
            df["Alert"] = currentMonth * df["Monthly"] > sum([df["January"]])

            df.index += 1

            df.to_sql(
                "income", con=connection, if_exists="replace", index=False
            )

        return render_template("index.html", table=render(df))
