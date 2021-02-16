import robot
import robotlibcore
import requests


class CreateWaybillClaim:

    def getClaimType(self):
        claimType = "'waybill_claim'"
        return claimType

    def getTenderId(self):
        tenderId = "'13'"
        return tenderId

    def getTenderCompanyId(self):
        tenderCompanyId = "'197'"
        return tenderCompanyId

    def getReferenceNumber(self):
        referenceNumber = '1'
        return referenceNumber

    def getClearingAgent(self):
        clearingAgent = "'1'"
        return clearingAgent

    def getCreateTenderClaimButton(self):
        createTenderClaimButton = "'createTenderClaim'"
        return createTenderClaimButton


WaybillClaim = CreateWaybillClaim()
