*** Settings ***
Documentation    A test suite demonstrating Variables and Logging in a Login scenario.
Library          SeleniumLibrary

*** Variables ***
# Scalar Variables (Single values)
${URL}           https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}       chrome
${USERNAME}      Admin
${PASSWORD}      admin123

# List Variable (Multiple values)
@{LOG_MESSAGES}    Starting the Browser    Entering Credentials    Login Successful

*** Test Cases ***
TC003_Variable_And_Logging_Test
    [Documentation]    Test case to demonstrate how scalars and lists work in a login flow.

    # Using the first item from our List Variable
    Log To Console     \nStep 1: ${LOG_MESSAGES}[0]
    Open Browser       ${URL}    ${BROWSER}
    Maximize Browser Window

    # Using Scalar Variables
    Log To Console     Step 2: ${LOG_MESSAGES}[1]
    Wait Until Element Is Visible    name=username    timeout=10s
    Input Text         name=username    ${USERNAME}
    Input Text         name=password    ${PASSWORD}

    Capture Page Screenshot    login_step.png
    Click Button       xpath=//button[@type='submit']

    # Verification and Final Log
    Sleep              5s
    Log To Console     Step 3: ${LOG_MESSAGES}[2]
    Capture Page Screenshot    dashboard_final.png
    Close Browser