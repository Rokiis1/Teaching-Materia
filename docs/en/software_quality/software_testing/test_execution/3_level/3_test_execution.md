# Level 3

## Table of Contents: Test Execution

- [Performing Test Execution](#performing-test-execution)
- [Recording Test Execution Results](#recording-test-execution-results)
- [Investigating Unexpected Results](#investigating-unexpected-results)
- [Re-executing Tests and Preserving Execution History](#re-executing-tests-and-preserving-execution-history)

**Test Execution Level 3** follows the practical work of executing a test, recording its outcome, investigating an unexpected result, and performing the test again when needed. A connected checkout example demonstrates how observations become evidence and inform subsequent actions, beginning with the conditions and checks involved in **performing test execution**.

## Performing Test Execution

Test execution begins by identifying the test case or objective, confirming that its instructions and expected results apply to the selected software build and configuration, and establishing the required starting state, test data, environment, and dependencies. If a prerequisite is unavailable, the tester determines whether the intended evaluation can proceed. Once the conditions are established, execution involves performing the actions and evaluating observations at the relevant **verification points**. During manual execution, the tester controls the actions and evaluation, using supporting tools where appropriate. Automated execution instead requires the appropriate configuration and data, followed by a review of the reported checks and errors, since an automated execution can finish normally while reporting failed assertions.

If execution is interrupted or a check fails, the decision to continue depends on whether further actions will provide useful evidence. Independent checks may continue when the test objective and agreed execution rules permit, while dependent checks that cannot be performed are identified as unperformed rather than independently failed.

!!! example "Executing the checkout discount test"

    A tester executes **TC-DISC-01**, the checkout discount calculation test case, against **Build A**. The prepared basket contains €100.00 of eligible items, a valid 10% discount, and no other charges. At the calculation verification point, the expected total is €90.00, but the application returns €95.00. The calculation response is saved as evidence of the observed result.

This observation and its supporting evidence provide the basis for determining and recording the outcome. The next section explains how **recording test execution results** associates that outcome with the test and the conditions under which it was performed.

## Recording Test Execution Results

After execution, the outcome is recorded in the **Test Execution Report**. The **Test Case ID** identifies the documented test case that was executed; when no documented test case was used, the entry identifies the test condition or objective evaluated instead. If the project maintains documented test scenarios, the related **Scenario ID** may also be included or obtained through the referenced test case. Other traceability references, such as associated requirements or test conditions, do not need to be repeated in the report unless the project requires them.

The entry records the actual result, execution status, date, tester or automated job, and relevant evidence, together with enough information to identify the particular execution and its conditions. The build and environment may be recorded directly or through a linked execution record, while the expected result may remain in the referenced test case if its applicable version is identifiable. Supporting evidence should demonstrate the observation without exposing credentials or sensitive customer data. The relationships between results and other testware are explored in [Requirements Traceability](../../test_managment/3_level/3_level_test_managment.md#requirements-traceability).

!!! example "Recording the checkout discount execution"

    The execution of **TC-DISC-01** against **Build A** is recorded as **RUN-001**. The linked execution record identifies the checkout test environment and contains the saved calculation response. The date and tester below are placeholders.

    | Execution ID | Test Case ID | Execution Date | Tester            | Actual Result            | Execution Status | Comments / Defects                           |
    |--------------|--------------|----------------|-------------------|--------------------------|------------------|----------------------------------------------|
    | RUN-001      | TC-DISC-01   | YYYY-MM-DD     | Tester identifier | €95.00 instead of €90.00 | Failed           | Saved calculation response linked to RUN-001 |

The failed result and its supporting evidence identify a specific execution for further examination. The next section explains how to **investigate unexpected results**.

## Investigating Unexpected Results

Investigation begins with the execution record and a check that the expected result was appropriate, using the referenced test case and relevant requirement, specification, or business rule where necessary. An incorrect or unclear expectation requires clarification or correction without changing the original observation. If the expectation remains valid, the investigation turns to plausible explanations for the discrepancy, such as the test data, starting conditions, dependencies, automated test actions or assertions, and application responses or logs. A separate reproduction execution can establish whether the result recurs under the same conditions, while varying a relevant condition can help narrow the circumstances in which it occurs. An unsuccessful reproduction attempt does not invalidate the original observation or establish that the problem is resolved.

!!! example "Investigating the checkout discount discrepancy"

    A review of **RUN-001**, the failed execution of **TC-DISC-01** on Build A, confirms that the 10% discount rule applied, the items were eligible, and no other calculation rules affected the total. The saved response also confirms that the application returned €95.00. Re-executing TC-DISC-01 on Build A under the same relevant conditions produces €95.00 again. This reproduction is recorded as **RUN-002** with the status Failed and linked to RUN-001. The repeated result establishes reproducibility under those conditions, not the underlying cause, and supports creating or referencing a defect report for the suspected calculation defect.

When a missing prerequisite prevents the intended evaluation, the investigation focuses on that condition rather than assigning a failed result to a check that was not performed. The tester concludes the investigation with a supported finding or an unresolved question and an agreed next action. When that action requires another execution, such as checking a correction or testing after a condition has been restored, the next section explains how to **re-execute tests and preserve execution history**.

## Re-executing Tests and Preserving Execution History

Re-execution starts with a stated objective, a check of what has changed, and the conditions required for evaluation. The new outcome is recorded as a **separate execution** of the same test case or objective, identifying any revised test version and linking relevant earlier results. A later pass therefore does not overwrite an earlier failure or blocked result.

!!! example "Re-executing the checkout discount test after a correction"

    After a correction becomes available in **Build B**, **TC-DISC-01** is re-executed using the same relevant checkout conditions. The application returns the expected €90.00. The new execution is recorded as **RUN-003** with the status Passed, and the saved calculation response is linked to the related defect report. The execution history retains **RUN-001** and **RUN-002** as Failed on Build A alongside RUN-003 as Passed on Build B, providing evidence that the reported discrepancy was corrected under the tested conditions.

This re-execution completes **[confirmation testing](../../types_of_testing/dynamic_testing/functional_testing/build_and_change_related_testing.md)** of the reported discount defect while preserving the earlier execution results. The **[Test Execution Summary](../summary.md)** brings together the practices and concepts covered throughout the module.
