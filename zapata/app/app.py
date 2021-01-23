#!/usr/bin/env python3
from datetime import datetime

import pandas as pd
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField

app = Flask(
    __name__, template_folder="/app/templates", static_folder="/app/static"
)
app.secret_key = "secret123"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://zapata:zapata@db:5432/zapata"
db = SQLAlchemy(app)


class Incident(db.Model):
    __tablename__ = "incidents"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


class Fee(db.Model):
    __tablename__ = "fees"
    id = db.Column(db.Integer, primary_key=True)
    yearly = db.Column(db.Integer)


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
def _index() -> str:
    with db.engine.begin() as conn:
        df = pd.read_sql_table("income", conn)
        df["Monthly"] = (df["Total"] / 12).astype(int)
        df["Balance"] = df["Total"] - sum([df["January"]])

        currentMonth = datetime.now().month
        df["Alert"] = currentMonth * df["Monthly"] > sum([df["January"]])

        df.index += 1

        df.to_sql("income", con=conn, if_exists="replace", index=False)

    return render_template("index.html", table=render(df))


class newIncident(Form):
    description = StringField("Description")


@app.route("/incident", methods=["GET", "POST"])
def _incident() -> str:
    form = newIncident(request.form)

    if request.method == "POST" and form.validate():
        try:
            db.session.add(Incident(description=form.description.data))
            db.session.commit()
            flash("Incident was created", "success")
        except Exception as e:
            print(f"{e}", flush=True)
            flash(f"{e}", category="warning")
        return redirect(url_for("_index"))
    return render_template("incident.html", form=form)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0")
