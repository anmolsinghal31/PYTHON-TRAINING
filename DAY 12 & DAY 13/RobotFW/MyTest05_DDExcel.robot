*** Settings ***
Library          SeleniumLibrary
Library          DataDriver    file=${CURDIR}/file.testdata.xlsx    sheet_name=Sheet1
Suite Setup      Open Orangehrm
Test Template    Orangehrmlogin With Excel
Suite Teardown   Close All Browsers

*** Variables ***
${url}           https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}       chrome
# These 2 lines prevent the "Unassigned" error
${username}      Admin
${password}      admin123

*** Keywords ***
Open Orangehrm
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Orangehrmlogin With Excel
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    name=username    15s
    Input Text      name=username    ${username}
    Input Text      name=password    ${password}
    Click Button    xpath=//button[@type="submit"]
    Sleep           5s
    # Logout Logic
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    15s
    Click Element   xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    link=Logout    5s
    Click Link      link=Logout
    Wait Until Element Is Visible    name=username    10s

*** Test Cases ***
Login with user from Excel    ${username}    ${password}