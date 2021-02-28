from datetime import datetime

import pandas as pd
from flask import Blueprint, flash, redirect, render_template, request, url_for
from wtforms import Form, IntegerField, StringField

from database import db
from models_ import Building, Incident, Project
from routers.utils import render

router = Blueprint("router", __name__)


@router.route("/", methods=["GET"])
def _index() -> str:
    with db.engine.begin() as conn:
        df = pd.read_sql_table("income", conn)
        df["Monthly"] = (df["Amount"] / 12).astype(int)
        df["Balance"] = df["Amount"] - sum([df["Jan"], df["Feb"], df["Mar"]])

        currentMonth = datetime.now().month
        df["Alert"] = currentMonth * df["Monthly"] > sum(
            [df["Jan"], df["Feb"], df["Mar"]]
        )

        df.to_sql("income", con=conn, if_exists="replace", index=False)

        df = pd.read_sql_table("fees", conn)
        df["Balance"] = df["Amount"] - sum([df["Jan"], df["Feb"], df["Mar"]])

        currentMonth = datetime.now().month
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


@router.route("/incident", methods=["GET", "POST"])
def _incident() -> str:
    class newIncident(Form):
        description = StringField("Description")

    form = newIncident(request.form)

    if request.method == "POST" and form.validate():
        try:
            db.session.add(Incident(description=form.description.data))
            db.session.commit()
            flash("Incident was created", "success")
        except Exception as e:
            print(f"{e}", flush=True)
            flash(f"{e}", category="warning")
        return redirect(url_for("router._index"))
    return render_template("incident.html", form=form)


@router.route("/building", methods=["GET", "POST"])
def _building() -> str:
    class newBuilding(Form):
        address = StringField("Address")
        flats = IntegerField("Number of Flats")

    form = newBuilding(request.form)

    if request.method == "POST" and form.validate():
        try:
            db.session.add(
                Building(address=form.address.data, flats=form.flats.data)
            )
            db.session.commit()
            flash("Building was created", "success")
        except Exception as e:
            print(f"{e}", flush=True)
            flash(f"{e}", category="warning")
        return redirect(url_for("router._index"))
    return render_template("building.html", form=form)


@router.route("/projects", methods=["GET"])
def _projects() -> str:
    with db.engine.begin() as conn:
        df = pd.read_sql_table("projects", conn)
    return render_template(
        "projects.html",
        projects=render(df, "projects"),
    )


@router.route("/projects/new", methods=["GET", "POST"])
def _new_project() -> str:
    class newProject(Form):
        summary = StringField("Summary")
        budget = IntegerField("Budget")

    form = newProject(request.form)

    if request.method == "POST" and form.validate():
        try:
            db.session.add(
                Project(summary=form.summary.data, budget=form.budget.data)
            )
            db.session.commit()
            flash("Project was created", "success")
        except Exception as e:
            print(f"{e}", flush=True)
            flash(f"{e}", category="warning")
        return redirect(url_for("router._projects"))

    return render_template("new_project.html", form=form)
