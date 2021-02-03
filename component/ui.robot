
*** Settings ***
Library    OperatingSystem
Library    SeleniumLibrary    timeout=1000    implicit_wait=0

*** Keywords ***
MG_Select
    [Arguments]                      ${element_id}                                            ${option_value}
    Wait Until Element Is Visible    //*[@id=${element_id}]
    Click Element                    //*[@id=${element_id}]
    Mouse Down                       //*[@id=${element_id}]/option[@value=${option_value}]
    Click Element                    //*[@id=${element_id}]/option[@value=${option_value}]

MG_Input
    [Arguments]                      ${element_id}             ${value}
    Wait Until Element Is Visible    //*[@id=${element_id}]
    Input Text                       //*[@id=${element_id}]    ${value}


MG_button
    [Arguments]                      ${element_id}
    Wait Until Element Is Visible    //*[@id=${element_id}]
    Click Element                    //*[@id=${element_id}]