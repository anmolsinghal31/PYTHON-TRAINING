*** Settings ***
Library    SeleniumLibrary
# This line creates the folder automatically if it doesn't exist
Library    OperatingSystem

*** Variables ***
${URL}           https://www.google.com
${BROWSER}       chrome
${FOLDER_PATH}   ${CURDIR}/DAY 13/QUESTION 1

*** Test Cases ***
Verify Page Title And Capture Screenshot
    [Documentation]    Opens browser, checks title, and saves SS in a specific folder.

    # Create the folder first so the screenshot has a place to go
    Create Directory    ${FOLDER_PATH}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Title Should Be    Google

    # Save the screenshot into the specific folder
    Capture Page Screenshot    ${FOLDER_PATH}/google_verify.png

    [Teardown]    Close Browser