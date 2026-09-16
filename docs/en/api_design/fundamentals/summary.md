# Summary

This summary brings together the most important concepts from **API Fundamentals**. It is designed as a quick reference for revision and preparation for questions where the purpose of APIs, their main components, and different approaches to API communication need to be explained clearly.

## Table of Contents: API Fundamentals

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **APIs, consumers, providers, operations, software boundaries, and API styles**. The main goal is to understand why APIs exist and how they allow different parts of software to interact through defined interfaces.

An **API (Application Programming Interface)** defines how one software component or system can use functionality provided by another. The software using the API is the **consumer**, while the software supplying the functionality is the **provider**. The API sits between these roles as the defined interface through which interaction takes place.

The consumer depends on the API rather than on the provider's internal implementation. This separation means that a consumer can use available functionality without needing to understand how the provider performs its work internally. The provider can also change internal implementation details while keeping the same API available to consumers.

APIs expose **operations**, which represent actions that consumers are allowed to use. Depending on the API, an operation might retrieve information, create or update data, perform a calculation, or trigger another action. A consumer supplies any required information through the API, the provider performs the work, and a result may be returned.

APIs also create **defined boundaries between software components and systems**. These boundaries allow applications, services, and other components to interact without depending directly on each other's internal implementations. APIs are not limited to communication over a network. Libraries, operating systems, databases, frameworks, and other software can also provide APIs.

API interactions do not all follow the same communication pattern. Some use requests and responses, some support ongoing communication, and others notify software when events occur. The important distinction is that the API defines how the participating software is allowed to interact.

For communication between applications and services, **REST, GraphQL, SOAP, and gRPC** are examples of different API approaches. **REST** commonly organizes operations around resources, **GraphQL** allows consumers to request the information they need, **SOAP** exchanges messages according to defined structural rules, and **gRPC** allows services to invoke defined operations provided by other services. These approaches differ in how they organize communication, but all provide defined ways for software systems to interact.

The important relationships to remember are that a **consumer uses an API**, a **provider supplies the functionality behind it**, and the **API defines the permitted interaction between them**. An API can expose multiple **operations**, and consumers use those operations without needing direct knowledge of the provider's internal implementation.

After reviewing Level 1, you should be able to explain **what an API is and why APIs are useful**, distinguish the roles of a **consumer, API, and provider**, describe what an **API operation** represents, explain how APIs create **defined software boundaries**, recognize that APIs can exist in different kinds of software and not only between web applications, and identify **REST, GraphQL, SOAP, and gRPC** as different approaches used for communication between applications and services.
