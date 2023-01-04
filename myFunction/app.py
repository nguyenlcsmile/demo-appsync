import json
import os
import time
from random import randrange
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import asyncio


def index(event, context):
    transport = AIOHTTPTransport(
        url='https://tm4ol33pqrar3jeplycp6k6qiq.appsync-api.ap-southeast-1.amazonaws.com/graphql',
        headers={
            'x-api-key': 'da2-vsys5v5lkrbsddlate3zniown4'
        }
    )

    dataJson = open('onBoarding.json')
    dataJson = json.load(dataJson)
    client = Client(transport=transport, fetch_schema_from_transport=True,)
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
    for data in dataJson:
        params = {
            'value': f'{data}'.replace('\'', '\"')
        }
        result = client.execute(document, variable_values=params)

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
        },
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
