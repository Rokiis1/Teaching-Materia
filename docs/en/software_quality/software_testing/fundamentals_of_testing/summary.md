# Summary

This summary brings together the key concepts from the **Fundamentals of Testing** module. It provides a concise reference for reviewing how testing is scoped, organized, performed, and evaluated. The material is divided into **Level 1**, which establishes the foundations of testing, and **Level 2**, which introduces testability and test oracles.

## Table of Contents: Fundamentals of Testing Summary

- [Fundamentals of Testing Level 1](#fundamentals-of-testing-level-1)
- [Fundamentals of Testing Level 2](#fundamentals-of-testing-level-2)
- [Knowledge Check](#knowledge-check)

## Fundamentals of Testing Level 1

Level 1 explains how teams determine **what to test**, **why testing is performed**, **how testing activities are organized**, and **who contributes to testing**. The **System Under Test (SUT)** is the software or system being evaluated, whether an individual function, component, service, application, or complete system. Its boundaries depend on the **testing scope**, and components outside those boundaries may still influence its behavior through interactions and dependencies.

**Test objectives** describe what testing is intended to achieve, including evaluating work products, helping prevent defects, triggering failures, identifying defects, achieving specified coverage, reducing risk, assessing requirements, and supporting decisions about product quality and readiness. These objectives are guided by **seven fundamental testing principles** that explain the value and limitations of testing.

| Testing principle                                              | Explanation                                                                                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Testing shows the presence of defects, not their absence**   | Testing can reveal problems, but finding no defects does not prove that software is defect-free.                                |
| **Exhaustive testing is impossible**                           | Testing every possible condition is generally impractical, so teams must prioritize their efforts.                              |
| **Early testing saves time and effort**                        | Identifying problems in requirements, designs, and other early work products can reduce later correction costs.                 |
| **Defect clustering**                                          | A relatively small number of components may contain a large proportion of discovered defects.                                   |
| **Pesticide paradox**                                          | Repeatedly using unchanged tests may become less effective at discovering new defects, so tests should be reviewed and updated. |
| **Testing is context dependent**                               | Testing approaches must reflect the product, risks, requirements, and project circumstances.                                    |
| **Absence of errors is a fallacy**                             | Software with few known defects may still fail to satisfy user needs or achieve its intended purpose.                           |

These principles are **guidelines rather than sequential steps**, and several may influence the same testing decision. Applying them involves different **test roles**, which describe responsibilities rather than fixed job titles. The **test management role** focuses primarily on planning, monitoring, controlling, coordinating, and completing testing, while the **testing role** focuses primarily on test analysis, design, implementation, and execution. One person may perform both roles, or responsibilities may be distributed across a team. These responsibilities are carried out through the **test process**, which consists of seven interconnected activities that organize testing work and support the achievement of testing objectives.

| Activity                        | Purpose                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Test planning**               | Establish objectives, scope, priorities, resources, and the testing approach.                                 |
| **Test monitoring and control** | Evaluate progress and make adjustments when necessary.                                                        |
| **Test analysis**               | Identify what needs to be tested by examining the test basis.                                                 |
| **Test design**                 | Develop test cases, expected results, and coverage considerations.                                            |
| **Test implementation**         | Prepare test procedures, suites, data, environments, and automated tests where appropriate.                   |
| **Test execution**              | Run tests, compare actual and expected results, investigate unexpected behavior, and report defects.          |
| **Test completion**             | Evaluate completion criteria, communicate results, preserve useful materials, and record lessons learned.     |

These activities are **not strictly linear** because they may overlap, repeat, and influence one another as testing progresses. Throughout the process, teams create and use **work products** that support testing and communication. **Testware** includes materials such as test plans, test conditions, test cases, test procedures, test suites, test data, scripts, results, and defect reports. **Deliverables** are agreed outputs that must be provided or communicated to stakeholders. A work product, such as a test plan, may serve as both testware and a deliverable.

**Independence of testing** describes the degree of separation between those performing testing and those creating the work product being tested. Testing may be performed by the author, a peer, a separate team within the organization, or an external organization. Greater independence can provide different perspectives and challenge assumptions, but it does not automatically guarantee more effective testing. The appropriate level depends on project context, risks, and other requirements.

At the same time, the **whole team approach** treats quality as a shared responsibility. Developers contribute technical knowledge, testers contribute testing expertise and risk awareness, and business representatives contribute knowledge of user needs and expected behavior. This collaboration supports early feedback, knowledge sharing, and better decisions without requiring everyone to perform identical responsibilities or eliminating the need for independent testing.

## Fundamentals of Testing Level 2

Level 2 introduces two closely related concepts, **testability** and **test oracles**. **Testability** describes how easily and effectively software can be tested. Good testability allows testers to establish test conditions, control relevant system states, observe behavior, reproduce failures, and investigate problems with less effort. It is influenced by characteristics such as controllability, observability, component isolation, and the availability of useful diagnostic information. **Test doubles** can replace real dependencies with controlled substitutes, allowing components to be tested under specific conditions. Improving testability is a **shared responsibility**. Developers can provide clear interfaces and mechanisms for controlling and observing behavior, testers can identify testing obstacles, and business representatives can clarify expected behavior and acceptance criteria. However, **good testability does not guarantee correctness**, because software may be easy to test and still contain defects.

A **test oracle** is a source of information used to establish expected results and evaluate actual results. Test oracles may come from **requirements**, **specifications**, **acceptance criteria**, **business rules**, **existing systems**, **reference implementations**, or **domain knowledge**. Knowledgeable stakeholders and subject matter experts may also help clarify expected behavior. The **test oracle problem** occurs when determining the correct expected result is difficult or impossible, as may happen with complex calculations that cannot easily be verified independently. In such situations, testers may evaluate known properties, constraints, or relationships instead of relying on an exact expected value. The **reliability of a test oracle** is important because incorrect or incomplete expected results can make correctly functioning software appear defective or allow actual defects to go unnoticed.

**Testability and test oracles complement each other**. Testability influences how easily testers can establish conditions and observe software behavior, while test oracles provide the basis for evaluating that behavior. Together, they help testers design meaningful tests, interpret results reliably, and communicate their findings.

## Knowledge Check

Test your understanding of the key concepts covered in Fundamentals of Testing. Select one answer for each question to receive feedback and an explanation.

<div class="knowledge-check">

<div class="knowledge-question" data-answer="B" data-explanation="The System Under Test is defined by the testing scope and objectives. Its boundaries determine which components are being evaluated, even when external dependencies influence their behavior.">

<p><strong>System Under Test</strong></p>

<p>When testing an application that communicates with external services, how should the System Under Test be defined?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Include every service that exchanges data with the application</button>
<button type="button" data-option="B">B. Identify the components included in the agreed testing scope</button>
<button type="button" data-option="C">C. Include only components developed by the internal team</button>
<button type="button" data-option="D">D. Identify the components deployed in the same environment</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="Testing provides evidence about software behavior and can reveal defects, but passing tests do not establish that defects are absent.">

<p><strong>Principles of Testing</strong></p>

<p>A team has executed all planned tests without observing a failure. Which conclusion is justified?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. The application meets all possible user expectations</button>
<button type="button" data-option="B">B. The application contains no remaining implementation defects</button>
<button type="button" data-option="C">C. The tested conditions revealed no observed failures</button>
<button type="button" data-option="D">D. The testing process has covered every relevant condition</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="A" data-explanation="The pesticide paradox describes how repeatedly executing unchanged tests may become less effective at finding new defects. Tests should be reviewed and adapted as risks and software behavior change.">

<p><strong>Pesticide Paradox</strong></p>

<p>A regression suite continues to pass, but users report defects in recently changed workflows. What is the most appropriate response?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Review the suite and add tests for newly identified risks</button>
<button type="button" data-option="B">B. Execute the existing suite more frequently without modifying it</button>
<button type="button" data-option="C">C. Replace the regression suite with tests of unchanged features</button>
<button type="button" data-option="D">D. Increase test execution speed while retaining the same conditions</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="D" data-explanation="Test management and testing are groups of responsibilities rather than fixed job titles. Depending on the project, one person may perform activities from both roles.">

<p><strong>Test Roles and Responsibilities</strong></p>

<p>In a small project, a tester plans testing activities, executes tests, and reports results. How should these responsibilities be understood?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Planning activities belong to development rather than testing roles</button>
<button type="button" data-option="B">B. Executing tests transfers responsibility for managing the test process</button>
<button type="button" data-option="C">C. Reporting results requires a separate person responsible for management</button>
<button type="button" data-option="D">D. One person can perform both test management and testing responsibilities</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="B" data-explanation="Test analysis examines the test basis to identify test conditions and determine what needs to be tested. Test design develops these conditions into test cases.">

<p><strong>Test Process and Activities</strong></p>

<p>A tester reviews requirements to identify which behaviors and conditions need verification. Which test activity is being performed?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Test implementation, preparing procedures and execution resources</button>
<button type="button" data-option="B">B. Test analysis, identifying test conditions from the test basis</button>
<button type="button" data-option="C">C. Test design, developing test cases from identified conditions</button>
<button type="button" data-option="D">D. Test execution, comparing observed results with expected behavior</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="Testware consists of work products created or used during testing. Deliverables are outputs provided to stakeholders. A test plan may be both testware and an agreed deliverable.">

<p><strong>Testware and Deliverables</strong></p>

<p>A test plan is used by the testing team and submitted to stakeholders as an agreed project output. How should it be classified?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. As testware only, because the testing team uses it</button>
<button type="button" data-option="B">B. As a deliverable only, because stakeholders receive it</button>
<button type="button" data-option="C">C. As both testware and a deliverable in this context</button>
<button type="button" data-option="D">D. As neither, because it does not contain executable tests</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="A" data-explanation="Testing independence can provide different perspectives and reduce shared assumptions, but its benefits should be balanced against collaboration, communication, and project needs.">

<p><strong>Independence of Testing</strong></p>

<p>A project is deciding whether developers or an independent team should perform certain tests. Which consideration is most appropriate?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Balance independent perspectives with collaboration and project needs</button>
<button type="button" data-option="B">B. Prefer external testers because organizational separation ensures effectiveness</button>
<button type="button" data-option="C">C. Assign testing to developers because implementation knowledge prevents bias</button>
<button type="button" data-option="D">D. Separate testers from developers to avoid influencing test decisions</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="D" data-explanation="The whole team approach encourages collaboration and shared responsibility for quality. Team members contribute through their different skills and roles rather than performing identical testing activities.">

<p><strong>Whole Team Approach</strong></p>

<p>How should a team apply the whole team approach when planning quality-related activities?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Assign final quality responsibility to the dedicated testing specialists</button>
<button type="button" data-option="B">B. Rotate all testing tasks equally among team members each iteration</button>
<button type="button" data-option="C">C. Let developers manage quality while testers independently verify releases</button>
<button type="button" data-option="D">D. Share responsibility for quality while contributing through different roles</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="B" data-explanation="Testability improves when testers can establish relevant conditions, control system states, observe outcomes, and investigate failures. These capabilities make testing more effective without guaranteeing correctness.">

<p><strong>Testability</strong></p>

<p>Which change would most directly improve the testability of an application?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Reduce the number of supported user workflows in the application</button>
<button type="button" data-option="B">B. Provide ways to control test states and observe system behavior</button>
<button type="button" data-option="C">C. Increase the number of features included in each test scenario</button>
<button type="button" data-option="D">D. Restrict diagnostic information to the production support team</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="When an exact expected result is unavailable, a test oracle may use known properties, constraints, or relationships to evaluate whether the observed result is acceptable.">

<p><strong>Test Oracles</strong></p>

<p>A complex calculation produces an output whose exact expected value is difficult to determine. How can the tester evaluate the result?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Compare the result with previous outputs from the same implementation</button>
<button type="button" data-option="B">B. Accept the result when the calculation finishes without an error</button>
<button type="button" data-option="C">C. Check the result against known mathematical properties and constraints</button>
<button type="button" data-option="D">D. Repeat the calculation and accept the result when outputs agree</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

</div>
