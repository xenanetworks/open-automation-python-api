.. _introduction-label:

Introduction
=====================================================

The *Xena OpenAutomation Python API Documentation* provides basic information about Xena OpenAutomation Python :term:`API` functions. It also provides descriptions of how to use these functions together with examples of creating and running test configurations.

The target audience of this document is test specialists who develop and run automated test scripts/programs using Xena :term:`TGA` hardware and software. Users of this document should have the following knowledge and experience:

* Ability to program with Python language.
* Familiarity with the operating system of your development environment.
* Familiarity with Xena test equipment.
* Working knowledge of data communications theory and practice.


About Xena OpenAutomation Python API
----------------------------------------

Many test specialists choose to develop their own test scripts, where they automate performance verification, regression test, development verification, and so on. At Xena Networks, we have always been providing customers with the best tool for test automation. To help our customers achieve a more efficient quality control and continuous development verification, we have developed an open test suite framework **Xena OpenAutomation** (XOA), overlaying various Xena hardware and virtual testers, to offer not only automated test suites but also the power to build programs from simple scripts to advanced applications with endless possibilities.

The foundation of Xena OpenAutomation is its Python API (XOA Python API) that provides interfaces for engineers to manage Xena hardware and virtual test equipment. Although we have open-sourced XOA Python API, it doesn't mean it will lack of support from Xena. On the contrary, our attitude toward XOA Python API is extremely serious because all of our test suites depend on XOA Python API.

Fundamentally different from :term:`CLI`, XOA Python API is **object-oriented** and is designed based on Xena's proprietary binary chassis management protocol from the ground up. This has brought tremendous advantages over :term:`CLI`, enabling engineers to develop not only test scripts but also high-performance applications.

XOA Python API contains more than 600 commands, from basic streams creation to advance eye diagrams measurement. With this rich collection of programming interfaces, we empower our customers to either write test scripts or develop applications with almost limitless possibilities.


About This Documentation
----------------------------------------

:ref:`introduction-label` provides an overview of XOA Python API and the use of this document.

:ref:`getting-started-label` covers installation instructions. 

:ref:`general-information-label` includes API structure, principles of using Xena testers, and guidance to increase test execution performance.

:ref:`high-level-api-label` covers the notations, terminologies, features, and code examples of XOA High-Level API (HL-API).  

:ref:`low-level-api-label` includes the notations, terminologies, features, and code examples of XOA Low-Level API (LL-API).  

:ref:`api-documentation-label` covers all the functions that make up XOA Python API. The description of API functions is automatically generated from the docstring in the source code.