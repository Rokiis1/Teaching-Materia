# Level 2

## Table of Contents: Test Execution

- [When to Use Manual Test Execution](#when-to-use-manual-test-execution)
- [When to Use Automated Test Execution](#when-to-use-automated-test-execution)
- [Limitations of Manual and Automated Test Execution](#limitations-of-manual-and-automated-test-execution)
- [Selecting and Combining Test Execution Approaches](#selecting-and-combining-test-execution-approaches)

**Test Execution Level 2** examines how to select an appropriate execution approach for a testing objective. It explores the circumstances that favor **manual or automated test execution**, the limitations of both approaches, and the considerations involved in selecting and combining them. Practical examples demonstrate how product risks, technical constraints, costs, and available resources influence these decisions. The chapter begins by examining when **manual test execution** is an appropriate choice.

## When to Use Manual Test Execution

**Manual test execution** is appropriate when the testing objective requires investigation, adaptation, or **contextual judgment**. It is particularly useful when the tester needs to interpret unexpected behavior or use observations to decide what to examine next, rather than rely entirely on predefined actions and checks. The tester may use supporting tools, such as an API client or browser developer tools, while retaining control of the actions and evaluation. The choice of approach therefore depends on what needs to be established, not simply on the feature, type of testing, or tools involved.

When examining **new or changing functionality**, testers may encounter behavior that is not yet fully understood or covered by predefined checks. Manual execution allows them to vary inputs and follow emerging evidence, drawing on **experience-based testing techniques** to identify likely failure conditions or guide further investigation. These techniques are explored in [Experience-Based Testing Techniques](../../test_case_design/experience_based_testing_techniques/experience_based_testing_techniques.md), while [Build and Change-Related Testing](../../types_of_testing/dynamic_testing/functional_testing/build_and_change_related_testing.md) covers the broader activities used to assess builds and changes. Neither the technique nor the software change alone determines whether execution should be manual or automated.

!!! example "Investigating an unexpected checkout failure"

    An online shopping application displays an unexpected payment error during checkout. To identify the circumstances in which it occurs, the tester attempts to reproduce the failure with the original inputs, compares it with a successful checkout, and varies relevant conditions, such as the payment method or basket contents.

    If the error occurs only when a discount is applied, that observation guides the tester toward the relationship between the discount, order total, and payment request. Manual execution is appropriate because the investigation develops in response to the evidence, while automated checks may help reproduce the failure or compare inputs once useful conditions have been identified.

Manual execution can also support the evaluation of **software quality attributes** when predefined checks do not provide sufficient evidence for the testing objective. A tester may assess whether an error message is understandable, investigate a keyboard navigation problem, or examine unexpected behavior in a supported browser. Such evaluation can complement automated checks by investigating concerns that those checks do not fully address. The relevant attributes and evaluation approaches are explored in [Quality Attributes and Evaluation](../../software_quality/quality_attributes_and_evaluation/index.md).

Practical constraints may also make manual execution appropriate when a test must be performed promptly and suitable automation is not available. This does not establish a permanent preference for manual testing; the approach should be reconsidered as the objective and circumstances change. The next section examines when **automated test execution** can provide greater value.

## When to Use Automated Test Execution

**Automated test execution** is appropriate when test actions can be implemented reliably and actual results can be evaluated against defined expectations. It is particularly useful when tests must be repeated frequently, executed at scale, performed across multiple configurations, or completed within a required **feedback time**. Testers weigh these benefits against the stability of the expected behavior, the availability of suitable test data and environments, and the effort of creating and maintaining the automation. Automated checks may use **assertions** to verify that an observed result satisfies an expected condition or apply evaluation criteria to collected measurements.

Tests of established behavior that must be repeated after software changes are often strong automation candidates. Selected [regression tests](../../types_of_testing/dynamic_testing/functional_testing/build_and_change_related_testing.md#regression-testing), for example, can provide timely feedback about unintended effects on existing functionality.

!!! example "Verifying a checkout calculation after each build"

    An online shopping application applies a 10% discount to eligible items. To verify this established rule after each relevant build, an automated test prepares a basket containing €100.00 of eligible items, applies a valid discount, and asserts that the calculated total is €90.00, with no other charges applied.

    The precise expected result, reproducible starting conditions, and frequent execution make this a strong automation candidate.

Automation can also support the evaluation of **software quality attributes** when the objective requires controlled workloads, repeated measurements, or checks against defined criteria. Performance tests may measure response times under concurrent requests, security tests may verify that an API rejects unauthorized requests, and reliability tests may examine failures or recovery behavior over repeated executions. These tests can collect evidence at a scale or precision that would be difficult to achieve manually, although their results remain limited to the conditions and criteria evaluated. The relevant attributes and evaluation approaches are explored in [Quality Attributes and Evaluation](../../software_quality/quality_attributes_and_evaluation/index.md).

Teams may use specialized testing tools or executable scripts to perform test actions, collect observations, and evaluate results. For example, an automated API test may create, retrieve, and update a resource, checking the responses and resulting state at each stage. Once implemented, the test can be reused across **multiple environments or configurations** where suitable starting conditions and test data are available, or integrated into a **continuous integration and continuous delivery (CI/CD)** pipeline to provide feedback at the required stage of delivery. A pipeline may run fast, reliable checks after each build and schedule more extensive tests for later stages, coordinating execution and reporting while leaving the evaluation of results to the criteria defined for each test. The integration of automated testing and quality feedback into delivery pipelines is explored further in **Quality Engineering on Continuous Testing and CI/CD**.

These applications illustrate where automation can provide value, but technical feasibility alone does not make a test worth automating. The next section examines the limitations of manual and automated execution and how they influence the choice of approach.

## Limitations of Manual and Automated Test Execution

Both **manual and automated test execution** have limitations that can affect the reliability, coverage, cost, and timeliness of testing. Both approaches depend on suitable test conditions, expected results, test data, and environments. Manual execution also depends on the tester's available time, attention, and judgment, while automated execution depends on the correctness and scope of the implemented actions and checks. Understanding these limitations helps testers recognize what the available results establish and where additional testing may be needed.

**Manual execution** can become time-consuming when the same checks must be repeated frequently, performed with many combinations of inputs, or executed across numerous configurations. Repetitive work can also increase the risk of overlooking a step or recording a result inconsistently. Clear test instructions and records can improve repeatability, but they do not remove the effort required for each execution. When an investigation is less structured, testers may also find it difficult to demonstrate exactly what was covered unless they record their actions and observations.

**Automated execution** can repeat implemented actions and checks consistently, but consistency does not guarantee that a check is correct or sufficient. An automated test may pass even when the application has a defect because its assertions do not examine the affected behavior or rely on an incorrect expectation. A failure may instead result from unsuitable test data, an unavailable dependency, or a defect in the automation itself. Automated tests may also produce inconsistent outcomes under apparently unchanged conditions, a problem commonly described as **flaky tests**. Such results reduce confidence in automated feedback and require investigation to determine whether the cause lies in the application, automation, or execution conditions. Automated checks must therefore be reviewed and maintained as the software and its requirements evolve.

!!! example "A checkout validation check passes"

    An automated check submits a checkout form without a required delivery address and verifies that a validation message appears. The check passes, but a tester notices that the message is displayed below the visible area and does not explain which field needs attention.

    The automated result is valid for the condition it checked, but it does not establish that the customer can understand and recover from the error. Manual evaluation can investigate that concern, while additional automated checks may be appropriate for specific, measurable requirements identified during the investigation.

Automation may also be **technically possible but uneconomical**. A rarely executed check may cost more to implement than it saves, while frequently changing requirements can create repeated maintenance work. For example, a team may need to update user interface locators, revise test data setup, or change API checks as the application evolves. Conversely, a one-time test may still justify automation if its scale, precision, or timing makes manual execution impractical. The decision should reflect the testing objective and expected benefit rather than execution frequency alone.

Specialized visual or accessibility tools can check additional conditions, but their results may still need human evaluation. System constraints can also limit automated execution. For example, a security control such as **CAPTCHA** is designed to restrict automated interaction. Automated tests of the surrounding workflow may use an approved test configuration or a provider-supported testing mechanism. However, results obtained through that configuration do not establish that the CAPTCHA control itself works correctly, which requires separate evaluation against its security requirements.

These limitations do not make either approach unsuitable in general. They identify where a test may need a different execution method, supporting tools, or complementary checks. The next section applies these considerations when selecting and combining manual and automated execution for a set of testing objectives.

## Selecting and Combining Test Execution Approaches

An execution approach should be selected for the **testing objective** rather than assigned automatically to an entire feature or test suite. A team may use manual execution for one objective, automated execution for another, and a combination of both where different forms of evidence are needed.

!!! example "Selecting execution approaches for checkout testing"

    A team is preparing a release that changes how discounts are applied during checkout. It needs to verify the calculation, investigate a reported payment failure, and assess whether customers can recover from validation errors.

    The team selects **automated execution** for the established discount calculation because it has precise expected results, reproducible test data, and will be checked after relevant builds. It selects **manual execution** to investigate the payment failure because the tester must use each observation to decide which condition to examine next.

    For validation errors, the team **combines both approaches**. Automated checks verify that the required messages appear under defined conditions, while manual evaluation examines whether the messages are understandable and help customers correct their inputs. If the investigation identifies a repeatable defect with a clear expected result, the team may also add an automated regression check after the fix.

The selection should also reflect **product risks and project constraints**. In the checkout example, an incorrect discount calculation and a payment failure may both threaten the release, even though they require different execution approaches. When time or resources are limited, the team prioritizes the tests needed to evaluate these risks and considers whether the selected approaches can provide sufficiently reliable and timely evidence. Choosing an execution approach does not, by itself, establish that the required coverage has been achieved.

Execution choices should be reviewed as the software, product risks, and testing needs evolve. A check initially performed manually may become worth automating, while an automated check may need revision or removal if it no longer provides useful feedback. [Test Execution Level 3](../3_level/3_test_execution.md) develops the practical activities of performing tests, recording execution results, investigating unexpected outcomes, and preserving execution history when tests are run again.
