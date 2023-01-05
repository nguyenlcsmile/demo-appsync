import json
import os
import time
from random import randrange
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import asyncio

# valueOnboarding = []


# def addFirstBoxOnboarding(statusCode, data, listInformation):
#     if (statusCode == 200):
#         dataDaily = {
#             "total": 1,
#             "success": 1,
#             "failure": 0
#         }

#         valueOnboarding.append({
#             "daily": dataDaily,
#             "detailCustomers": listInformation,
#             "nameBox": data.get('step')
#         })

#     elif (statusCode == 400 and data.get('step') == 'Check Cust Phone'):
#         dataDaily = {
#             "total": 1,
#             "success": 1,
#             "failure": 0
#         }
#         valueOnboarding.append({
#             "daily": dataDaily,
#             "detailCustomers": listInformation,
#             "nameBox": data.get('step')
#         })
#     else:
#         dataDaily = {
#             "total": 1,
#             "success": 0,
#             "failure": 1
#         }
#         valueOnboarding.append({
#             "daily": dataDaily,
#             "detailCustomers": listInformation,
#             "nameBox": data.get('step')
#         })


# def checkValueExists(data, dataCheck):
#     for item in data:
#         if (item[0].get('phone') == dataCheck.get('phone') and
#             item[0].get('cifId') == dataCheck.get('cifId') and
#             item[0].get('url') == dataCheck.get('dataDetail').get('url') and
#                 item[0].get('statusCode') == dataCheck.get('dataDetail').get('statusCode')):
#             return True
#         return False


def index(event, context):
    transport = AIOHTTPTransport(
        url='https://tm4ol33pqrar3jeplycp6k6qiq.appsync-api.ap-southeast-1.amazonaws.com/graphql',
        headers={
            'x-api-key': 'da2-vsys5v5lkrbsddlate3zniown4'
        }
    )

    # dataJson = open('onBoarding.json')
    # dataJson = json.load(dataJson)
    dataJson = [
        {
            "check_cust_box": {"total": 105, "success": 2573, "fail": 29},
            "submit_ekyc_box": {"total": 24, "success": 77, "fail": 7},
            "submit_kyc_status_box": {"total": 31, "success": 468, "fail": 24},
            "video_statement_box": {"total": 0, "success": 17, "fail": 0},
            "face_match_box": {"total": 19, "success": 271, "fail": 127},
            "get_contract_box": {"total": 18, "success": 151, "fail": 102},
            "sign_contract_box": {"total": 11, "success": 44, "fail": 2},
            "onboarding_new_customer": 402,
            "pass_onboarding": 10,
            "issue_card_func": {"total": 8, "success": 10, "fail": 3},
            "create_signature_func": {"total": 1, "success": 2, "fail": 4},
            "request_econtract_func": {"total": 0, "success": 0, "fail": 0},
            "request_statement_func": {"total": 0, "success": 0, "fail": 0},
            "cash_withdrawal_func": {"total": 1, "success": 15, "fail": 5},
            "open_td_func": {"total": 0, "success": 2, "fail": 0},
            "closure_td_func": {"total": 0, "success": 1, "fail": 0},
            "uuid": "2023-01-04-today"
        },
        {
            "check_cust_box": {"total": 105, "success": 2573, "fail": 29},
            "submit_ekyc_box": {"total": 24, "success": 77, "fail": 7},
            "submit_kyc_status_box": {"total": 31, "success": 468, "fail": 24},
            "video_statement_box": {"total": 0, "success": 17, "fail": 0},
            "face_match_box": {"total": 19, "success": 271, "fail": 127},
            "get_contract_box": {"total": 18, "success": 151, "fail": 102},
            "sign_contract_box": {"total": 11, "success": 44, "fail": 2},
            "onboarding_new_customer": 402,
            "pass_onboarding": 10,
            "issue_card_func": {"total": 8, "success": 10, "fail": 3},
            "create_signature_func": {"total": 1, "success": 2, "fail": 4},
            "request_econtract_func": {"total": 0, "success": 0, "fail": 0},
            "request_statement_func": {"total": 0, "success": 0, "fail": 0},
            "cash_withdrawal_func": {"total": 1, "success": 15, "fail": 5},
            "open_td_func": {"total": 0, "success": 2, "fail": 0},
            "closure_td_func": {"total": 0, "success": 1, "fail": 0},
            "uuid": "2023-01-04-today"
        },
        {
            "check_cust_box": {"total": 105, "success": 2573, "fail": 29},
            "submit_ekyc_box": {"total": 24, "success": 77, "fail": 7},
            "submit_kyc_status_box": {"total": 31, "success": 468, "fail": 24},
            "video_statement_box": {"total": 0, "success": 17, "fail": 0},
            "face_match_box": {"total": 19, "success": 271, "fail": 127},
            "get_contract_box": {"total": 18, "success": 151, "fail": 102},
            "sign_contract_box": {"total": 11, "success": 44, "fail": 2},
            "onboarding_new_customer": 402,
            "pass_onboarding": 10,
            "issue_card_func": {"total": 8, "success": 10, "fail": 3},
            "create_signature_func": {"total": 1, "success": 2, "fail": 4},
            "request_econtract_func": {"total": 0, "success": 0, "fail": 0},
            "request_statement_func": {"total": 0, "success": 0, "fail": 0},
            "cash_withdrawal_func": {"total": 1, "success": 15, "fail": 5},
            "open_td_func": {"total": 0, "success": 2, "fail": 0},
            "closure_td_func": {"total": 0, "success": 1, "fail": 0},
            "uuid": "2023-01-04-today"
        }
    ]
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
    # for data in dataJson[:15]:
    #     dataDetail = data.get('dataDetail')
    #     statusCode = dataDetail.get('statusCode')
    #     listInformations = []
    #     nameBoxs = []
    #     valueDaily = []

    #     if (len(valueOnboarding) != 0):
    #         for item in valueOnboarding:
    #             if (item.get('nameBox')):
    #                 nameBoxs.append(item.get('nameBox'))
    #             if (item.get('daily')):
    #                 valueDaily.append(item.get('daily'))
    #             if (len(item.get('detailCustomers')) != 0):
    #                 listInformations.append(item.get('detailCustomers'))
    #     else:
    #         if (statusCode or data.get('phone')):
    #             listInformations.append({
    #                 "statusCode": statusCode,
    #                 "phone": data.get('phone'),
    #                 "url": dataDetail.get('url'),
    #                 "cifId": data.get('cifId')
    #             })

    #     if (len(valueOnboarding) == 0 and data):
    #         addFirstBoxOnboarding(statusCode, data, listInformations)

    #     elif (len(valueOnboarding) != 0 and data):
    #         if (data.get('step') in nameBoxs):
    #             index = nameBoxs.index(data.get('step'))
    #             dataDaily = valueDaily[index]
    #             listInformation = listInformations[index]

    #             if (data.get('phone') or dataDetail.get('statusCode') or data.get('cifId')):
    #                 dataAdd = {
    #                     "statusCode": dataDetail.get('statusCode'),
    #                     "phone": data.get('phone'),
    #                     "url": dataDetail.get('url'),
    #                     "cifId": data.get('cifId')
    #                 }
    #                 checkExist = checkValueExists(listInformations, data)

    #                 if (checkExist == False):
    #                     listInformation.append(dataAdd)

    #                 if (statusCode == 200 or (statusCode == 400 and data.get('step') == 'Check Customer Phone')):
    #                     dataDailyUpdate = {
    #                         "total": dataDaily.get("total") + 1,
    #                         "success": dataDaily.get("success") + 1,
    #                         "failure": dataDaily.get("failure")
    #                     }
    #                 else:
    #                     dataDailyUpdate = {
    #                         "total":  dataDaily.get("total") + 1,
    #                         "success": dataDaily.get("success"),
    #                         "failure": dataDaily.get("failure") + 1
    #                     }

    #                 dataDispatch = {
    #                     "daily": dataDailyUpdate,
    #                     "detailCustomers": listInformation,
    #                     "nameBox": data.get('step')
    #                 }
    #             valueOnboarding[index] = dataDispatch
    #         else:
    #             listInformations = []
    #             if (data.get('phone') or dataDetail.get('statusCode')):
    #                 listInformations.append({
    #                     "statusCode": dataDetail.get('statusCode'),
    #                     "phone": data.get('phone'),
    #                     "url": dataDetail.get('url'),
    #                     "cifId": data.get('cifId')
    #                 })
    #             addFirstBoxOnboarding(statusCode, data, listInformations)

    # if (len(valueOnboarding) != 0):
    #     for data in valueOnboarding:
    #         params = {
    #             'value': f'{data}'.replace('\'', '\"')
    #         }
    #         result = client.execute(document, variable_values=params)

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
        },
        'statusCode': 200,
        'body': json.dumps("blabla")
    }
