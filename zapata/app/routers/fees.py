import pandas as pd
from flask import Blueprint, flash, redirect, render_template, request, url_for
from wtforms import Form, IntegerField, SelectField, StringField

from database import db
from models.fee import Fee
from routers.utils import render

fees_router = Blueprint("fees", __name__)


@fees_router.route("/fees", methods=["GET"])
def _fees() -> str:
    with db.engine.begin() as conn:
        df = pd.read_sql_table("fees", conn)
    return render_template(
        "fees.html",
        projects=render(df, "fees"),
    )


@fees_router.route("/fees/new", methods=["GET", "POST"])
def _new_fee() -> str:
    class newFee(Form):
        Apartment = IntegerField("Apartment")
        Fee_type = SelectField(
            "Fee_type", choices=[("1", "Ongoing"), ("2", "Project")]
        )
        Amount = IntegerField("Amount")
        project = StringField("project")

    form = newFee(request.form)

    if request.method == "POST" and form.validate():
        try:
            # TBD transform form.project.data which is a string into the
            # project id
            db.session.add(
                Fee(
                    Apartment=form.Apartment.data,
                    Fee_type=form.Fee_type.data,
                    Amount=form.amount.data,
                    project=1,
                )
            )
            db.session.commit()
            flash("Fee was created", "success")
        except Exception as e:
            print(f"{e}", flush=True)
            flash(f"{e}", category="warning")
        return redirect(url_for("fees_router._fees"))

    return render_template("new_fee.html", form=form)
