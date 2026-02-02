*** Test Cases ***
Print Names using for loop
    FOR    ${name}    IN    Ram  Ravi  Taj
        log to console    ${name}
    END

Print Numbers Using While Loop
    ${count}=    Set Variable    1
    WHILE    ${count} <= 5
        Log To Console    ${count}
        ${count}=    Evaluate    ${count} + 1
    END