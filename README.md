# API Test Automation Framework

A Python learning and portfolio project for building a readable API test
automation framework using Requests, pytest, and GitHub Actions.

## Project Status

**Milestone 1: Project foundation — in progress.**

The project currently contains planning and foundation files:

- `AGENTS.md`: instructions for working and learning together.
- `PROJECT.md`: scope, architecture proposal, eight milestones, and completion criteria.
- `README.md`: project introduction and current usage status.
- `.gitignore`: rules for excluding local and generated files from Git tracking.

The framework and tests are not implemented yet. Environment setup, dependency
installation, Git initialization, and automated test runs remain future steps.

## Project Goal

Build a professional API test automation framework while learning Python, HTTP,
JSON, Requests, pytest, Git, GitHub, and CI/CD.

An API lets programs exchange data through requests and responses. HTTP defines
how those requests and responses travel, and JSON is a structured data format
commonly used in their content. Automated tests will check whether API responses
match expected results.

## Planned Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Write the framework and tests |
| Requests | Send HTTP requests |
| pytest | Discover and run tests |
| Existing pytest HTML reporting plugin | Generate HTML test reports |
| Formatting and linting tools, to be selected | Keep style consistent and check common code issues |
| Git and GitHub | Track changes and share the project |
| GitHub Actions | Run tests automatically |

These tools have not been installed or configured as part of the documentation
work. Python and dependency versions will be recorded during setup.

## Practice API

The initial API will be JSONPlaceholder at
`https://jsonplaceholder.typicode.com`, starting with the posts resource.

JSONPlaceholder simulates write operations without permanently saving changes.
Tests will check write responses without expecting later requests to return saved
changes. Exact expectations will be checked against its documentation before
implementation.

## Planned Features

None of the following features is implemented yet:

- Positive and negative API tests covering GET, POST, PUT, PATCH, and DELETE.
- Checks for status codes, selected headers, JSON structure, and key values.
- Reusable API helpers, configuration, and pytest fixtures (shared test setup).
- Parameterized tests, which run the same checks with different inputs.
- Explicit request timeouts, clear failures, and independent tests.
- HTML test reports, formatting, and linting checks.
- Automated test execution through GitHub Actions.

## Roadmap

1. **Project foundation:** documentation, `.gitignore`, virtual environment, and
   the first Git commit.
2. **First API test:** learn the core tools and run the first GET test.
3. **More API test scenarios:** positive and negative tests across the five HTTP
   methods, respecting simulated writes.
4. **Reusable framework structure:** API helpers, configuration, and fixtures.
5. **Advanced testing basics:** parameterization, timeouts, and error handling.
6. **Reports and code quality:** HTML reports, formatting, and linting.
7. **GitHub and CI/CD:** publish the repository and automate test runs.
8. **Portfolio polish:** improve documentation, add an architecture diagram,
   and prepare to explain the framework in interviews.

See [PROJECT.md](PROJECT.md) for detailed milestones, the proposed architecture,
out-of-scope items, and the definition of done. Each new milestone requires approval.

## Setup and Test Execution

Setup instructions will be added when the Python environment and dependencies
are established. There are currently no project tests to run.

The planned test command is `python -m pytest`; it will become a verified usage
instruction after tests are implemented. HTML report commands will be documented
when a reporting plugin is selected and configured.

## Security and Limitations

- Never commit passwords, API keys, or other secrets. Ignore rules help prevent
  accidental additions but do not protect secrets already tracked by Git.
- Tests will depend on internet access and an external practice service.
- Connection or service failures must be investigated and must not be hidden
  with automatic skips or retries.
- Authentication, load testing, security testing, and application deployment
  are outside the initial scope.
