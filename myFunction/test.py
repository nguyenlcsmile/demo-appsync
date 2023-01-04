import json

dataJson = open('onBoarding.json')
dataJson = json.load(dataJson)
valueOnboarding = []


def addFirstBoxOnboarding(statusCode, data, listInformation):
    if (statusCode == 200):
        dataDaily = {
            "total": 1,
            "success": 1,
            "failure": 0
        }

        valueOnboarding.append({
            "daily": dataDaily,
            "detailCustomers": listInformation,
            "nameBox": data.get('step')
        })

    elif (statusCode == 400 and data.get('step') == 'Check Cust Phone'):
        dataDaily = {
            "total": 1,
            "success": 1,
            "failure": 0
        }
        valueOnboarding.append({
            "daily": dataDaily,
            "detailCustomers": listInformation,
            "nameBox": data.get('step')
        })
    else:
        dataDaily = {
            "total": 1,
            "success": 0,
            "failure": 1
        }
        valueOnboarding.append({
            "daily": dataDaily,
            "detailCustomers": listInformation,
            "nameBox": data.get('step')
        })


def checkValueExists(data, dataCheck):
    for item in data:
        if (item[0].get('phone') == dataCheck.get('phone') and
            item[0].get('cifId') == dataCheck.get('cifId') and
            item[0].get('url') == dataCheck.get('dataDetail').get('url') and
                item[0].get('statusCode') == dataCheck.get('dataDetail').get('statusCode')):
            return True
        return False


for data in dataJson[:15]:
    dataDetail = data.get('dataDetail')
    statusCode = dataDetail.get('statusCode')
    listInformations = []
    nameBoxs = []
    valueDaily = []

    if (len(valueOnboarding) != 0):
        for item in valueOnboarding:
            if (item.get('nameBox')):
                nameBoxs.append(item.get('nameBox'))
            if (item.get('daily')):
                valueDaily.append(item.get('daily'))
            if (len(item.get('detailCustomers')) != 0):
                listInformations.append(item.get('detailCustomers'))
    else:
        if (statusCode or data.get('phone')):
            listInformations.append({
                "statusCode": statusCode,
                "phone": data.get('phone'),
                "url": dataDetail.get('url'),
                "cifId": data.get('cifId')
            })

    if (len(valueOnboarding) == 0 and data):
        addFirstBoxOnboarding(statusCode, data, listInformations)

    elif (len(valueOnboarding) != 0 and data):
        if (data.get('step') in nameBoxs):
            index = nameBoxs.index(data.get('step'))
            dataDaily = valueDaily[index]
            listInformation = listInformations[index]

            if (data.get('phone') or dataDetail.get('statusCode') or data.get('cifId')):
                dataAdd = {
                    "statusCode": dataDetail.get('statusCode'),
                    "phone": data.get('phone'),
                    "url": dataDetail.get('url'),
                    "cifId": data.get('cifId')
                }
                checkExist = checkValueExists(listInformations, data)

                if (checkExist == False):
                    listInformation.append(dataAdd)

                if (statusCode == 200 or (statusCode == 400 and data.get('step') == 'Check Customer Phone')):
                    dataDailyUpdate = {
                        "total": dataDaily.get("total") + 1,
                        "success": dataDaily.get("success") + 1,
                        "failure": dataDaily.get("failure")
                    }
                else:
                    dataDailyUpdate = {
                        "total":  dataDaily.get("total") + 1,
                        "success": dataDaily.get("success"),
                        "failure": dataDaily.get("failure") + 1
                    }

                dataDispatch = {
                    "daily": dataDailyUpdate,
                    "detailCustomers": listInformation,
                    "nameBox": data.get('step')
                }
            valueOnboarding[index] = dataDispatch
        else:
            listInformations = []
            if (data.get('phone') or dataDetail.get('statusCode')):
                listInformations.append({
                    "statusCode": dataDetail.get('statusCode'),
                    "phone": data.get('phone'),
                    "url": dataDetail.get('url'),
                    "cifId": data.get('cifId')
                })
            addFirstBoxOnboarding(statusCode, data, listInformations)

print(valueOnboarding, len(valueOnboarding))
# for data in valueOnboarding:
#     print(f'{data}', type(f'{data}'))
