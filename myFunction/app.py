import json
import os
import time
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

    listValue = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

    for i in range(len(listValue)):
        params = {
            'id': i,
            'value': listValue[i]
        }
        result = client.execute(document, variable_values=params)
        print(result)
        time.sleep(3)

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
