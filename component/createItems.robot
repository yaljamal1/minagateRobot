*** Settings ***

Library    OperatingSystem
Library    SeleniumLibrary    timeout=1000    implicit_wait=0
*** Keywords ***

Create Items
    [Arguments]    ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}

    # choose tender_id
    MG_Select    'tenderId'    ${tenderId}

    # fill WN
    MG_Input      'WN'             ${WN} 
    Press Keys    //*[@id="WN"]    ENTER
    Sleep         1 seconds

    # choose paymentAgentId
    MG_Select    'paymentAgentId'    ${paymentAgentId}

    # choose tenderOrigin
    MG_Select    'tenderOrigin'    ${tenderOrigin}

    # choose destination
    MG_Select         'destination'     ${destination}
    Log To Console    ${destination}

    # fill policyNumber
    MG_Input    'policyNumber'    ${policyNumber}

    # fill loadingWeight
    MG_Input    'loadingWeight'    ${loadingWeight}

    # fill dischargeWeight
    MG_Input    'dischargeWeight'    ${dischargeWeight}

    # fill loadingTimeStamp
    MG_Input    'loadingTimeStamp'    ${loadingTimeStamp}

    # fill arrivalTimeStamp
    MG_Input    'arrivalTimeStamp'    ${arrivalTimeStamp}

    # # fill dischargeTimeStamp
    MG_Input    'dischargeTimeStamp'    ${dischargeTimeStamp}

    Sleep        2 seconds
    # click create
    MG_button    'add'

    # click add without ts3era
    MG_button    'AddTenderClamItem'

    #check if it pass or not
    Sleep                  2 seconds
    Page Should Contain    تمت عملية اضافة المستند بنجاح
    Sleep                  2 seconds
