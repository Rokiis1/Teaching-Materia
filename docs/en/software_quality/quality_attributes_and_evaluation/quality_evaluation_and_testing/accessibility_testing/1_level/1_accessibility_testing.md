# Level 1

## Table of Contents: Accessibility Testing

- [Accessibility Barriers and User Needs](#accessibility-barriers-and-user-needs)
- [Web Content Accessibility Guidelines (WCAG)](#web-content-accessibility-guidelines-wcag)
- [WCAG Conformance Levels](#wcag-conformance-levels)
- [Accessibility Requirements and Scope](#accessibility-requirements-and-scope)

**Accessibility Testing Level 1** introduces common accessibility barriers and user needs before exploring the **Web Content Accessibility Guidelines (WCAG)**, including their four foundational principles and conformance levels. It then examines how applicable accessibility requirements are identified and how the scope of an evaluation is determined. Understanding these concepts begins with recognizing the barriers that people may encounter when interacting with software.

## Accessibility Barriers and User Needs

An **accessibility barrier** occurs when the design or implementation of a product makes information or functionality difficult or impossible to access for someone with particular needs. These barriers may affect people with permanent disabilities, temporary limitations, or situational difficulties, depending on how the product is used. Different users may encounter different barriers, and the same barrier can affect more than one group. The following examples illustrate common accessibility concerns.

| Area            | Example of an accessibility barrier                                                                | Potential user impact                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Visual**      | Important information is communicated only through color                                           | Users who cannot distinguish the colors may miss important information                           |
| **Auditory**    | A video contains spoken instructions without captions or an equivalent alternative                 | Users who cannot hear the audio may miss essential instructions                                  |
| **Motor**       | A form can only be completed using a mouse                                                         | Users who rely on a keyboard or alternative input device may be unable to complete the form      |
| **Cognitive**   | Instructions are unnecessarily complicated or error messages are unclear                           | Users may struggle to understand what to do or how to recover from mistakes                      |
| **Speech**      | An important function requires spoken commands without another input method                        | Users who cannot use speech input may be unable to access that function                          |
| **Vestibular**  | An interface uses excessive animation or unexpected motion without an appropriate way to reduce it | Users sensitive to motion may experience dizziness or discomfort                                 |

These categories illustrate different access needs but do not represent every disability or situation. Some users have multiple access needs, and accessibility should not be evaluated by assuming that everyone interacts with software in the same way. For example, consider an account registration form. A user who cannot operate a mouse may depend on keyboard navigation, while a screen reader user may need properly associated labels to understand each input field. Another user may need clear instructions and understandable validation messages to complete the same task. Although these users interact with the same feature, they may encounter different barriers.

**Assistive technologies** help people interact with software through alternative methods, including screen readers, screen magnifiers, voice control, and alternative input devices. However, these technologies depend on the software providing information and controls that can be interpreted and operated correctly. Understanding these interactions helps testers recognize potential barriers and identify relevant accessibility requirements. For web applications, established guidelines provide a consistent basis for evaluating those requirements.

## Web Content Accessibility Guidelines (WCAG)

The **Web Content Accessibility Guidelines (WCAG)** are internationally recognized guidelines developed by the **World Wide Web Consortium (W3C)** through its **Web Accessibility Initiative (WAI)**. They provide a framework for making web content more accessible to people with disabilities and help organizations define consistent accessibility expectations. For testers, WCAG provides a basis for evaluating web content against defined requirements rather than relying only on personal judgment about whether an interface appears accessible.

WCAG is organized around **principles**, **guidelines**, and **success criteria**, which describe accessibility expectations at increasing levels of detail. Principles establish the fundamental qualities of accessible web content, guidelines describe what should be achieved, and success criteria define specific, testable requirements for determining whether those goals have been met. For example, the Perceivable principle includes a guideline about providing text alternatives for non-text content, with a success criterion requiring appropriate alternatives for informative images. WCAG also provides **techniques** that demonstrate possible ways to satisfy success criteria but are not mandatory requirements.

WCAG has evolved through different versions, including **WCAG 2.1** and **WCAG 2.2**. WCAG 2.2 builds on WCAG 2.1 by introducing additional accessibility requirements while retaining the earlier success criteria, except for the obsolete **4.1.1 Parsing** criterion, which was removed. The version used for an evaluation depends on the project's applicable standards and requirements.

The four foundational WCAG principles are known as **POUR**, which stands for **Perceivable**, **Operable**, **Understandable**, and **Robust**. Each principle addresses a different aspect of accessibility, and together they describe how web content should support people with different access needs.

**Perceivable** means that information and user interface components must be presented in ways users can perceive. Important information should not depend entirely on one sensory ability, such as sight or hearing. For example, informative images may require text alternatives that screen readers can communicate, while videos containing spoken information may need captions. Important messages should also remain understandable without relying on color alone.

**Operable** means that interface components and navigation must be usable through appropriate input methods. For example, a user who relies on a keyboard should be able to navigate through an application and activate its controls without requiring a mouse. Keyboard focus should remain visible and should not become trapped inside an interactive component.

**Understandable** means that information and the operation of the interface must be understandable. Users should be able to recognize what controls do, follow instructions, and understand feedback from the system. For example, if a form rejects an invalid email address, the interface should identify the affected field and explain what needs to be corrected. Consistent navigation and predictable interactions also help users understand how the application behaves.

**Robust** means that content must be implemented so it can be interpreted reliably by different user agents, including assistive technologies. For example, form controls should communicate meaningful names, roles, and states. A custom checkbox that changes visually but does not communicate whether it is checked may create a barrier for someone using a screen reader.

These principles work together rather than representing separate stages of testing. A product may satisfy one principle while still presenting barriers related to another. Meeting the applicable success criteria across these principles provides the basis for determining WCAG conformance.

## WCAG Conformance Levels

WCAG defines three **conformance levels**, identified as **A**, **AA**, and **AAA**. Each level represents a different set of accessibility success criteria, with higher levels introducing additional requirements intended to address more accessibility barriers.

| Level         | Description                                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Level A**   | Establishes basic accessibility requirements, such as providing text alternatives for informative images and making functionality available through a keyboard |
| **Level AA**  | Adds further requirements, such as sufficient color contrast for text and the ability to resize text without losing content or functionality                   |
| **Level AAA** | Introduces additional, more demanding requirements, such as enhanced text contrast and sign language interpretation for prerecorded video content              |

The levels are **cumulative**, meaning that higher conformance levels also require satisfying the criteria from lower levels. Achieving **Level AA conformance** requires meeting the applicable Level A and Level AA success criteria, while **Level AAA conformance** requires meeting the applicable criteria at all three levels. Although Level AA is a common target for web accessibility projects and is referenced by various policies and regulatory frameworks, the required level depends on the applicable law, standard, contract, or organizational policy. Level AAA represents the highest conformance level, but it is not necessarily appropriate for every website because some of its success criteria cannot be satisfied for all types of content. For this reason, W3C does not recommend requiring Level AAA conformance as a general policy for entire websites.

WCAG conformance involves more than satisfying individual success criteria in isolation. It applies to **complete web pages** and requires every page in a **complete process**, such as a registration or checkout flow, to meet the selected conformance level. WCAG conformance also requires that only accessibility-supported uses of technologies are relied upon to satisfy success criteria, and that content using other technologies does not interfere with accessibility. These requirements help establish the conformance target that must be considered when defining the scope of an accessibility evaluation.

## Accessibility Requirements and Scope

**Accessibility requirements** define the conditions a product must satisfy to meet its accessibility expectations. They may come from WCAG, applicable laws or regulations, contractual obligations, organizational policies, or product-specific needs. The **scope of accessibility testing** determines which parts of the product, user interactions, and supported environments will be evaluated. Establishing these requirements and scope involves considering several factors that influence how the evaluation is planned and conducted.

| Factor                     | What needs to be established                                                                  |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| **Applicable standards**   | Which accessibility standards and versions apply to the product                               |
| **Conformance target**     | Which WCAG level or other accessibility requirements must be satisfied                        |
| **Product scope**          | Which pages, features, content, and user flows are included                                   |
| **Supported environments** | Which browsers, devices, operating systems, and relevant assistive technologies are supported |
| **User needs**             | Which accessibility barriers and interaction requirements are relevant to the product         |
| **Evaluation expectations**| What must be checked and how results will be assessed against the requirements                |

For example, when evaluating an online registration process, the team may need to identify the applicable WCAG version and conformance level, the registration pages and interactions included in the evaluation, and the relevant browser and assistive technology combinations. A specific accessibility requirement might state that all functionality in the registration process must be operable through a keyboard interface, consistent with the applicable WCAG success criteria. This provides testers with a defined condition to evaluate rather than a general expectation that the interface should be accessible.

A team may also select representative pages for a broader accessibility assessment. However, **testing scope is not necessarily the same as WCAG conformance scope**, and evaluating selected pages does not automatically establish conformance for an entire website. Supported testing environments guide practical coverage but do not, by themselves, limit the accessibility requirements that the product must satisfy. Requirements should also reflect the product's intended users and relevant interaction methods, including different screen sizes and input methods.

**Accessibility Testing Level 1** establishes the foundations for understanding accessibility barriers, WCAG principles, conformance levels, and the requirements that determine the scope of an evaluation. Building on these concepts, [**Accessibility Testing Level 2**](../2_level/2_accessibility_testing.md) introduces practical accessibility testing through keyboard operation and focus management, screen reader compatibility, image alternatives, color contrast, zoom and text resizing, accessible forms, motion preferences, semantic structure, and supporting accessibility testing tools.
