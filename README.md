 # [Chaos Toolkit Driver for Spring Chaos](https://chaostoolkit.org/drivers/spring/)

[![Python versions](https://img.shields.io/pypi/pyversions/chaostoolkit-spring.svg)](https://www.python.org/) [![Build Status](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-spring.svg?branch=master)](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-spring)


This project is a collection of [actions][] and [probes][], gathered as an
extension to the [Chaos Toolkit][chaostoolkit].

[actions]: http://chaostoolkit.org/reference/api/experiment/#action
[probes]: http://chaostoolkit.org/reference/api/experiment/#probe
[chaostoolkit]: http://chaostoolkit.org

## Install

This package requires Python 3.6+

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

```
$ pip install -U chaostoolkit-spring
```

## Usage

Currently this driver supports interactions with a [Spring Boot-based](https://spring.io/projects/spring-boot) service that has included the [2.0.0.-SNAPSHOT](https://codecentric.github.io/chaos-monkey-spring-boot/2.0.0-SNAPSHOT/) release of the [Chaos Monkey for Spring Boot](https://github.com/codecentric/chaos-monkey-spring-boot). This snapshot includes the necessary Spring Boot Actuator HTTP endpoints so that the Chaos Toolkit to interact with the chaos features at runtime.

Once you have [added the Chaos Monkey for Spring Boot](https://codecentric.github.io/chaos-monkey-spring-boot/2.0.0-SNAPSHOT/#getting-started) and [enabled the Spring Boot Actuator HTTP endpoints](https://codecentric.github.io/chaos-monkey-spring-boot/2.0.0-SNAPSHOT/#endpoints) you can then use the probes and actions from this driver.

To use the probes and actions from this package, add the following to your
experiment file:

```json
{
    "name": "enable_chaosmonkey",
    "provider": {
        "arguments": {
            "base_url": "http://localhost:8080/actuator"
        },
        "func": "enable_chaosmonkey",
        "module": "chaosspring.actions",
        "type": "python"
    },
    "type": "action"
}
```

This will interact with the specified service and enable the Chaos Monkey features. You can also turn off the Chaos Monkey if you wish by specifying the following action:

```json
{
    "name": "disable_chaosmonkey",
    "provider": {
        "arguments": {
            "base_url": "http://localhost:8080/actuator"
        },
        "func": "disable_chaosmonkey",
        "module": "chaosspring.actions",
        "type": "python"
    },
    "type": "action"
}
```

You can then manipulate the [Chaos Monkey assaults](https://codecentric.github.io/chaos-monkey-spring-boot/2.0.0-SNAPSHOT/#assaults) active on your service by specifing the following action:

```json
{
    "name": "configure_assaults",
    "provider": {
        "arguments": {
            "base_url": "http://localhost:8080/actuator",
            "assaults_configuration": {
                "level": 5,
                "latencyRangeStart": 2000,
                "latencyRangeEnd": 5000,
                "latencyActive": false,
                "exceptionsActive": false,
                "killApplicationActive": true,
                "restartApplicationActive": false
            }
        },
        "func": "change_assaults_configuration",
        "module": "chaosspring.actions",
        "type": "python"
    },
    "type": "action"
}
```

That's it!

Please explore the code to use further probes and actions.

### SSL Verification

If you do not wish to have SSL Verification performed during your actions/probes
then you can pass the argument `"verify_ssl": false` to the individual activities.

If you wish to provide a `CA_BUNDLE` or directory of trusted CAs certificates,
provide the environment variables specified in the `requests` documentation here:
[Requests SSL Cert Verification](https://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification).

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, write unit tests to cover the proposed changes,
implement the changes, ensure they meet the formatting standards set out by `black`,
`flake8`, and `isort`, and then raise a PR to the repository for review.

Please refer to the [formatting](#formatting-and-linting) section for more information
on the formatting standards.

The Chaos Toolkit projects require all contributors must sign a
[Developer Certificate of Origin][dco] on each commit they would like to merge
into the master branch of the repository. Please, make sure you can abide by
the rules of the DCO before submitting a PR.

[dco]: https://github.com/probot/dco#how-it-works

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ make install-dev
```

Now, you can edit the files and they will be automatically be seen by your
environment, even when running from the `chaos` command locally.

### Tests

To run the tests for the project execute the following:

```console
$ make tests
```

### Formatting and Linting

We use a combination of [`black`][black], [`flake8`][flake8], and [`isort`][isort] to both
lint and format this repositories code.

[black]: https://github.com/psf/black
[flake8]: https://github.com/PyCQA/flake8
[isort]: https://github.com/PyCQA/isort

Before raising a Pull Request, we recommend you run formatting against your code with:

```console
$ make format
```

This will automatically format any code that doesn't adhere to the formatting standards.

As some things are not picked up by the formatting, we also recommend you run:

```console
$ make lint
```

To ensure that any unused import statements/strings that are too long, etc. are also picked up.
