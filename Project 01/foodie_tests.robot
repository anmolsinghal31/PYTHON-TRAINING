*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Check Restaurant API
    Create Session    mysess    http://127.0.0.1:5000
    &{body}=    Create Dictionary    name=Dominos    location=Mumbai
    ${res}=    POST On Session    mysess    /api/v1/restaurants    json=${body}
    Should Be Equal As Strings    ${res.status_code}    201

Check User Registration
    Create Session    mysess    http://127.0.0.1:5000
    &{user}=    Create Dictionary    username=john_doe    email=john@email.com
    ${res}=    POST On Session    mysess    /api/v1/users    json=${user}
    Should Be Equal As Strings    ${res.status_code}    201

# robot --timestampoutputs --outputdir Reports foodie_tests.robot