import robot
import robotlibcore
import requests
import json
import collections
import random
import time


class CreateItemsWith:
    def __init__(self):
        self.wn = []
        self.getWn()
        self.AutoComplete()

    def getWn(self):
        res = requests.get(
            'https://api-dev-dot-waybill-project.appspot.com/waybill?method=searchWaybills&filter={"tender_id":13,"status":"ONROAD"}&integration_token=YAZAN&limit=1')
        data = res.json()
        data2 = []
        for x in data:
            if x == 'data':
                data2 = data[x]
        for x in range(len(data2)):
            for y in data2[x]:
                if y == 'wn':
                    self.wn.append(data2[x][y])

        return self.wn

    def getTenderId(self):
        tenderId = '"13"'
        return tenderId

    def getTenderOrigin(self):
        tenderOrigin = "'91090000'"
        return tenderOrigin

    def getPaymentAgentId(self):
        paymentAgentId = "'37'"
        return paymentAgentId

    def getDestination(self):
        destination = "91010025"
        return destination

    # def getWN(self, wn):
    #     WN = wn
    #     return WN

    def getTN(self):
        TN = "60999999"
        return TN

    def getCargoId(self):
        cargoId = "2010000006"
        return cargoId

    def getLoadingWeight(self):
        n = str(random.randint(20000, 60000))
        loadingWeight = n
        return loadingWeight

    def getDischargeWeight(self):
        n = str(random.randint(20000, 60000))
        dischargeWeight = n
        return dischargeWeight

    def str_time_prop(self, start, end, format, prop):
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))

    def random_date(self, start, end, prop):
        return self.str_time_prop(start, end, '%Y/%m/%d', prop)

    def getLoadingTimeStamp(self):
        # loadingTimeStamp = str(self.random_date("2021/01/15",
        #                                         "2021/01/16", random.random()))
        loadingTimeStamp = '2021/01/15'
        return loadingTimeStamp

    def getArrivalTimeStamp(self):
        # arrivalTimeStamp = str(self.random_date("2021/01/15",
        #                                         "2021/02/16", random.random()))
        arrivalTimeStamp = '2021/01/16'
        return arrivalTimeStamp

    def getDischargeTimeStamp(self):
        # dischargeTimeStamp = str(self.random_date("2021/01/01",
        #                                           "2021/02/04", random.random()))
        dischargeTimeStamp = '2021/01/16'

        return dischargeTimeStamp

    def getpolicyNumber(self):
        policyNumber = "123456798"
        return policyNumber

    def getAddButton(self):
        AddButton = "'add'"
        return AddButton

    def getLateFineValue(self):
        lateFineValue = "'50'"
        return lateFineValue

    def getCompensationFineValue(self):
        compensationFineValue = "'20'"
        return compensationFineValue

    def getAbsenceFineValue(self):
        absenceFineValue = "'10'"
        return absenceFineValue

    def AutoComplete(self):
        # for x in self.wn:
        # print(x)
        res = requests.get(
            f'https://api-dev-dot-waybill-project.appspot.com/tender_claim?method=autoCompleteARWaybillInfo&tender_id=13&wn={self.wn[0]}&integration_token=YAZAN')
        data = res.json()
        # {"method": "calculateFreight", "waybill_id": "260819", "discharge_weight": "37460", "loading_weight": 37760, "loading_date": "2021-01-17", "destination_id": "91030008", "arrival_date": "2021-01-18", "discharge_date": "2021-01-18", "cargo_id": 2010000006, "type": "payable", "origin_id": 91090000}
        # print(data[0].cargo_id)

        cal = requests.get(
            f'https://api-dev-dot-waybill-project.appspot.com/payment?method=calculateFreight&waybill_id:260819&discharge_weight:37460&loading_weight:37760&loading_date:2021-01-17&destination_id:91030008&arrival_date:2021-01-18&discharge_date:2021-01-18&cargo_id:2010000006&type:payable&origin_id:91090000&integration_token=YAZAN')
        print(cal.json())
        # return data[0]


# CreateItems = CreateItemsWith()
CreateItemsWith()
# CreateItems.getDischargeTimeStamp()
