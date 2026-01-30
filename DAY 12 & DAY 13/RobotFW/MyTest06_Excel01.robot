*** Settings ***
Library          SeleniumLibrary
# Ensure the filename matches your saved Excel exactly
Library          DataDriver    file=${CURDIR}/file.testdata1.xlsx    sheet_name=Sheet1
Suite Setup      Open Registration Page
Test Template    Register User On TutorialsNinja
Suite Teardown   Close All Browsers

*** Variables ***
${URL}           https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}       chrome
# Placeholders to help DataDriver map variables
${firstname}     ${EMPTY}
${lastname}      ${EMPTY}
${email}         ${EMPTY}
${telephone}     ${EMPTY}
${password}      ${EMPTY}

*** Keywords ***
Open Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Register User On TutorialsNinja
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}
    Wait Until Element Is Visible    id=input-firstname    15s

    # Form Filling
    Input Text      id=input-firstname    ${firstname}
    Input Text      id=input-lastname     ${lastname}
    Input Text      id=input-email        ${email}
    Input Text      id=input-telephone    ${telephone}
    Input Password  id=input-password     ${password}
    Input Password  id=input-confirm      ${password}

    # Mandatory Checkbox and Submit
    Select Checkbox    name=agree
    Click Button       xpath=//input[@value='Continue']

    Sleep    5s
    # Navigate back to Registration for the next loop/row
    Go To    ${URL}

*** Test Cases ***
Register user ${firstname}    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}