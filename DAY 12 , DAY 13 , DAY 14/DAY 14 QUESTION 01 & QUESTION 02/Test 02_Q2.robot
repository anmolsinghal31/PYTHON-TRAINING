*** Settings ***
Library           RequestsLibrary
Suite Setup       Create Session    mysession    ${baseurl}
Suite Teardown    Delete All Sessions

*** Variables ***
${baseurl}        http://127.0.0.1:5000

*** Keywords ***
# 4. Use of User Defined Keywords
Create And Validate User
    [Arguments]    ${username}
    ${data}=    Create Dictionary    name=${username}
    ${response}=    POST On Session    mysession    /users    json=${data}
    Status Should Be    201    ${response}
    Log To Console    Successfully created user: ${response.json()['name']}
    RETURN    ${response}

*** Test Cases ***
Scenario: Add Multiple Users Using Keywords
    [Tags]    Regression
    Create And Validate User    Alice
    Create And Validate User    Bob
    Create And Validate User    Charlie