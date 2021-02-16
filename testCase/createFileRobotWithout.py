import os
from createItemsWithout import createItemsWithout
data = createItemsWithout.getWn()

# Specify the path
path = '/home/yazan/Desktop/MinagateRobot'
filePath = '/home/yazan/Desktop/MinagateRobot/createItemsWithout.robot'
# Specify the file name
file = 'createItemsWithout.robot'

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
        'Variables    testCase/createItemsWithout.py\n'
        'Resource     component/navigation.robot\n'
        'Resource     component/ui.robot\n'
        'Resource     component/createItemsWithout.robot\n'
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
            '   ${WN}                     Set Variable                   '+wn+'\n' +\
            '   ${tenderId}=              call method    ${createItemsWithout}       getTenderId\n' + \
            '   ${paymentAgentId}=        call method    ${createItemsWithout}       getPaymentAgentId\n' +\
            '   ${destination}=           call method    ${createItemsWithout}       getDestination\n' +\
            '   ${loadingWeight}=         call method    ${createItemsWithout}       getLoadingWeight\n' +\
            '   ${dischargeWeight}=       call method    ${createItemsWithout}       getDischargeWeight\n' +\
            '   ${loadingTimeStamp}=      call method    ${createItemsWithout}       getLoadingTimeStamp\n' +\
            '   ${arrivalTimeStamp}=      call method    ${createItemsWithout}       getArrivalTimeStamp\n' +\
            '   ${dischargeTimeStamp}=    call method    ${createItemsWithout}       getDischargeTimeStamp\n' +\
            '   ${AddButton}=             call method    ${createItemsWithout}       getAddButton\n' +\
            '   ${policyNumber}=          Call Method    ${createItemsWithout}       getpolicyNumber\n' +\
            '   ${tenderOrigin}=          Call Method    ${createItemsWithout}       getTenderOrigin\n' +\
            '   Create Items Without             ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}\n'

        fp.write(testCases)
    # os.remove(filePath)
