from flask import Flask
from zapata.app import app


def test_main(mocker):
    mocker.patch("flask.Flask.run")
    app.main()
    Flask.run.assert_called_once()
