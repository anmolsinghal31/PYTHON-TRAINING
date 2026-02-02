*** Settings ***
Library           RequestsLibrary
Suite Setup       Create Session    mysession    ${baseurl}
Suite Teardown    Delete All Sessions
Test Setup        Log To Console    --- Starting Test Case ---
Test Teardown     Log To Console    --- Finished Test Case ---

*** Variables ***
${baseurl}        http://127.0.0.1:5000

*** Test Cases ***
Verify API Connectivity
    [Tags]    Sanity
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    Log To Console    API is up and running.

Create and Verify User
    [Tags]    Regression    SMOKE
    ${data}=    Create Dictionary    name=Anmol
    ${response}=    POST On Session    mysession    /users    json=${data}
    Status Should Be    201    ${response}
    Log To Console    User Created Successfully: ${response.json()}