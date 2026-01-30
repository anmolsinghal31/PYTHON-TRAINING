*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
001A.robot
    Open Browser     https://www.google.com    chrome
    Maximize Browser Window
    Input Text       name=q    Robot Framework
    Press Keys       name=q    ENTER
    Sleep            5s
    Page Should Contain    Robot Framework
    Close Browser