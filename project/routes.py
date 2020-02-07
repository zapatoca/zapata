#!/usr/bin/env python3

from flask import flash, redirect, render_template, request, url_for
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email


def configure_routes(app, db):

    class SubscribeForm(Form):
        email = StringField('Email', validators=[DataRequired(), Email()])

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        form = SubscribeForm(request.form)

        if request.method == 'POST' and form.validate():
            app.logger.info('New subscriber %s', form.email.data)

            add_subscriber(app, db, form.email.data)
            return(redirect(url_for('home')))

        return render_template('index.html', form=form)


def add_subscriber(app, db, email):
    try:
        cur = db.connection.cursor()
        cur.execute(
            "INSERT INTO subscribers (email) VALUES ('{0}')"
            .format(email)
        )
        db.connection.commit()
        cur.close()
        flash('You are now subscribed', 'success')

    except Exception as e:
        app.logger.info(e)
