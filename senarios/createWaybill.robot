*** Settings ***
Library      String
Library      Collections
Variables    senarios/createTenderClaim.py
Library      OperatingSystem
Library      SeleniumLibrary                  timeout=1000    implicit_wait=0


*** Test Cases ***

createTenderClaim
    ${createTenderClaimRes}=    call method                                                                                      ${createTenderClaimClass}    createTenderClaim    
    Log To Console              ${createTenderClaimRes}
    Run Keyword if              ${createTenderClaimRes} == {'ERRORCODE': '0', 'MESSAGE': 'TENDER_CLAIM.SUCCESSFUL_OPERATION'}    Log To Console               Done                 ELSE    Log To Console    Fail    
    Log To Console              ${createTenderClaimRes}


createItemWithWagePerTon

