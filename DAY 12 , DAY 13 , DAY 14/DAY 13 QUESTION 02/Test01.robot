*** Settings ***
Library          SeleniumLibrary
# Adding 'dialect=excel' helps DataDriver handle the commas correctly
Library          DataDriver    file=data.csv    dialect=excel
Suite Setup      Open Registration Page
Test Template    Register User On TutorialsNinja
Suite Teardown   Close All Browsers

*** Variables ***
${URL}           https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}       chrome
# Placeholders to prevent "Unassigned" error if mapping flickers
${username}      ${EMPTY}
${password}      ${EMPTY}

*** Keywords ***
Open Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Register User On TutorialsNinja
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    id=input-firstname    15s

    # Using the data from your CSV
    # Note: TutorialsNinja has Firstname, Lastname, Email separately.
    # For now, we are putting your 'username' column into the 'First Name' field.
    Input Text      id=input-firstname    ${username}
    Input Text      id=input-lastname     SINGHAL
    Input Text      id=input-email        anmol${username}@gmail.com
    Input Text      id=input-telephone    7819932006

    Input Password  id=input-password     ${password}
    Input Password  id=input-confirm      ${password}

    # Mandatory Privacy Policy
    Select Checkbox    name=agree

    # Taking a screenshot for your folder (Day 13 Question 1)
    Capture Page Screenshot    DAY_13_QUESTION_1/registration_${username}.png

    # Submit the form
    Click Button       xpath=//input[@value='Continue']
    Sleep    3s

    # Go back to the registration page for the next row of data
    Go To           ${URL}

*** Test Cases ***
Register_User_With_${username}    ${username}    ${password}