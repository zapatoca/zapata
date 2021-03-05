import pandas as pd
from flask import Blueprint, flash, redirect, render_template, request, url_for
from wtforms import Form, IntegerField, StringField

from database import db
from models_ import Building, Incident, Project
from routers.utils import render

router = Blueprint("router", __name__)


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
        return redirect(url_for("index._index"))
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
        return redirect(url_for("index._index"))
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
