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

    while (True):
        value = randrange(100)
        params = {
            'id': value,
            'value': value
        }
        result = client.execute(document, variable_values=params)
        time.sleep(1)
        if (value == 22):
            break

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
