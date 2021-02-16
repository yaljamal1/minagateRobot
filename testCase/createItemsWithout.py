import robot
import robotlibcore
import requests
import json
import collections
import random
import time


class createItemsWithout:
    def getWn(self):
        wn = []
        res = requests.get(
            'https://api-dev-dot-waybill-project.appspot.com/waybill?method=searchWaybills&filter={"tender_id":13,"status":"ONROAD"}&integration_token=YAZAN&limit=2')
        data = res.json()
        data2 = []
        for x in data:
            if x == 'data':
                data2 = data[x]
        for x in range(len(data2)):
            for y in data2[x]:
                if y == 'wn':
                    wn.append(data2[x][y])

        return wn

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
        loadingTimeStamp = str(self.random_date("2021/02/01",
                                                "2021/02/04", random.random()))
        # loadingTimeStamp = '2021/02/02'
        return loadingTimeStamp

    def getArrivalTimeStamp(self):
        arrivalTimeStamp = str(self.random_date("2021/01/01",
                                                "2021/02/04", random.random()))
        # arrivalTimeStamp = '2021/02/04'
        return arrivalTimeStamp

    def getDischargeTimeStamp(self):
        dischargeTimeStamp = str(self.random_date("2021/01/01",
                                                  "2021/02/04", random.random()))
        # dischargeTimeStamp = '2021/02/04'

        return dischargeTimeStamp

    def getpolicyNumber(self):
        policyNumber = "123456798"
        return policyNumber

    def getAddButton(self):
        AddButton = "'add'"
        return AddButton


createItemsWithout = createItemsWithout()
createItemsWithout.getWn()
# CreateItems.getDischargeTimeStamp()
