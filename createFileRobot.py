import os
from pynput.keyboard import Key, Controller
from createItems import CreateItems
data = CreateItems.getData()


# Keyboard = Controller()
# Keyboard.press(Key.Enter)
# Keyboard.release(Key.Enter)
# Specify the path
path = '/home/yazan/Desktop/Minagate Robot'
filePath = '/home/yazan/Desktop/Minagate Robot/myfile.robot'
# Specify the file name
file = 'myfile.robot'

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
        'Variables    login.py\n'
        'Variables    createItems.py\n'
        'Resource     component/navigation.robot\n'
        'Resource     component/ui.robot\n'
        'Resource     component/createItems.robot\n'
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

        text = 'Create Items'+str(index) + '\n' +\
            '   ${WN}                     Set Variable                   '+wn+'\n' +\
            '   ${tenderId}=              call method    ${CreateItems}       getTenderId\n' + \
            '   ${paymentAgentId}=        call method    ${CreateItems}       getPaymentAgentId\n' +\
            '   ${destination}=           call method    ${CreateItems}       getDestination\n' +\
            '   ${loadingWeight}=         call method    ${CreateItems}       getLoadingWeight\n' +\
            '   ${dischargeWeight}=       call method    ${CreateItems}       getDischargeWeight\n' +\
            '   ${loadingTimeStamp}=      call method    ${CreateItems}       getLoadingTimeStamp\n' +\
            '   ${arrivalTimeStamp}=      call method    ${CreateItems}       getArrivalTimeStamp\n' +\
            '   ${dischargeTimeStamp}=    call method    ${CreateItems}       getDischargeTimeStamp\n' +\
            '   ${AddButton}=             call method    ${CreateItems}       getAddButton\n' +\
            '   ${policyNumber}=          Call Method    ${CreateItems}       getpolicyNumber\n' +\
            '   ${tenderOrigin}=          Call Method    ${CreateItems}       getTenderOrigin\n' +\
            '   Create Items              ${tenderId}    ${paymentAgentId}    ${destination}    ${WN}    ${policyNumber}    ${loadingWeight}    ${dischargeWeight}    ${loadingTimeStamp}    ${arrivalTimeStamp}    ${dischargeTimeStamp}    ${tenderOrigin}\n'

        fp.write(text)
    # os.remove(filePath)
