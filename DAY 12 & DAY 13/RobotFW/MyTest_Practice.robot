*** Variables ***
@{COLORS}    Red    Green    Blue
@{USERS}     admin    user
@{PWDS}      admin123    user123

*** Test Cases ***
1. IF condition (basic)
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log To Console    Eligible to vote
    END

2. IF – ELSE
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END

3. IF – ELSE IF – ELSE
    ${marks}=    Set Variable    75
    IF    ${marks} >= 90
        Log To Console    Grade A
    ELSE IF    ${marks} >= 75
        Log To Console    Grade B
    ELSE
        Log To Console    Grade C
    END

4. Inline IF
    ${status}=    Set Variable    PASS
    IF    '${status}' == 'PASS'    Log To Console    Test Passed

5. FOR loop (basic list)
    FOR    ${item}    IN    one    two    three
        Log To Console    Item: ${item}
    END

6. FOR loop with list variable
    FOR    ${color}    IN    @{COLORS}
        Log To Console    Color: ${color}
    END

7. FOR loop – IN RANGE
    FOR    ${i}    IN RANGE    1    6
        Log To Console    Number: ${i}
    END

8. FOR loop – with step
    FOR    ${i}    IN RANGE    0    10    2
        Log To Console    Value: ${i}
    END

9. FOR loop – ENUMERATE
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    ${index} = ${value}
    END

10. FOR loop – ZIP
    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PWDS}
        Log To Console    User: ${u} Password: ${p}
    END

11. Nested FOR loop
    FOR    ${i}    IN RANGE    1    3
        FOR    ${j}    IN RANGE    1    3
            Log To Console    i=${i}, j=${j}
        END
    END

12. FOR loop with IF condition
    FOR    ${n}    IN RANGE    1    6
        IF    ${n} == 3
            Log To Console    Found number 3
        END
    END

13. BREAK
    FOR    ${i}    IN RANGE    1    10
        IF    ${i} == 5
            BREAK
        END
        Log To Console    ${i}
    END

14. CONTINUE
    FOR    ${i}    IN RANGE    1    6
        IF    ${i} == 3
            CONTINUE
        END
        Log To Console    ${i}
    END

15. WHILE loop
    ${i}=    Set Variable    1
    WHILE    ${i} <= 5
        Log To Console    Value: ${i}
        ${i}=    Evaluate    ${i} + 1
    END

16. WHILE with BREAK
    ${i}=    Set Variable    1
    WHILE    True
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}=    Evaluate    ${i} + 1
    END

17. TRY / EXCEPT / FINALLY
    TRY
        Log To Console    Attempting operation
        Fail    Intentional Failure
    EXCEPT
        Log To Console    Error caught successfully
    FINALLY
        Log To Console    Cleaning up...
    END

18. Run Keyword If
    ${status}=    Set Variable    PASS
    Run Keyword If    '${status}' == 'PASS'    Log To Console    Executed via Run Keyword If

19. Run Keyword Unless
    ${status}=    Set Variable    FAIL
    Run Keyword Unless    '${status}' == 'PASS'    Log To Console    Executed via Run Keyword Unless