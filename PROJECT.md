# API Test Automation Framework — Technical Specification

## Project Overview

This specification defines the scope, architecture, requirements, delivery
milestones, and acceptance criteria for a Python API test automation framework.
Implementation proceeds in small, reviewable increments with explicit approval
before advancing to each subsequent milestone. CI/CD refers to automated checks
and delivery; the initial scope includes continuous integration through test
execution, without application deployment.

An API lets programs exchange data through requests and responses. Automated API
tests check whether those responses match expected behavior.

The initial practice API will be JSONPlaceholder, using
`https://jsonplaceholder.typicode.com` as the planned base URL. A base URL is the
shared starting address for API requests. Initial tests will focus on posts.

JSONPlaceholder is a practice service: write requests simulate changes rather
than permanently saving them. Planned tests must check each write response
without expecting later requests to return a saved change. Exact response
expectations will be checked against its documentation before implementation.

## Engineering Objectives

- Send HTTP requests and validate status codes and JSON data.
  HTTP is the communication protocol used by the API; a status code describes
  the result of a request, and JSON is a structured data format.
- Write clear, independent tests with useful failure messages.
- Build reusable request code without unnecessary complexity.
- Manage project history with Git and publish the repository on GitHub.
- Run tests automatically with GitHub Actions.
- Produce a portfolio project that another person can understand and run.

## Technology Stack

The following stack is planned. Installation and configuration have not been
verified through the documentation work.

| Technology | Planned purpose |
| --- | --- |
| Python | Language used for the framework and tests |
| Requests | Python library for sending HTTP requests |
| pytest | Tool for discovering, running, and reporting tests |
| pytest HTML reporting plugin | Generate readable HTML test reports using an existing plugin |
| Formatting and linting tools | Keep code formatting consistent and identify common code issues; tools to be selected |
| Git | Track changes in project history |
| GitHub | Host the repository and share the portfolio project |
| GitHub Actions | Run automated tests when changes are pushed or proposed |
| JSONPlaceholder | Initial external practice API |

Use a Python virtual environment to keep project packages separate from other
projects. Choose and record compatible Python and package versions during setup.
Additional dependencies require a clear need and approval.

## Architecture Specification — Planned

Begin with one readable test, then introduce shared code when it becomes useful.
The following layout is a proposal, not a list of files already created:

```text
project root/
├── AGENTS.md                  AI agent engineering guidelines
├── PROJECT.md                 Project scope, plan, and progress
├── README.md                  Setup, execution, and portfolio instructions
├── .gitignore                 Exclusions for local and generated files
├── requirements.txt           Required Python packages and their versions
├── pytest.ini                 Shared pytest settings
├── clients/
│   └── api_client.py           Small reusable layer for HTTP requests
├── tests/
│   ├── conftest.py             Shared pytest setup, called fixtures
│   └── test_posts.py           Tests for the posts resource
└── .github/
    └── workflows/
        └── tests.yml          GitHub Actions test workflow
```

Planned request flow:

```text
pytest test → API client → JSONPlaceholder → response → test assertions
```

An assertion checks an expected result and fails the test when it is not met.
Tests will own those expectations. The API client will handle sending requests,
including an explicit timeout to prevent requests from waiting indefinitely.
Fixtures will provide reusable setup without making tests depend on one another.
Keep the base URL in one shared configuration location when shared setup is added.

## Functional and Quality Requirements — Planned

None of these framework features is implemented yet.

- Read a list of posts and an individual post using GET requests.
- Check response status codes, selected headers, JSON structure, and key values.
- Cover a documented missing-resource case with an expected error response.
- Send POST, PUT, PATCH, and DELETE requests to validate creating, replacing,
  partially updating, and deleting data through simulated write responses.
- Reuse request handling and pytest fixtures where they improve clarity.
- Use parameterized tests: run the same test with multiple input examples.
- Set explicit request timeouts and provide understandable test failures.
- Run tests locally and automatically through GitHub Actions.
- Generate HTML test reports using an existing pytest plugin.
- Add formatting and linting: consistent code style and automated checks for
  common code issues.
- Document setup, test execution, limitations, and troubleshooting.

## Delivery Roadmap — Eight Milestones

Each milestone requires approval before moving to the next one. This plan does
not authorize implementation of future milestones.

| # | Milestone | Completion criteria | Current status |
| --- | --- | --- | --- |
| 1 | Project foundation | Create AGENTS.md, PROJECT.md, README.md, and .gitignore; create a Python virtual environment; initialize Git and make the first commit | In progress |
| 2 | First API test | Establish understanding of HTTP, JSON, Requests, and pytest through incremental explanations; implement and run the first GET test | Not started |
| 3 | More API test scenarios | Add positive and negative tests; cover GET, POST, PUT, PATCH, and DELETE; respect JSONPlaceholder's simulated writes | Not started |
| 4 | Reusable framework structure | Introduce API helpers, configuration, and fixtures | Not started |
| 5 | Advanced testing basics | Add parameterized tests, timeouts, and error handling; keep tests independent and maintainable | Not started |
| 6 | Reports and code quality | Generate HTML reports using an existing pytest plugin; add formatting and linting | Not started |
| 7 | GitHub and CI/CD | Publish the repository on GitHub; run tests automatically using GitHub Actions | Not started |
| 8 | Portfolio polish | Improve README and documentation; add an architecture diagram; review the framework for interview readiness | Not started |

## Current Progress

- Milestone 1: **In progress**.
- `AGENTS.md`: **Completed**; defines engineering guidelines, communication
  requirements, scope boundaries, and approval checkpoints.
- `PROJECT.md`: **Created, awaiting review**; records the project proposal,
  milestones, and completion criteria.
- `README.md` and `.gitignore`: **Created**; project introduction and Git
  exclusion rules are present.
- Remaining foundation steps and milestones 2–8: **Not started**.

### Not Yet Completed or Verified

- No framework code, tests, dependencies, or CI configuration have been created
  as part of these documentation tasks.
- Existing Python, Git, and GitHub setup has not been inspected or verified.
- No API requests or test runs have been performed for this project plan.

Update progress only when work has actually been completed. Record verification
results and relevant limitations rather than treating planned work as finished.

## Out of Scope for the Initial Version

- Building or hosting an API or database.
- Testing permanent data storage through JSONPlaceholder write requests.
- Authentication flows or APIs requiring passwords or API keys.
- Browser or mobile interface testing.
- Performance, load, penetration, or security testing.
- Complex framework abstractions, custom reporting systems, and plugins beyond
  the planned HTML reporting plugin unless explicitly approved.
- Deployment of an application or a full continuous delivery pipeline.
- Additional APIs or resources unless explicitly approved.

Never put passwords, API keys, or other secrets in source code. Any future need
for credentials requires a separate, approved approach to secure configuration.

## Acceptance Criteria — Definition of Done

The initial framework is done when all of the following are verified:

- The eight milestones have been reviewed and approved as completed.
- A fresh checkout can be set up using the documented Python version, virtual
  environment instructions, and recorded dependencies.
- The README explains how to run tests with `python -m pytest` and interpret
  results, including common setup and network errors.
- Approved read, missing-resource, and simulated write tests pass locally and
  in GitHub Actions against JSONPlaceholder.
- HTML test reports can be generated using an existing pytest plugin, and the
  README explains how to generate and view them.
- Formatting and linting checks pass using the selected tools.
- Tests check meaningful response behavior, run independently, and do not assume
  simulated writes persist.
- Requests use explicit timeouts; network failures remain visible and are not
  hidden by automatic skips or retries.
- Python code is readable, pytest conventions are followed, and shared code has
  a clear purpose.
- No secrets, unnecessary dependencies, or unrelated features are included.
- Documentation accurately distinguishes implemented behavior from future ideas
  and explains the external API and simulated-write limitations.
- The project owner can explain the main files, request flow, assertions, and
  automated workflow in clear terms, supported by incremental explanations and
  documentation.

The framework depends on an external service and internet access. A failed run
must be investigated to distinguish a test problem from a service or connection
problem; passing runs do not guarantee the external API will always be available.
