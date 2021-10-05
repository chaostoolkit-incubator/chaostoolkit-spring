# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit-incubator/chaostoolkit-spring/compare/0.3.0...HEAD

## [0.3.0][] - 2021-10-05

[0.3.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-spring/compare/0.2.0...0.3.0

### Changed:

* Switched to `black`, `flake8`, and `isort` for linting & formatting
* Ran `pyupgrade --py36-plus` across the codebase
* Switch to GitHub Actions instead of TravisCI
* Modified README to fall closer inline to more recently touched CTK packages

### Added:

* Makefile to abstract away common development tasks
* GitHub Actions workflows
* Added `verify_ssl` argument to probes and actions to allow for disabling SSL verification

## [0.2.0][] - 2018-11-20

[0.2.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-spring/compare/0.1.1...0.2.0

### Added

- fixed the bug on chaosmonkey_enabled probes when chaosmonkey not enabled.
- refactoring the code to remove duplicate requests calling

## [0.1.1][] - 2018-07-06

[0.1.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-spring/compare/0.1.0...0.1.1

### Added

-   MANIFEST.in

## [0.1.0][] - 2018-07-06

[0.1.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-spring/tree/0.1.0

### Added

-   Initial release
