#!/usr/bin/env python3

from flask import redirect, render_template, request, url_for
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email


def configure_routes(app):

    class SubscribeForm(Form):
        email = StringField('Email', validators=[DataRequired(), Email()])

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        form = SubscribeForm(request.form)

        if request.method == 'POST' and form.validate():
            # email = form.email.data
            return(redirect(url_for('home')))

        return render_template('index.html', form=form)
