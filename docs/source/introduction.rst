Introduction
====================

Many test specialists choose to develop their own test scripts, where they automate performance verification, regression test, development verification, and so on. At Xena Networks, we have always been providing customers with the best tool for test automation. To help our customers achieve a more efficient quality control and continuous development verification, we have developed an open test suite framework **Xena OpenAutomation** (:term:`XOA`), overlaying various Xena hardware and virtual testers, to offer not only automated test suites but also the power to build programs from simple scripts to advanced applications with endless possibilities.

The foundation of XOA is its Python API, aka. XOA Driver, that provides interfaces for engineers to manage Xena hardware and virtual test equipment. Although we have open-sourced XOA Python API, it doesn't mean it will lack of support from Xena. On the contrary, our attitude toward XOA Python API is extremely serious because all of our test suites depend on XOA Python API.

Fundamentally different from `XOA CLI <https://docs.xenanetworks.com/projects/xoa-cli>`_, XOA Python API provides **object-oriented API**, **IDE built-in manual**, **high-level abstraction**, **command grouping**, and **event subscription** on top of Xena's proprietary binary chassis management protocol, built from the ground up. This has brought tremendous advantages over XOA CLI, enabling engineers to develop not only test scripts but also high-performance applications.

XOA Python API contains more than 600 APIs and functions, from basic streams creation to advance eye diagrams measurement. With this rich collection of programming interfaces, we empower our customers to either write test scripts or develop applications with almost limitless possibilities.
