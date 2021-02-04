*** Settings ***
Library      OperatingSystem
Library      SeleniumLibrary    timeout=1000    implicit_wait=0
Library      ReactLibrary
Variables    login.py
Variables    createItems.py
Resource     component/navigation.robot
Resource     component/ui.robot
Resource     component/createItems.robot
*** Test Cases ***
Login
   ${email}=             call method            ${LoginValue}    getEmail
   ${password}=          call method            ${LoginValue}    getPassword
   Login                 ${email}               ${password}
   Switch Window         MAIN
   Navigate to screen    "المطالبات المالية"
   Sleep                 3 seconds
   Wait Until Element Is Visible    //*[@id="AR_edit"]
   Click Element                    //*[@id="AR_edit"]
   Sleep                            1 seconds
Create Items1
   ${WN}                     Set Variable                   2120003254
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
   ${tenderOrigin}=          Call Method    ${CreateItems}       getTenderOrigin
   Create Items              ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}
Create Items2
   ${WN}                     Set Variable                   2120004505
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
   ${tenderOrigin}=          Call Method    ${CreateItems}       getTenderOrigin
   Create Items              ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}
