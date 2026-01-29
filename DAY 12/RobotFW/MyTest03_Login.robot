*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}     chrome
${username}    Admin
${password}    admin123

*** Test Cases ***
TC003_Login_Test
    open browser    ${url}    ${browser}
    maximize browser window

    # This ensures screenshots go into your project folder
    Set Screenshot Directory    ${CURDIR}

    wait until element is visible    name=username    timeout=10s
    input text      name=username    ${username}
    input text      name=password    ${password}

    # Force a unique name for the screenshot
    Capture Page Screenshot    login_page_success.png

    click button    xpath=//button[@type='submit']
    sleep           5s
    Capture Page Screenshot    dashboard_success.png

    close browser