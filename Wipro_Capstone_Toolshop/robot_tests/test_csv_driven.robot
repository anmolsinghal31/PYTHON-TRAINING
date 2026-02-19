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
    Location Should Be    ${URL}

    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    20s
    Click Element    css:[data-test="nav-sign-in"]

    Wait Until Element Is Visible    id:email    20s
    Input Text       id:email       ${email}
    Textfield Value Should Be    id:email    ${email}
    Input Text       id:password    ${password}
    Click Button     css:[data-test="login-submit"]

    Wait Until Location Contains    account    20s
    Location Should Contain    account
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    20s
    Element Should Be Visible    css:[data-test="nav-menu"]

    Click Element    css:.navbar-brand
    Wait Until Element Is Visible    id:search-query    20s
    Input Text       id:search-query    ${product}
    Click Button     css:[data-test="search-submit"]

    Sleep            3s
    Wait Until Element Is Visible    css:a.card    20s
    Element Should Be Visible    css:a.card
    Click Element    css:a.card

    Wait Until Element Is Visible    id:btn-add-to-cart    20s
    Click Button     id:btn-add-to-cart
    Run Keyword And Ignore Error    Wait Until Element Is Not Visible    css:.toast-body    5s

    Wait Until Element Is Visible    css:[data-test="nav-cart"]    20s
    Execute Javascript    document.querySelector('a[data-test="nav-cart"]').click()
    Wait Until Location Contains    checkout    20s

    Wait Until Element Is Visible    css:[data-test="nav-menu"]    20s
    Click Element    css:[data-test="nav-menu"]
    Wait Until Element Is Visible    css:[data-test="nav-sign-out"]    20s
    Click Element    css:[data-test="nav-sign-out"]
    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    20s