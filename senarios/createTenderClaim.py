import datetime
import robot
import robotlibcore
import requests
import json
import collections
import random
import time
import decimal
import urllib.parse


class createTenderClaimClass:
    def __init__(self):
        self.main()
        self.defultValues = {
            "pa_id": "1",
            "loadingWeight": "32000",
            "dischargeWeight": "30000",
            "loadingTimeStamp": "2021-01-15",
            "dischargeTimeStamp": "2021-01-16",
            "arrivalTimeStamp": "2021-01-16",
            "policyNumber": "12345",
            "waybill_id": "12345",
            "cargoId": "12345",
            "tenderId": "12345",
            "cargoName": "12345",
            "destination": "12345"
        }

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
            {"rate": 0.01, "behavior": "sucsess"},
            {"rate": -0.1, "behavior": "sucsess"},
            {"rate": -0.05, "behavior": "sucsess"},
            {"rate": 20, "behavior": "fail"},
            {"rate": -20, "behavior": "fail"}
        ]
        dischargeHours = [24]
        arrivalHours = [15]
        status = ["ONROAD"]
        pa_id = ['37']
        limit = len(pa_id)+len(status)+len(arrivalHours) + \
            len(dischargeHours)+len(dischargeWeightDeff)
        print(limit)
        for pa in pa_id:
            for state in status:
                for deff in dischargeWeightDeff:
                    self.getWn(deff=deff, limit=limit,
                               dischargeHours=dischargeHours, arrivalHours=arrivalHours, status=state, pa_id=pa)

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
            while count < len(waybillData):
                counter += 1
                print(counter)
                # for h in dischargeHours:
                print(dischargeHours[hours])
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
                dischargeWeight = cargo[0]["weights"]["discharge"]["net_weight"]
                dischargeWeight = float(
                    dischargeWeight)+(float(dischargeWeight) * deff["rate"])
                dischargeTimeStamp = cargo[0]["weights"]["discharge"]["time_stamp"]
                dischargeTimeStampDef = datetime.datetime.strptime(
                    dischargeTimeStamp,
                    "%Y-%m-%d %H:%M")+datetime.timedelta(hours=dischargeHours[hours])
                loadingTimeStamp = cargo[0]["weights"]["loading"]["time_stamp"]
                arrivalTimeStamp = dischargeTimeStamp
                arrivalTimeStampDeff = datetime.datetime.strptime(
                    arrivalTimeStamp,
                    "%Y-%m-%d %H:%M")+datetime.timedelta(hours=arrivalHours[hours])
                destination = document["negotiable_instructios"]["route"]["destination"]["id"]

                # self.collectData("1234", "123444")
                # appendRes = self.appendWaybillToARClaim(loadingWeight, dischargeWeight, loadingTimeStamp, dischargeTimeStamp,
                #                                         arrivalTimeStamp, policyNumber, waybill_id, cargoId, tenderId, cargoName, destination, pa_id)
                # print(appendRes)
                count += 1
                hours += 1

    def collectData(self, loadingWeight='', dischargeWeight='', loadingTimeStamp='', dischargeTimeStamp='', arrivalTimeStamp='', policyNumber='', waybill_id='', cargoId='', tenderId='', cargoName='', destination='', pa_id=''):
        count = 0
        # print(self.defultValues.keys())

        while count < len(self.defultValues):
            for key in self.defultValues.keys():
                if loadingWeight == "" and key == "loadingWeight":
                    loadingWeight = self.defultValues[key]
                    print(loadingWeight, "loadingWeight")
                    count += 1
                if dischargeWeight == "" and key == "dischargeWeight":
                    dischargeWeight = self.defultValues[key]
                    print(dischargeWeight, "dischargeWeight")
                    count += 1
                if pa_id == "" and key == "pa_id":
                    pa_id = self.defultValues[key]
                    print(pa_id, "pa_id")
                    count += 1
                if loadingWeight == "" and key == "loadingWeight":
                    loadingWeight = self.defultValues[key]
                    print(loadingWeight, "loadingWeight")
                    count += 1

                if dischargeWeight == "" and key == "dischargeWeight":
                    dischargeWeight = self.defultValues[key]
                    print(dischargeWeight, "dischargeWeight")
                    count += 1

                if loadingTimeStamp == "" and key == "loadingTimeStamp":
                    loadingTimeStamp = self.defultValues[key]
                    print(loadingTimeStamp, "loadingTimeStamp")
                    count += 1

                if dischargeTimeStamp == "" and key == "dischargeTimeStamp":
                    dischargeTimeStamp = self.defultValues[key]
                    print(dischargeTimeStamp, "dischargeTimeStamp")
                    count += 1

                if arrivalTimeStamp == "" and key == "arrivalTimeStamp":
                    arrivalTimeStamp = self.defultValues[key]
                    print(arrivalTimeStamp, "arrivalTimeStamp")
                    count += 1

                if policyNumber == "" and key == "policyNumber":
                    policyNumber = self.defultValues[key]
                    print(policyNumber, "policyNumber")
                    count += 1

                if waybill_id == "" and key == "waybill_id":
                    waybill_id = self.defultValues[key]
                    print(waybill_id, "waybill_id")
                    count += 1

                if cargoId == "" and key == "cargoId":
                    cargoId = self.defultValues[key]
                    print(cargoId, "cargoId")
                    count += 1

                if tenderId == "" and key == "tenderId":
                    tenderId = self.defultValues[key]
                    print(tenderId, "tenderId")
                    count += 1

                if cargoName == "" and key == "cargoName":
                    cargoName = self.defultValues[key]
                    print(cargoName, "cargoName")
                    count += 1

                if destination == "" and key == "destination":
                    destination = self.defultValues[key]
                    print(destination, "destination")
                    count += 1
                count += 1

        # self.validation(waybill_id)

    def validation(self, waybill_id):
        print(waybill_id, 'waybill_id')
        res = requests.get(
            f'https://api-dev-dot-waybill-project.appspot.com/tender_claim?method=searchTenderClaimItems&filter={"waybill_id":{waybill_id},"status":"NEW"}&integration_token=YAZAN')
        print(res.json(), "res")

    def formatData(self):
        print("test")

    def appendWaybillToARClaim(self, loadingWeight, dischargeWeight, loadingTimeStamp, dischargeTimeStamp, arrivalTimeStamp, policyNumber, waybill_id, cargoId, tenderId, cargoName, destination, pa_id):
        # self.calculateFreight()

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
        return JsonRes


createTenderClaimClass()
