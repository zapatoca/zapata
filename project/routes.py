#!/usr/bin/env python3

from flask import flash, redirect, render_template, request, url_for
from mailchimp3 import MailChimp
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email

from project.secrets import get_secret


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
        client = MailChimp(
            mc_api=get_secret('mailchimp/apikey'),
            mc_user=get_secret('mailchimp/username')
        )
        client.lists.members.create(
            get_secret('mailchimp/listid'),
            {
                'email_address': '{email}'.format(email=email),
                'status': 'subscribed'
            }
        )
        flash('You are now subscribed', 'success')

    except Exception as e:
        app.logger.info(e)
