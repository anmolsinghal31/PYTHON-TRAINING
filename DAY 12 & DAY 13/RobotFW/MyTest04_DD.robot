*** Settings ***
Library          SeleniumLibrary
Test Template    orangehrmlogin

*** Variables ***
${url}           https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}       chrome

*** Keywords ***
open orangehrm
    open browser     ${url}     ${browser}
    maximize browser window

orangehrmlogin
    [Arguments]    ${username}   ${password}
    open orangehrm
    wait until element is visible    name=username    10s
    input text     name=username   ${username}
    input text     name=password   ${password}
    capture page screenshot    login_page_success.png
    click button    xpath=//button[@type='submit']
    sleep           5s
    capture page screenshot    dashboard_success.png
    close browser

*** Test Cases ***
Valid Login      Admin    admin123