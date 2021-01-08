#!/usr/bin/env python3

from datetime import datetime

import pandas as pd
from flask import flash, redirect, render_template, request, url_for
from mailchimp3 import MailChimp
from passlib.hash import sha256_crypt
from wtforms import Form, PasswordField, StringField, validators
from wtforms.validators import DataRequired, Email

from modules.secrets import get_secret


class newAccountForm(Form):
    name = StringField(
        "Name",
        [
            validators.Regexp(
                r"[A-Za-z\s]+",
                message="Name may only contain alphanumeric \
                          characters and spaces",
            ),
            validators.Length(min=1, max=50),
        ],
    )
    email = StringField(
        "Email", [validators.Email(), validators.Length(min=6, max=50)]
    )
    username = StringField(
        "Username",
        [
            validators.Regexp(
                r"[A-Za-z0-9_]+",
                message="Name may only contain alphanumeric \
                          characters",
            ),
            validators.Length(min=4, max=25),
        ],
    )
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="Passwords do not match"),
        ],
    )
    confirm = PasswordField("Confirm Password")


def configure_routes(app, db):
    class SubscribeForm(Form):
        email = StringField("Email", validators=[DataRequired(), Email()])

    @app.route("/", methods=["GET", "POST"])
    @app.route("/home", methods=["GET", "POST"])
    def home():
        form = SubscribeForm(request.form)

        if request.method == "POST" and form.validate():
            app.logger.info("New subscriber %s", form.email.data)

            add_subscriber(app, db, form.email.data)
            return redirect(url_for("home"))

        return render_template("index.html", form=form)

    @app.route("/new_account", methods=["GET", "POST"])
    def new_account():
        form = newAccountForm(request.form)

        if request.method == "POST" and form.validate():
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))

            try:
                # Create cursor
                cur = db.connection.cursor()

                cur.execute(
                    "INSERT INTO users(name, email, username, password) \
                    VALUES(%s, %s, %s, %s)",
                    (name, email, username, password),
                )

                # Commit to DB
                db.connection.commit()

                # Close connection
                cur.close()

                flash("Account was created", "success")

            except Exception as e:
                flash("{}".format(e.args[1]), category="warning")

            return redirect(url_for("home"))

        return render_template("new_account.html", form=form)

    def add_subscriber(app, db, email):
        try:
            cur = db.connection.cursor()
            cur.execute(
                "INSERT INTO subscribers (email) VALUES ('{0}')".format(email)
            )
            db.connection.commit()
            cur.close()
            client = MailChimp(
                mc_api=get_secret("vault-server", "mailchimp/apikey"),
                mc_user=get_secret("vault-server", "mailchimp/username"),
            )
            client.lists.members.create(
                get_secret("vault-server", "mailchimp/listid"),
                {
                    "email_address": "{email}".format(email=email),
                    "status": "subscribed",
                },
            )
            flash("You are now subscribed", "success")

        except Exception as e:
            app.logger.info(e)

    def render(df) -> str:
        df = df[["Total", "Monthly", "January", "Balance"]]

        props = [("border", "2px solid black")]

        styles = [
            {"selector": "table, th, td", "props": props},
        ]

        return (
            df.style.set_properties(
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
        currentMonth = datetime.now().month
        return [
            "background-color: red"
            if currentMonth * row["Monthly"] > sum([row["January"]])
            and index == "January"
            else "background-color: white"
            for index, val in row.items()
        ]

    @app.route("/building", methods=["GET", "POST"])
    def building() -> str:
        total = [
            5400,
            5400,
            3780,
            3780,
            3780,
            3780,
            3780,
            4500,
            4500,
            4860,
            5400,
            5400,
            4860,
            5400,
            4860,
            5400,
            4860,
            7200,
            7200,
        ]
        january = [
            1350,
            450,
            3780,
            315,
            0,
            157,
            0,
            0,
            0,
            1215,
            450,
            0,
            810,
            5400,
            0,
            1350,
            405,
            0,
            600,
        ]
        df = pd.DataFrame(data={"Total": total, "January": january})
        df["Monthly"] = (df["Total"] / 12).astype(int)
        df["Balance"] = df["Total"] - sum([df["January"]])
        df.index += 1

        return render_template("building.html", table=render(df))
