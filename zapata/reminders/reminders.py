#!/usr/bin/env python3

import os

import boto3
import pandas as pd
from sqlalchemy import create_engine


def send_mail(appartment) -> None:
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_DEFAULT_REGION"),
    )
    client = session.client("ses")
    client.send_email(
        Source="liora@lmb.co.il",
        Destination={
            "ToAddresses": [
                "liora@lmb.co.il",
            ]
        },
        Message={
            "Subject": {
                "Data": f"Overdue Payment - appartment={appartment}",
                "Charset": "UTF-8",
            },
            "Body": {
                "Text": {
                    "Data": "This is a reminder to pay the house committee "
                    "payments",
                    "Charset": "UTF-8",
                },
                "Html": {
                    "Data": "This is a reminder to pay the house committee "
                    "payments",
                    "Charset": "UTF-8",
                },
            },
        },
        ReturnPath="liora@lmb.co.il",
    )


def alert(row) -> None:
    if row["Alert"]:
        send_mail(row["index"])


def main() -> None:

    SQLALCHEMY_DATABASE_URL = "postgresql://zapata:zapata@db:5432/zapata"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    with engine.begin() as connection:
        df = pd.read_sql_table("income", connection)
        df.apply(alert, axis=1)


if __name__ == "__main__":
    main()
