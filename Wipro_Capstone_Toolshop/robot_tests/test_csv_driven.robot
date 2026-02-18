*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           String
Suite Setup       Setup Browser
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${CSV_PATH}       ${CURDIR}${/}..${/}test_data.csv

*** Test Cases ***
Run Data Driven Tests From CSV
    ${file_content}=    Get File    ${CSV_PATH}
    @{lines}=           Split To Lines    ${file_content}    1
    FOR    ${line}    IN    @{lines}
        @{data}=        Split String    ${line}    ,
        Data Driven Toolshop Flow    ${data[0]}    ${data[1]}    ${data[2]}
    END

*** Keywords ***
Setup Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    20 seconds

Data Driven Toolshop Flow
    [Arguments]    ${email}    ${password}    ${product}
    Go To    ${URL}

    # Login & Assert
    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]
    Click Element    css:[data-test="nav-sign-in"]
    Input Text       id:email       ${email}
    Input Text       id:password    ${password}
    Click Button     css:[data-test="login-submit"]
    Wait Until Location Contains    account
    Location Should Contain    account    message=ASSERTION FAILED: Login Failed

    # Search & Assert
    Click Element    css:.navbar-brand
    Input Text       id:search-query    ${product}
    Click Button     css:[data-test="search-submit"]
    Wait Until Element Is Visible    css:a.card
    Page Should Contain Element      css:a.card    message=ASSERTION FAILED: Product Not Found

    # Add to Cart & Assert
    Click Element    css:a.card
    Wait Until Element Is Visible    id:btn-add-to-cart
    Element Should Be Visible        id:btn-add-to-cart    message=ASSERTION FAILED: Product Page Not Loaded
    Click Button     id:btn-add-to-cart

    # Navigate Cart & Logout
    Run Keyword And Ignore Error    Wait Until Element Is Not Visible    css:.toast-body    5s
    Execute Javascript    document.querySelector('a[data-test="nav-cart"]').click()
    Wait Until Element Is Visible    css:[data-test="product-quantity"]

    # Final Delete and Logout
    Execute Javascript    document.querySelector('.btn-danger').click()
    Reload Page
    Click Element    css:[data-test="nav-menu"]
    Wait Until Element Is Visible    css:[data-test="nav-sign-out"]
    Click Element    css:[data-test="nav-sign-out"]

#COMMAND TO TUN THIS - robot -d results robot_tests/test_csv_driven.robot