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
            mutation AddSampleData($id: ID!, $value: String!) {
                addSampleData(id: $id, value: $value) {
                    id
                    value
                    datetime
                }
            }
        """
    )

    document1 = gql(
        """
            mutation AddSampleData1($id: ID!, $value: String!) {
                addSampleData1(id: $id, value: $value) {
                    id
                    value
                    datetime
                }
            }
        """
    )
    i = 0
    while (True):
        i = i + 1
        value = randrange(100)
        value1 = randrange(100)

        params = {
            'id': value,
            'value': value
        }

        params1 = {
            'id': value,
            'value': value1
        }
        result = client.execute(document, variable_values=params)
        result1 = client.execute(document1, variable_values=params1)

        print(value, value1)
        if (i == 100):
            break

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
