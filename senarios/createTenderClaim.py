import datetime
import os
import robot
import robotlibcore
import requests
import json
import collections
import random
import time
import decimal
import urllib.parse
from yattag import Doc
doc, tag, text = Doc().tagtext()


class createTenderClaimClass:
    def __init__(self):
        self.main()

    def createTenderClaim(self):
        randRefId = random.randint(1, 1000)
        # print(randRefId)
        payload = {
            "tender_company_id": "197",
            "ref_id": randRefId,
            "claim_type": "waybill_claim",
            "ca_id": 10184,
            "integration_token": "YAZAN"
        }
        url = 'https://api-dev-dot-waybill-project.appspot.com/tender_claim?method:createTenderClaim'
        res = requests.post(url, data=payload)
        JsonRes = res.json()
        return JsonRes

    def main(self):
        # senarios
        dischargeWeightDeff = [
            {"rate": 0.01, "behavior": {'ERRORCODE': '200'}},
            {"rate": -0.1, "behavior": {'ERRORCODE': '200'}},
            {"rate": 20, "behavior": {'ERRORCODE': '500'}},
            {"rate": -20, "behavior": {'ERRORCODE': '500'}}
        ]
        dischargeHours = [24, 72]
        arrivalHours = [15, 40]
        status = ["ONROAD", "NEW"]
        pa_id = ['37', '1']
        limit = len(pa_id)+len(status)+len(arrivalHours) + \
            len(dischargeHours)+len(dischargeWeightDeff)
        print(limit)
        f = open('report.json', 'a+')
        f.truncate(0)
        f.write('[')
        f.close()
        for pa in pa_id:
            for state in status:
                for deff in dischargeWeightDeff:
                    self.getWn(deff=deff, limit=1,
                               dischargeHours=dischargeHours, arrivalHours=arrivalHours, status=state, pa_id=pa)
        f = open('report.json', 'a+')
        f.write(']')

    def getWn(self, deff, dischargeHours, arrivalHours, status, pa_id, limit):
        filterData = {
            "tender_id": 13,
            "status": status
        }
        fd_json = json.dumps(filterData)
        url = f'https://api-dev-dot-waybill-project.appspot.com/waybill?method=searchWaybills&filter={fd_json}&integration_token=YAZAN&limit={limit}'
        res = requests.get(url=url)
        waybillsJson = res.json()
        # print(waybillsJson)
        waybillData = []
        wn = ''
        tn = ''
        ca_id = ''
        cargo = ''
        policyNumber = random.randint(1, 10000)
        loadingWeight = 0.00
        dischargeWeight = ''
        dischargeTimeStamp = ''
        loadingTimeStamp = ''
        arrivalTimeStamp = ''
        dischargeWeight = ''
        waybill_id = ''
        tenderId = ''
        cargoName = ''
        cargoId = ''
        destination = ''
        dischargeTimeStampDef = ''
        arrivalTimeStampDeff = ''
        waybillData = waybillsJson["data"]
        count = 0
        # prossesing
        counter = 0
        hours = 0

        while hours < len(dischargeHours):

            # print(dischargeHours[hours], "dischargeHours")
            while count < len(waybillData):
                counter += 1
                print(counter, "counter")
                # for h in dischargeHours:
                waybill_id = waybillData[count]["id"]
                wn = waybillData[count]["wn"]
                print("wn", wn)
                tn = waybillData[count]["tn"]
                ca_id = waybillData[count]["ca_id"]
                document = json.loads(waybillData[count]["document"])
                cargo = document["cargo"]
                tender = document["tender"]
                tenderId = tender["id"]
                cargoId = cargo[0]["cargo"]["id"]
                cargoName = cargo[0]["name"]
                loadingWeight = cargo[0]["weights"]["loading"]["net_weight"]
                print(loadingWeight, "loadingWeight")

                # if the loadingWeight didn't available

                if loadingWeight == None:
                    loadingWeight = self.getDefultValue(
                        "loadingWeight")
                    print(loadingWeight, "loadingWeight")

                dischargeWeight = cargo[0]["weights"]["discharge"]["net_weight"]

                # if the dischargeWeight didn't available

                if dischargeWeight == None:
                    dischargeWeight = self.getDefultValue(
                        "dischargeWeight")

                dischargeWeight = float(
                    dischargeWeight)+(float(dischargeWeight) * deff["rate"])

                # if the dischargeTimeStamp didn't available

                dischargeTimeStamp = cargo[0]["weights"]["discharge"]["tare_weight"]["time_stamp"]
                if dischargeTimeStamp == None:
                    dischargeTimeStamp = self.getDefultValue(
                        "dischargeTimeStamp")

                dischargeTimeStampDef = datetime.datetime.strptime(
                    dischargeTimeStamp, "%Y-%m-%d %H:%M")+datetime.timedelta(hours=dischargeHours[hours])
                loadingTimeStamp = cargo[0]["weights"]["loading"]["tare_weight"]["time_stamp"]
                # if the loadingTimeStamp didn't available
                if loadingTimeStamp == None:
                    loadingTimeStamp = self.getDefultValue("loadingTimeStamp")
                    print(loadingTimeStamp, "loadingTimeStamp")

                # if the arrivalTimeStamp didn't available
                print(dischargeTimeStampDef, 'dischargeTimeStampDef>>>')
                arrivalTimeStamp = dischargeTimeStampDef - \
                    datetime.timedelta(hours=arrivalHours[hours])
                if arrivalTimeStamp == None:
                    arrivalTimeStamp = self.getDefultValue("arrivalTimeStamp")
                    print(arrivalTimeStamp, "arrivalTimeStamp")

                # arrivalTimeStamp = datetime.datetime.strptime(
                #     arrivalTimeStamp, "%Y-%m-%d %H:%M")+datetime.timedelta(hours=arrivalHours[hours])

                destination = document["negotiable_instructios"]["route"]["destination"]["id"]
                # if the destination didn't available
                if destination == None:
                    destination = self.getDefultValue("destination")

                # beforeAppend = self.checkMoney(policyNumber)
                # print(beforeAppend, "beforeAppend")
                actual = self.appendWaybillToARClaim(loadingWeight, dischargeWeight, loadingTimeStamp, dischargeTimeStampDef,
                                                     arrivalTimeStamp, policyNumber, waybill_id, cargoId, tenderId, cargoName, destination, pa_id)
                # print(actual)
                # afterAppend = self.checkMoney(policyNumber)
                # print(afterAppend, "afterAppend")
                params = {
                    "loadingWeight": str(loadingWeight),
                    "dischargeWeight": str(dischargeWeight),
                    "loadingTimeStamp": str(loadingTimeStamp),
                    "dischargeTimeStampDef": str(dischargeTimeStampDef),
                    "arrivalTimeStamp": str(arrivalTimeStamp),
                    "policyNumber": str(policyNumber),
                    "waybill_id": str(waybill_id),
                    "cargoId": str(cargoId),
                    "tenderId": str(tenderId),
                    "cargoName": str(cargoName),
                    "destination": str(destination),
                    "pa_id": str(pa_id),
                }
                expected = deff["behavior"]

                valid = self.validation(waybill_id, wn, actual, expected)

                testName = 'appendWaybillToARClaim'
                self.generateReport(params, count, actual,
                                    expected, testName, valid, deff["rate"], dischargeHours[hours], arrivalHours[hours], status, pa_id)
                count += 1
            hours += 1

    def getDefultValue(self, keySearch):
        count = 0
        defultValues = {
            "pa_id": "1",
            "loadingWeight": "32000",
            "dischargeWeight": "30000",
            "loadingTimeStamp": "2021-01-12 12:00",
            "dischargeTimeStamp": "2021-01-13 12:00",
            "arrivalTimeStamp": "2021-01-13 12:00",
            "policyNumber": "12345",
            "waybill_id": "255530",
            "cargoId": "2010000001",
            "tenderId": "13",
            "cargoName": "شعير مشول",
            "destination": "91000000"
        }
        while count < len(defultValues):
            for keys in defultValues.keys():
                if keys == keySearch:
                    count += 1
                    return defultValues[keySearch]
                count += 1

    def validation(self, waybill_id, wn, actual, expected):
        if actual == expected:
            filterData = {
                "waybill_id": waybill_id,
                "status": "ACTIVE"
            }
            fd_json = json.dumps(filterData)
            res = requests.get(
                f'https://api-dev-dot-waybill-project.appspot.com/tender_claim?method=searchTenderClaimItems&filter={fd_json}&integration_token=YAZAN')
            resJson = res.json()
            dump = json.loads(resJson["data"][0]["details"])
            newWn = dump["wn"]

            print(newWn, wn)
            if int(wn) == newWn:
                return 'Sucsess'
            else:
                return 'Fail'
        else:
            return 'Fail'

    def checkMoney(self, policy_number):
        print(policy_number, "policy_number")
        filterData = {
            # "waybill_id": waybill_id,
            # "status": "ACTIVE",
            "policy_number": policy_number,
            # "tender_claim_type": "AR_claim",


        }
        fd_json = json.dumps(filterData)
        res = requests.get(
            f'https://api-dev-dot-waybill-project.appspot.com//tender_claim?method=searchTenderClaims&offset=0&limit=15&filter={fd_json}&integration_token=YAZAN')
        resJson = res.json()
        print(resJson, "resJson")
        if resJson["data"]:

            tender_claim_id = resJson["data"][0]["tender_claim_id"]

            print(tender_claim_id, "tender_claim_id")
            res = requests.get(
                f'https://api-dev-dot-waybill-project.appspot.com/tender_claim?method=getTenderClaim&id={tender_claim_id}&integration_token=YAZAN')
            resJson = res.json()
            print(resJson)
            amount = resJson["claim_details"]["amount"]
            print(amount, "amount")
            return amount
        else:
            return 'Tender Not Found'

    def generateReport(self, params, count, actual, expected, testName, valid, deff, dischargeHours, arrivalHours, status, pa_id):
        report = ""
        start = '{'
        end = '}'
        title = f'\n"test_name": "{testName} dischargeWeightDeff = {deff} , dischargeHoursDeff = {dischargeHours} , arrivalHoursDeff= {arrivalHours} , status= {status} , pa_id={pa_id}" , \n"test_time":"{datetime.datetime.now()}", \n'
        params = str(params).replace(",", ",\n")
        params = str(params).replace("'", "\"")
        values = f'"params ":\n {params},\n'
        expected = f'"expected_value" : "{expected}",\n'
        actual = f'"actual_value" : "{actual}",\n'
        resultTest = f'"result_test":"{valid}"\n'
        report = start + title+values+expected+actual+resultTest+end+","+"\n"
        f = open('report.json', 'a+')
        f.write(report)
        f.close()

    def appendWaybillToARClaim(self, loadingWeight, dischargeWeight, loadingTimeStamp, dischargeTimeStamp, arrivalTimeStamp, policyNumber, waybill_id, cargoId, tenderId, cargoName, destination, pa_id):
        # self.calculateFreight()
        print(loadingTimeStamp, "loadingTimeStamp")
        url = 'https://api-dev-dot-waybill-project.appspot.com/tender_claim'
        payload = {
            "method": "appendWaybillToARClaim",
            "waybill_id": waybill_id,
            "pa_id": pa_id,
            "claim_loading_weight": loadingWeight,
            "claim_discharge_weight": dischargeWeight,
            "claim_loading_date": loadingTimeStamp,
            "claim_discharge_date": dischargeTimeStamp,
            "claim_discharge_arrive_date": arrivalTimeStamp,
            "ref_num": policyNumber,
            "destination_id": destination,
            "cargo_id": cargoId,
            "origin_id": 91090000,
            "tender_payable_id": "1",
            "item_url": "",
            "cargo_name": cargoName,
            "late_fine": 0,
            "compensation": 0,
            "absence_fine": 0,
            "loss_fine": 0,
            "claim_amount": 0,
            "tender_id": tenderId,
            "integration_token": "YAZAN"
        }
        res = requests.post(url, data=payload)
        JsonRes = res.json()

        print(JsonRes)
        result = {'ERRORCODE': f'{JsonRes["ERRORCODE"]}'}
        print(result)
        return result


createTenderClaimClass()
