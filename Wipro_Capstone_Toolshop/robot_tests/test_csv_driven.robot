*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           String
Suite Setup       Setup Browser
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${CSV_PATH}       ${CURDIR}${/}..${/}robot_data.csv

*** Test Cases ***
Run Data Driven Tests For All Products
    ${file_content}=    Get File    ${CSV_PATH}
    @{lines}=           Split To Lines    ${file_content}    1
    FOR    ${line}    IN    @{lines}
        @{data}=        Split String    ${line}    ,
        Run Keyword If    '${line}' != ''    Data Driven Toolshop Flow    ${data[0]}    ${data[1]}    ${data[2]}
    END

*** Keywords ***
Setup Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    30 seconds

Data Driven Toolshop Flow
    [Arguments]    ${email}    ${password}    ${product}
    Go To    ${URL}

    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    20s
    Click Element    css:[data-test="nav-sign-in"]

    # Assert Email Field and Login
    Wait Until Element Is Visible    id:email    20s
    Page Should Contain Element    id:email
    Input Text       id:email       ${email}
    Input Text       id:password    ${password}
    Click Button     css:[data-test="login-submit"]

    # CRITICAL: Wait for login to finish before looking for menu
    Wait Until Location Contains    account    20s
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    20s
    Page Should Contain Element    css:[data-test="nav-menu"]

    # Search Process
    Click Element    css:.navbar-brand
    Wait Until Element Is Visible    id:search-query    20s
    Input Text       id:search-query    ${product}
    Click Button     css:[data-test="search-submit"]

    # Product Selection and Add
    Sleep            3s
    Wait Until Element Is Visible    css:a.card    20s
    Click Element    css:a.card
    Wait Until Element Is Visible    id:btn-add-to-cart    20s
    Click Button     id:btn-add-to-cart
    Run Keyword And Ignore Error    Wait Until Element Is Not Visible    css:.toast-body    5s

    # Cart and Logout
    Wait Until Element Is Visible    css:[data-test="nav-cart"]    20s
    Execute Javascript    document.querySelector('a[data-test="nav-cart"]').click()
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    20s
    Click Element    css:[data-test="nav-menu"]
    Wait Until Element Is Visible    css:[data-test="nav-sign-out"]    20s
    Click Element    css:[data-test="nav-sign-out"]

# command to run this - robot -d results robot_tests/test_csv_driven.robot