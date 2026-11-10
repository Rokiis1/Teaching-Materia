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

Test your understanding of the key concepts covered in both levels. Select one answer for each question to receive feedback and an explanation.

<div class="knowledge-check">

<div class="knowledge-question" data-answer="B" data-explanation="The System Under Test is the software or system being evaluated. Its boundaries depend on the testing scope, and external dependencies may still influence its behavior.">

<p><strong>System Under Test</strong></p>

<p>What determines which components belong to the System Under Test?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. The number of developers working on the application</button>
<button type="button" data-option="B">B. The testing scope and purpose of the evaluation</button>
<button type="button" data-option="C">C. Whether the software has already been released</button>
<button type="button" data-option="D">D. The programming language used</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="Testing can reveal defects and provide evidence about quality, but it cannot prove that software is completely free of defects.">

<p><strong>Principles of Testing</strong></p>

<p>Which statement correctly reflects a fundamental testing principle?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Successful testing proves that no defects remain</button>
<button type="button" data-option="B">B. Every possible input and condition must be tested</button>
<button type="button" data-option="C">C. Testing can show the presence of defects but not prove their absence</button>
<button type="button" data-option="D">D. The same testing approach is suitable for every project</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="A" data-explanation="The pesticide paradox highlights that repeatedly using unchanged tests may become less effective at revealing new defects. Reviewing and updating tests helps address this limitation.">

<p><strong>Pesticide Paradox</strong></p>

<p>Why should existing tests be reviewed and updated?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Repeatedly using unchanged tests may fail to reveal new kinds of defects</button>
<button type="button" data-option="B">B. Every test becomes invalid after its first execution</button>
<button type="button" data-option="C">C. Updating tests guarantees complete coverage</button>
<button type="button" data-option="D">D. Tests should always be replaced rather than maintained</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="D" data-explanation="Test roles describe groups of responsibilities rather than fixed job titles. One person may perform responsibilities from both the test management role and the testing role.">

<p><strong>Test Roles and Responsibilities</strong></p>

<p>Which statement about testing roles is correct?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Test management and testing must always be performed by different people</button>
<button type="button" data-option="B">B. Only employees with the job title tester can perform testing activities</button>
<button type="button" data-option="C">C. Testing roles are identical in every organization</button>
<button type="button" data-option="D">D. One person may perform responsibilities from both principal testing roles</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="B" data-explanation="Test analysis identifies what needs to be tested by examining the test basis and identifying test conditions. Test design then develops those conditions into test cases.">

<p><strong>Test Process and Activities</strong></p>

<p>Which testing activity primarily answers the question "What should be tested?"</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Test execution</button>
<button type="button" data-option="B">B. Test analysis</button>
<button type="button" data-option="C">C. Test completion</button>
<button type="button" data-option="D">D. Test implementation</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="Testware supports testing activities, while deliverables are agreed outputs provided or communicated to stakeholders. The same work product may serve both purposes.">

<p><strong>Testware and Deliverables</strong></p>

<p>Which statement correctly distinguishes testware from deliverables?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Testware consists only of automated test scripts</button>
<button type="button" data-option="B">B. Deliverables can never be used during testing</button>
<button type="button" data-option="C">C. A test plan can be both testware and a deliverable</button>
<button type="button" data-option="D">D. Testware and deliverables must always be separate documents</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="A" data-explanation="Independent testing can introduce different perspectives and challenge assumptions, but greater independence does not automatically improve testing effectiveness.">

<p><strong>Independence of Testing</strong></p>

<p>What is an important consideration when deciding the level of testing independence?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Independence should be balanced with collaboration and project needs</button>
<button type="button" data-option="B">B. External testing is always more effective than internal testing</button>
<button type="button" data-option="C">C. Developers should never test their own work</button>
<button type="button" data-option="D">D. Independence eliminates the need for communication</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="D" data-explanation="The whole team approach encourages everyone to contribute to quality using their different skills and responsibilities. It does not require everyone to perform identical tasks.">

<p><strong>Whole Team Approach</strong></p>

<p>What does the whole team approach emphasize?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Testers are solely responsible for software quality</button>
<button type="button" data-option="B">B. Every team member must perform the same testing tasks</button>
<button type="button" data-option="C">C. Independent testing must be eliminated</button>
<button type="button" data-option="D">D. Quality is a shared responsibility supported by collaboration</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="B" data-explanation="Testability influences how easily testers can establish conditions, control states, observe behavior, and investigate failures. It does not guarantee that the software is correct.">

<p><strong>Testability</strong></p>

<p>Which characteristic indicates better software testability?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Testers cannot control relevant system states</button>
<button type="button" data-option="B">B. Testers can establish conditions and observe behavior easily</button>
<button type="button" data-option="C">C. Failures provide no diagnostic information</button>
<button type="button" data-option="D">D. Components can only be tested through unavailable external services</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

<div class="knowledge-question" data-answer="C" data-explanation="A test oracle provides a basis for establishing expected results and evaluating actual results. When an exact expected value is unknown, testers may use known properties or constraints.">

<p><strong>Test Oracles</strong></p>

<p>What can testers do when the exact expected result of a complex calculation is unknown?</p>

<div class="quiz-options">
<button type="button" data-option="A">A. Assume that the software's output is correct</button>
<button type="button" data-option="B">B. Skip evaluating the result entirely</button>
<button type="button" data-option="C">C. Evaluate known properties, constraints, or relationships</button>
<button type="button" data-option="D">D. Treat every result as a confirmed defect</button>
</div>

<p class="quiz-feedback" role="status" aria-live="polite"></p>

</div>

</div>
