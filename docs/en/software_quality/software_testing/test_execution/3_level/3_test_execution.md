# Level 3

## Table of Contents: Test Execution

- [Preparing for Test Execution](#preparing-for-test-execution)
- [Executing Test Cases](#executing-test-cases)
- [Expected and Actual Results](#expected-and-actual-results)
- [Test Execution Statuses](#test-execution-statuses)
- [Test Evidence and Execution Records](#test-evidence-and-execution-records)
- [Handling Failed and Blocked Tests](#handling-failed-and-blocked-tests)


## Test Execution

Test execution is the process of running test cases against the system and comparing the **actual results** with the **expected results**.

At this stage, everything prepared earlier comes together. Test scenarios define what should be tested, test cases provide structure and test data supplies the inputs. Execution is where the system behavior is observed and validated.

During execution, each test case is run under defined conditions, and the outcome is recorded. The purpose is to determine whether the system behaves as expected or if any deviations occur.

To keep execution organized, results are documented in a structured way. Traditionally, this is done using a test execution table, sometimes referred to as a test results table.

This structure typically includes a reference to the **Test Case ID**, allowing each result to be linked back to what was designed. In cases where scenarios are used, a **Scenario ID** may also be included to maintain a connection to higher-level context.

Execution records usually capture the **execution date**, which helps track when testing was performed. In manual testing, the **tester name** may also be recorded, while in automated testing this is often replaced by system-generated logs.

The most important part of execution is the **actual result**, which represents what the system did during the test. This is compared against the expected outcome defined in the test case.

Based on this comparison, a **status** is assigned. A test may be marked as `Pass` when the behavior matches expectations, `Fail` when there is a deviation or `Blocked` when the test cannot be executed due to an issue such as missing data or environment problems and also exits `Not Run` the test was planned but not yet executed.

When a test fails, the tester records **defect information** including steps to reproduce, actual vs. expected behavior and environment details. This information is passed to the development team for investigation and fix. Once a fix is deployed, the test is **re-executed** to confirm the issue is resolved this is called **confirmation testing** or **re-testing**.

Additional **comments** may also be recorded to provide context for any result, including observations about environment stability, data issues, or test script problems.

In modern testing practices, particularly in automated environments, this information is captured automatically through tools rather than manually maintained tables. Test execution results may be stored in test management systems, CI/CD pipelines, or reporting dashboards.

However, the underlying concept remains the same. Each test execution must clearly show what was tested, what happened, and whether the system behaved as expected.

This ensures that testing results are reliable, traceable, and useful for evaluating system quality.