import os
from createItemsWith import CreateItemsWith
data = CreateItemsWith.getWn()

# Specify the path
path = '/home/yazan/Desktop/MinagateRobot'
filePath = '/home/yazan/Desktop/MinagateRobot/createItemsWith.robot'
# Specify the file name
file = 'createItemsWith.robot'

# Before creating
dir_list = os.listdir(path)
# Creating a file at specified location
with open(os.path.join(path, file), 'w') as fp:
    pass
    # To write data to new file uncomment
    fp.write(
        '*** Settings ***\n'
        'Library      OperatingSystem\n'
        'Library      SeleniumLibrary    timeout=1000    implicit_wait=0\n'
        'Library      ReactLibrary\n'
        'Variables    testCase/login.py\n'
        'Variables    testCase/createItemsWith.py\n'
        'Resource     component/navigation.robot\n'
        'Resource     component/ui.robot\n'
        'Resource     component/createItemsWith.robot\n'
        '*** Test Cases ***\n'
        'Login\n'
        '   ${email}=             call method            ${LoginValue}    getEmail\n'
        '   ${password}=          call method            ${LoginValue}    getPassword\n'
        '   Login                 ${email}               ${password}\n'
        '   Switch Window         MAIN\n'
        '   Navigate to screen    "المطالبات المالية"\n'
        '   Sleep                 3 seconds\n'
        '   Wait Until Element Is Visible    //*[@id="AR_edit"]\n'
        '   Click Element                    //*[@id="AR_edit"]\n'
        '   Sleep                            1 seconds\n'
    )
    index = 0
    for wn in data:
        print(wn)
        index = index+1

        testCases = 'Create Items'+str(index) + '\n' +\
            '   ${WN}                        Set Variable                   '+wn+'\n' +\
            '   ${tenderId}=                 call method    ${CreateItemsWith}       getTenderId\n' + \
            '   ${paymentAgentId}=           call method    ${CreateItemsWith}       getPaymentAgentId\n' +\
            '   ${destination}=              call method    ${CreateItemsWith}       getDestination\n' +\
            '   ${loadingWeight}=            call method    ${CreateItemsWith}       getLoadingWeight\n' +\
            '   ${dischargeWeight}=          call method    ${CreateItemsWith}       getDischargeWeight\n' +\
            '   ${loadingTimeStamp}=         call method    ${CreateItemsWith}       getLoadingTimeStamp\n' +\
            '   ${arrivalTimeStamp}=         call method    ${CreateItemsWith}       getArrivalTimeStamp\n' +\
            '   ${dischargeTimeStamp}=       call method    ${CreateItemsWith}       getDischargeTimeStamp\n' +\
            '   ${AddButton}=                call method    ${CreateItemsWith}       getAddButton\n' +\
            '   ${policyNumber}=             Call Method    ${CreateItemsWith}       getpolicyNumber\n' +\
            '   ${tenderOrigin}=             Call Method    ${CreateItemsWith}       getTenderOrigin\n' +\
            '   ${lateFineValue} =           Call Method    ${CreateItemsWith}       getLateFineValue\n' +\
            '   ${compensationFineValue} =          Call Method    ${CreateItemsWith}       getCompensationFineValue\n' +\
            '   ${absenceFineValue} =          Call Method    ${CreateItemsWith}       getAbsenceFineValue\n' +\
            '   Create Items With             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}  ${lateFineValue}    ${compensationFineValue}    ${absenceFineValue}\n'

        fp.write(testCases)
    # os.remove(filePath)
