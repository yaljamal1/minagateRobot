*** Settings ***
Library      OperatingSystem
Library      SeleniumLibrary    timeout=1000    implicit_wait=0
Library      ReactLibrary
Variables    testCase/login.py
Variables    testCase/createItemsWith.py
Resource     component/navigation.robot
Resource     component/ui.robot
Resource     component/createItemsWith.robot
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
   ${WN}                        Set Variable                   2120005710
   ${tenderId}=                 call method    ${CreateItemsWith}       getTenderId
   ${paymentAgentId}=           call method    ${CreateItemsWith}       getPaymentAgentId
   ${destination}=              call method    ${CreateItemsWith}       getDestination
   ${loadingWeight}=            call method    ${CreateItemsWith}       getLoadingWeight
   ${dischargeWeight}=          call method    ${CreateItemsWith}       getDischargeWeight
   ${loadingTimeStamp}=         call method    ${CreateItemsWith}       getLoadingTimeStamp
   ${arrivalTimeStamp}=         call method    ${CreateItemsWith}       getArrivalTimeStamp
   ${dischargeTimeStamp}=       call method    ${CreateItemsWith}       getDischargeTimeStamp
   ${AddButton}=                call method    ${CreateItemsWith}       getAddButton
   ${policyNumber}=             Call Method    ${CreateItemsWith}       getpolicyNumber
   ${tenderOrigin}=             Call Method    ${CreateItemsWith}       getTenderOrigin
   ${lateFineValue} =           Call Method    ${CreateItemsWith}       getLateFineValue
   ${compensationFineValue} =          Call Method    ${CreateItemsWith}       getCompensationFineValue
   ${absenceFineValue} =          Call Method    ${CreateItemsWith}       getAbsenceFineValue
   Create Items With             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}  ${lateFineValue}    ${compensationFineValue}    ${absenceFineValue}
Create Items2
   ${WN}                        Set Variable                   2120005711
   ${tenderId}=                 call method    ${CreateItemsWith}       getTenderId
   ${paymentAgentId}=           call method    ${CreateItemsWith}       getPaymentAgentId
   ${destination}=              call method    ${CreateItemsWith}       getDestination
   ${loadingWeight}=            call method    ${CreateItemsWith}       getLoadingWeight
   ${dischargeWeight}=          call method    ${CreateItemsWith}       getDischargeWeight
   ${loadingTimeStamp}=         call method    ${CreateItemsWith}       getLoadingTimeStamp
   ${arrivalTimeStamp}=         call method    ${CreateItemsWith}       getArrivalTimeStamp
   ${dischargeTimeStamp}=       call method    ${CreateItemsWith}       getDischargeTimeStamp
   ${AddButton}=                call method    ${CreateItemsWith}       getAddButton
   ${policyNumber}=             Call Method    ${CreateItemsWith}       getpolicyNumber
   ${tenderOrigin}=             Call Method    ${CreateItemsWith}       getTenderOrigin
   ${lateFineValue} =           Call Method    ${CreateItemsWith}       getLateFineValue
   ${compensationFineValue} =          Call Method    ${CreateItemsWith}       getCompensationFineValue
   ${absenceFineValue} =          Call Method    ${CreateItemsWith}       getAbsenceFineValue
   Create Items With             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}  ${lateFineValue}    ${compensationFineValue}    ${absenceFineValue}
