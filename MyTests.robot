*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
001A.robot
    Open Browser    https://www.google.com    edge
    Title Should Be    Google
    Close Browser

*** Keywords ***
Open Application
    Open Browser    https://example.com    chrome
    Maximize Browser Window

*** Settings ***
Documentation     Simple Google Search Automation Project.
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window

*** Test Cases ***
001A.robot
    Open Application
    Input Text    name=q    Robot Framework
    Press Keys    name=q    ENTER
    Title Should Be    Robot Framework - Google Search
    Close Browser
