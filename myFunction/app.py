import json
import os
import time
from random import randrange
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def index(event, context):
    transport = AIOHTTPTransport(
        url='https://tm4ol33pqrar3jeplycp6k6qiq.appsync-api.ap-southeast-1.amazonaws.com/graphql',
        headers={
            'x-api-key': 'da2-vsys5v5lkrbsddlate3zniown4'
        }
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    document = gql(
        """
            mutation AddSampleData($value: String!) {
                addSampleData(value: $value) {
                    value
                    datetime
                }
            }
        """
    )

    document1 = gql(
        """
            subscription SubscribeToNewMessage1($filter: ModelSubscriptionTodoFilterInput) {
                subscribeToNewMessage1(filter: $filter) {
                    value
                    datetime
                }
                }
        """
    )
    dataJson = open('onBoarding.json')
    data = json.load(dataJson)

    for i in range(len(data)):
        params = {
            'value': f'{data[i]}'.replace('\'', '\"')
        }
        result = client.execute(document, variable_values=params)
        if (i == 20):
            result1 = client.execute(document1)
            print(result1)

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
