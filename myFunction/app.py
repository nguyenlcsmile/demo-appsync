import json
import os
import time
from random import randrange
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import asyncio


def filterOnBoarding(onBoarding):
    listStep = []

    for t in onBoarding:
        if (t["eventCode"] == 'JAOFuntion./v1/jao/check-cust/GET'):
            item = {"dashboard": "OnBoarding",
                    "step": "Check Customer Phone"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'KYCFunction./v1/kyc/submit/POST'):
            item = {"dashboard": "OnBoarding",
                    "step": "Submit EKYC"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'TopUpFuntion./v1/top-up/kyc-status/POST'):
            item = {"dashboard": "OnBoarding",
                    "step": "Check KYC Status"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'ProducerFunction./v1/producer/push/PUT'):
            item = {"dashboard": "OnBoarding",
                    "step": "Video Statement"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'JAOFuntion./v1/jao/check-face-match/POST'):
            item = {"dashboard": "OnBoarding",
                    "step": "Face Match"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'JAOFuntion./v1/jao/jao-contract/POST'):
            item = {"dashboard": "OnBoarding",
                    "step": "Get Contract"
                    }
            t.update(item)
            listStep.append(t)
        elif (t["eventCode"] == 'JAOFuntion./v1/jao/verify-otp/POST'):
            item = {"dashboard": "OnBoarding",
                    "step": "Sign Contract"
                    }
            t.update(item)
            listStep.append(t)
    # print(listStep)
    return listStep


def filterFunctionals(functionals):
    listFunctionals = []

    for t in functionals:
        if (t["eventCode"] == 'ServiceFunction./v1/service/issue-card/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "Issue Card"
                    }
            t.update(item)
            listFunctionals.append(t)
        elif (t["eventCode"] == 'ServiceFunction./v1/services/request-statement/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "E-Statement"
                    }
            t.update(item)
            listFunctionals.append(t)
        elif (t["eventCode"] == 'ServiceFunction./v1/services/request-econtract/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "E-Contract"
                    }
            t.update(item)
            listFunctionals.append(t)
        elif (t["eventCode"] == 'ServiceFunction./v1/services/create-signature/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "Create Signature"
                    }
            t.update(item)
            listFunctionals.append(t)
        elif (t["eventCode"] == 'POP.CashWithdrawalVPBankCounter./api/v1/cwdr/vpbank/txn/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "Cash with Drawal"
                    }
            t.update(item)
            listFunctionals.append(t)
        elif (t["eventCode"] == 'POP.OpenTDAccountFunction./api/v1/fin/deposit/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "Open TD Account"
                    }
            t.update(item)
        elif (t["eventCode"] == 'POP.OpenTDAccountFunction./api/v1/fin/deposit/{accountId}/closure/POST'):
            item = {"dashboard": "Functionals",
                    "nameFunctionals": "Terminate TD Acount"
                    }
            t.update(item)
            listFunctionals.append(t)

    return listFunctionals


def index(event, context):
    transport = AIOHTTPTransport(
        url='https://tm4ol33pqrar3jeplycp6k6qiq.appsync-api.ap-southeast-1.amazonaws.com/graphql',
        headers={
            'x-api-key': 'da2-vsys5v5lkrbsddlate3zniown4'
        }
    )

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

    logData = []
    onBoard = filterOnBoarding(event)
    func = filterFunctionals(event)

    for ob in onBoard:
        logData.append(ob)
    for f in func:
        logData.append(f)

    json_object = json.dumps(logData, indent=4)
    dataJson = json.load(json_object)

    client = Client(transport=transport, fetch_schema_from_transport=True,)

    for data in dataJson:
        params = {
            'value': f'{data}'.replace('\'', '\"')
        }
        result = client.execute(document, variable_values=params)

    return {
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
