#!/usr/bin/env python3

import os


def main():
    with open('microservices/.env', 'w') as envfile:
        envfile.write(
            'MYSQL_PASSWORD='+os.getenv('MYSQL_PASSWORD')+'\n'
        )
        envfile.write(
            'MAILCHIMP_USERNAME='+os.getenv('MAILCHIMP_USERNAME') + '\n'
        )
        envfile.write(
            'MAILCHIMP_APIKEY='+os.getenv('MAILCHIMP_APIKEY') + '\n'
        )
        envfile.write(
            'MAILCHIMP_LISTID='+os.getenv('MAILCHIMP_LISTID') + '\n'
        )


if __name__ == "__main__":
    main()
