*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${PATIENT_NAME}    Mark Taylor
${DISEASE}         Malaria

*** Test Cases ***
Automate Patient Registration Form
    [Documentation]    Testing the UI flow logic
    # To run this for real, you'd point it to the hospital URL
    Log To Console    Launching Browser...
    Log To Console    Entering Name: ${PATIENT_NAME}
    Log To Console    Selecting Disease: ${DISEASE}
    Log To Console    Clicking Submit Button

    # Example of a keyword-driven approach
    Verify Success Message    Registration Successful

*** Keywords ***
Verify Success Message
    [Arguments]    ${expected_msg}
    Log    Checking for message: ${expected_msg}
    # Should Be Equal    ${actual_msg}    ${expected_msg}