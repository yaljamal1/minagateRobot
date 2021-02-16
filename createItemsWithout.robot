*** Settings ***
Library      OperatingSystem
Library      SeleniumLibrary    timeout=1000    implicit_wait=0
Library      ReactLibrary
Variables    testCase/login.py
Variables    testCase/createItemsWithout.py
Resource     component/navigation.robot
Resource     component/ui.robot
Resource     component/createItemsWithout.robot
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
   ${WN}                     Set Variable                   2120005711
   ${tenderId}=              call method    ${createItemsWithout}       getTenderId
   ${paymentAgentId}=        call method    ${createItemsWithout}       getPaymentAgentId
   ${destination}=           call method    ${createItemsWithout}       getDestination
   ${loadingWeight}=         call method    ${createItemsWithout}       getLoadingWeight
   ${dischargeWeight}=       call method    ${createItemsWithout}       getDischargeWeight
   ${loadingTimeStamp}=      call method    ${createItemsWithout}       getLoadingTimeStamp
   ${arrivalTimeStamp}=      call method    ${createItemsWithout}       getArrivalTimeStamp
   ${dischargeTimeStamp}=    call method    ${createItemsWithout}       getDischargeTimeStamp
   ${AddButton}=             call method    ${createItemsWithout}       getAddButton
   ${policyNumber}=          Call Method    ${createItemsWithout}       getpolicyNumber
   ${tenderOrigin}=          Call Method    ${createItemsWithout}       getTenderOrigin
   Create Items Without             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}
Create Items2
   ${WN}                     Set Variable                   2120005710
   ${tenderId}=              call method    ${createItemsWithout}       getTenderId
   ${paymentAgentId}=        call method    ${createItemsWithout}       getPaymentAgentId
   ${destination}=           call method    ${createItemsWithout}       getDestination
   ${loadingWeight}=         call method    ${createItemsWithout}       getLoadingWeight
   ${dischargeWeight}=       call method    ${createItemsWithout}       getDischargeWeight
   ${loadingTimeStamp}=      call method    ${createItemsWithout}       getLoadingTimeStamp
   ${arrivalTimeStamp}=      call method    ${createItemsWithout}       getArrivalTimeStamp
   ${dischargeTimeStamp}=    call method    ${createItemsWithout}       getDischargeTimeStamp
   ${AddButton}=             call method    ${createItemsWithout}       getAddButton
   ${policyNumber}=          Call Method    ${createItemsWithout}       getpolicyNumber
   ${tenderOrigin}=          Call Method    ${createItemsWithout}       getTenderOrigin
   Create Items Without             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}
