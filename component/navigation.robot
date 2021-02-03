*** Settings ***
Library    OperatingSystem
Library    SeleniumLibrary    timeout=1000    implicit_wait=0

*** Variable ***
${backend_url}    http://localhost:2202/#/homePage
${browser}        firefox

*** Keywords ***
Navigate to screen
    [Arguments]                      ${screen_name}
    Wait Until Element Is Visible    //*[contains(text(), ${screen_name})] 
    Click Element                    //*[contains(text(), ${screen_name})] 

Login
    [Arguments]                ${user_name}              ${password}
    Comment                    login into the system!
    Close All Browsers
    Open Browser               ${backend_url}            ${browser}
    Maximize Browser Window

    #press تسجيل الدخول
    Wait Until Element Is Visible    //*[@id="smartadmin-root"]/div/div[2]/div[1]/div/div/nav/div[3]/ul/li[1]
    Click Element                    //*[@id="smartadmin-root"]/div/div[2]/div[1]/div/div/nav/div[3]/ul/li[1]

    #press login by email
    Wait Until Element Is Visible    //*[@id="firebaseui-auth-container"]/div/div/form/ul/li[2]/button
    Click Element                    //*[@id="firebaseui-auth-container"]/div/div/form/ul/li[2]/button

    #To select the new pop up window
    Switch Window    locator=NEW

    #input the email
    Wait Until Element Is Visible    //*[@id="identifierId"]
    Input Text                       //*[@id="identifierId"]                 ${user_name}
    Click Button                     //*[@id="identifierNext"]/div/button

    #input the password
    Wait Until Element Is Visible    //*[@id="passwordNext"]/div/button/div[1]
    Wait Until Element Is Visible    //*[@id="password"]/div[1]/div/div[1]/input    
    Input Text                       //*[@id="password"]/div[1]/div/div[1]/input    ${password}
    Wait Until Element Is Enabled    //*[@id="passwordNext"]/div/button
    Click Button                     //*[@id="passwordNext"]/div/button
    # get back to original window
    Switch Window                    MAIN
