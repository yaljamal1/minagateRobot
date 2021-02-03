*** Settings ***

Library    OperatingSystem
Library    SeleniumLibrary    timeout=1000    implicit_wait=0
*** Keywords ***

Create Items
    [Arguments]    ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}


    # ${data}=                  Call Method    ${CreateItems}    getData
     # ${tenderId}=              call method    ${CreateItems}    getTenderId
    # ${paymentAgentId}=        call method    ${CreateItems}    getPaymentAgentId
    # ${destination}=           call method    ${CreateItems}    getDestination
    # ${WN}=                    call method    ${CreateItems}    getWN                    5
    # ${TN}=                    call method    ${CreateItems}    getTN
    # ${cargoId}=               call method    ${CreateItems}    getCargoId
    # ${loadingWeight}=         call method    ${CreateItems}    getLoadingWeight
    # ${dischargeWeight}=       call method    ${CreateItems}    getDischargeWeight
    # ${loadingTimeStamp}=      call method    ${CreateItems}    getLoadingTimeStamp
    # ${arrivalTimeStamp}=      call method    ${CreateItems}    getArrivalTimeStamp
    # ${dischargeTimeStamp}=    call method    ${CreateItems}    getDischargeTimeStamp
    # ${AddButton}=             call method    ${CreateItems}    getAddButton
    # ${policyNumber}=          Call Method    ${CreateItems}    getpolicyNumber
    # Log To Console                   ${data}


    #choose motalaba

      #Execute Javascript    window.scrollTo(0,200);
    # Scroll Element Into View         //*[@id="claims0"]
    # Wait Until Element is visible    //*[@id="2091000937"]    timeout=5s
    # Set Focus To Element             //*[@id="2091000937"]
    # Click Element                    //*[@id="2091000937"]
    #  Scroll Element Into View         //*[@id="2091000937"]
    # Wait Until Element Is Visible    //*[@id="claims0"]
    # Click Element                    //*[@id="claims0"]



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
    # Press Keys    //*[@id="policyNumber"]    ENTER

    # fill loadingWeight
    MG_Input    'loadingWeight'    ${loadingWeight}
    # Press Keys    //*[@id="loadingWeight"]    ENTER

    # fill dischargeWeight
    MG_Input    'dischargeWeight'    ${dischargeWeight}
    # Press Keys    ${dischargeWeight}    ENTER

    # fill loadingTimeStamp
    MG_Input    'loadingTimeStamp'    ${loadingTimeStamp}
    # Press Keys    //*[@id="loadingTimeStamp"]    ENTER

    # fill arrivalTimeStamp
    MG_Input    'arrivalTimeStamp'    ${arrivalTimeStamp}
    # Press Keys    //*[@id="arrivalTimeStamp"]    ENTER

    # # fill dischargeTimeStamp
    MG_Input    'dischargeTimeStamp'    ${dischargeTimeStamp}
    # Press Keys    //*[@id="dischargeTimeStamp"]    ENTER

    Sleep        2 seconds
    # click create
    MG_button    'add'

    #To select the new pop up window
    # Switch Window    locator=NEW

    # click add without ts3era
    MG_button    'AddTenderClamItem'

    Sleep                  2 seconds
    Pass Execution if      Current Frame Should Not Contain    تمت عملية اضافة المستند بنجاح
    Page Should Contain    تمت عملية اضافة المستند بنجاح
    Sleep                  2 seconds
