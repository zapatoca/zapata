#!/usr/bin/env python3

from flask import render_template


def configure_routes(app):

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/services')
    def services():
        return render_template('services.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
