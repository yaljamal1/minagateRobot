*** Settings ***
Library      OperatingSystem
Library      SeleniumLibrary          timeout=1000    implicit_wait=0
Library      ReactLibrary
Variables    login.py
Variables    createItemsWithout.py


Resource    component/navigation.robot
Resource    component/ui.robot
Resource    component/createItemsWithout.robot

*** Test Cases ***
Login
    ${email}=             call method            ${LoginValue}    getEmail
    ${password}=          call method            ${LoginValue}    getPassword
    Login                 ${email}               ${password}
    Switch Window         MAIN
    Navigate to screen    'المطالبات المالية'
    Sleep                 5 seconds

Create Items
    ${WN}=                    call method    ${CreateItems}       getWN                    
    ${tenderId}=              call method    ${CreateItems}       getTenderId
    ${paymentAgentId}=        call method    ${CreateItems}       getPaymentAgentId
    ${destination}=           call method    ${CreateItems}       getDestination
    ${loadingWeight}=         call method    ${CreateItems}       getLoadingWeight
    ${dischargeWeight}=       call method    ${CreateItems}       getDischargeWeight
    ${loadingTimeStamp}=      call method    ${CreateItems}       getLoadingTimeStamp
    ${arrivalTimeStamp}=      call method    ${CreateItems}       getArrivalTimeStamp
    ${dischargeTimeStamp}=    call method    ${CreateItems}       getDischargeTimeStamp
    ${AddButton}=             call method    ${CreateItems}       getAddButton
    ${policyNumber}=          Call Method    ${CreateItems}       getpolicyNumber
    Create Items              ${tenderId}    ${paymentAgentId}    ${destination}           ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}
