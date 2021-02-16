*** Settings ***

Library    OperatingSystem
Library    SeleniumLibrary    timeout=1000    implicit_wait=0
*** Keywords ***

Create Items With
    [Arguments]    ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}    ${lateFineValue}    ${compensationFineValue}    ${absenceFineValue}

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

   # fill late_fine_value
    MG_Input    'late_fine_value'    ${lateFineValue}


   # fill compensation_fine_value
    MG_Input    'compensation_fine_value'    ${compensationFineValue}

   # fill absence_fine_value
    MG_Input     'absence_fine_value'         ${absenceFineValue}
  # click create
    MG_button    'handelAddTenderClamItem'



    #check if it pass or not
    Sleep                  2 seconds
    Page Should Contain    تمت عملية اضافة المستند بنجاح
    Sleep                  2 seconds
