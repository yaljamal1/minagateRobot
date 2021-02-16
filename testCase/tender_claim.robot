*** Settings ***
Library      OperatingSystem
Library      SeleniumLibrary          timeout=1000    implicit_wait=0
Library      ReactLibrary
# Library    REST
# Library    LoggingLibrary
Variables    login.py
Variables    createWaybillClaim.py


Resource    component/navigation.robot
Resource    component/ui.robot




*** Test Cases ***
Login
    ${email}=       call method    ${LoginValue}    getEmail
    ${password}=    call method    ${LoginValue}    getPassword

    Login                 ${email}               ${password}
    Switch Window         MAIN
    Navigate to screen    'المطالبات المالية'

Create Waybill Claim


    ${claimType}=                  call method    ${WaybillClaim}    getClaimType
    ${tenderId}=                   call method    ${WaybillClaim}    getTenderId
    ${tenderCompanyId}=            call method    ${WaybillClaim}    getTenderCompanyId
    ${referenceNumber}=            call method    ${WaybillClaim}    getReferenceNumber
    ${clearingAgent}=              call method    ${WaybillClaim}    getClearingAgent
    ${createTenderClaimButton}=    call method    ${WaybillClaim}    getCreateTenderClaimButton

    # press Create button
    Wait Until Element Is Visible    //*[@id="--jarviswidget-1"]/header/div/div/span[1]/i
    Click Element                    //*[@id="--jarviswidget-1"]/header/div/div/span[1]/i    

    # choose claim_type
    MG_Select    'claim_type'    ${claimType}

    # choose tender_id
    MG_Select    'tender_id'    ${tenderId}

    # choose tender_company_id
    MG_Select    'tender_company_id'    ${tenderCompanyId}

    # fill ref num
    MG_Input    'reference_number'    ${referenceNumber}

    # # fill ca
    MG_Select    'clearing_agent'    ${clearingAgent}

    # # click create
    MG_button    ${createTenderClaimButton}
