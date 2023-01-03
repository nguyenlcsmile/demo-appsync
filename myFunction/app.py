import json
import os
import time
from random import randrange
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def index(event, context):
    transport = AIOHTTPTransport(
        url='https://cdbw4zmkabdg7dk2ytlja5itje.appsync-api.ap-southeast-1.amazonaws.com/graphql',
        headers={
            'x-api-key': 'da2-yhrtgyvlwbhclasnj7jihce3xm'
        }
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    document = gql(
        """
            mutation AddSampleData($value: Object!) {
                addSampleData(value: $value) {
                    value
                    datetime
                }
            }
        """
    )

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
