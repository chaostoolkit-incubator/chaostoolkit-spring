from unittest import mock
from unittest.mock import MagicMock

import pytest
from chaoslib.exceptions import FailedActivity
from requests import Response, codes

from chaosspring.actions import (
    change_assaults_configuration,
    change_watchers_configuration,
    disable_chaosmonkey,
    enable_chaosmonkey,
)


def test_enable_chaosmonkey():
    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Chaos Monkey is enabled"
    )
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        text = enable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/enable",
        method="POST",
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert text == "Chaos Monkey is enabled"


def test_enable_chaosmonkey_without_ssl_verification():
    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Chaos Monkey is enabled"
    )
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        text = enable_chaosmonkey(base_url=actuator_endpoint, verify_ssl=False)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/enable",
        method="POST",
        headers=None,
        timeout=None,
        verify=False,
        configuration=None,
        secrets=None,
    )
    assert text == "Chaos Monkey is enabled"


def test_enable_chaosmonkey_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            enable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/enable",
        method="POST",
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert "Enable ChaosMonkey failed" in str(ex)


def test_disable_chaosmonkey():
    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Chaos Monkey is disabled"
    )
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        text = disable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/disable",
        method="POST",
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert text == "Chaos Monkey is disabled"


def test_disable_chaosmonkey_without_ssl_verification():
    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Chaos Monkey is disabled"
    )
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        text = disable_chaosmonkey(base_url=actuator_endpoint, verify_ssl=False)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/disable",
        method="POST",
        headers=None,
        timeout=None,
        verify=False,
        configuration=None,
        secrets=None,
    )
    assert text == "Chaos Monkey is disabled"


def test_disable_chaosmonkey_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            disable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/disable",
        method="POST",
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert "Disable ChaosMonkey failed" in str(ex)


def test_change_assaults_configuration():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False,
    }

    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Assault config has changed"
    )

    actuator_endpoint = "http://localhost:8080/actuator"
    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        changed = change_assaults_configuration(
            base_url=actuator_endpoint, assaults_configuration=assaults_configuration
        )

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/assaults",
        method="POST",
        assaults_configuration=assaults_configuration,
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert changed == "Assault config has changed"


def test_change_assaults_configuration_without_ssl_verification():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False,
    }

    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Assault config has changed"
    )

    actuator_endpoint = "http://localhost:8080/actuator"
    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        changed = change_assaults_configuration(
            base_url=actuator_endpoint,
            assaults_configuration=assaults_configuration,
            verify_ssl=False,
        )

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/assaults",
        method="POST",
        assaults_configuration=assaults_configuration,
        headers=None,
        timeout=None,
        verify=False,
        configuration=None,
        secrets=None,
    )
    assert changed == "Assault config has changed"


def test_change_assaults_configuration_fails():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False,
    }

    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            change_assaults_configuration(
                base_url=actuator_endpoint,
                assaults_configuration=assaults_configuration,
            )

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/assaults",
        method="POST",
        assaults_configuration=assaults_configuration,
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert "Change ChaosMonkey Assaults Configuration failed" in str(ex)


def test_change_watchers_configuration():
    watchers_configuration = {
        "controller": False,
        "restController": False,
        "service": True,
        "repository": False,
        "component": False,
        "restTemplate": False,
        "webClient": False,
        "actuatorHealth": False,
        "beans": [],
        "beanClasses": [],
        "excludeClasses": [],
    }

    mock_response = MagicMock(
        Response, status_code=codes.ok, text="Watcher config has changed"
    )

    actuator_endpoint = "http://localhost:8080/actuator"
    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        changed = change_watchers_configuration(
            base_url=actuator_endpoint, watchers_configuration=watchers_configuration
        )

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/watchers",
        method="POST",
        watchers_configuration=watchers_configuration,
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert changed == "Watcher config has changed"


def test_change_watchers_configuration_fails():
    watchers_configuration = {
        "controller": False,
        "restController": False,
        "service": True,
        "repository": False,
        "component": False,
        "restTemplate": False,
        "webClient": False,
        "actuatorHealth": False,
        "beans": [],
        "beanClasses": [],
        "excludeClasses": [],
    }

    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch(
        "chaosspring.api.call_api", return_value=mock_response
    ) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            change_watchers_configuration(
                base_url=actuator_endpoint,
                watchers_configuration=watchers_configuration,
            )

    mock_call_api.assert_called_once_with(
        base_url=actuator_endpoint,
        api_endpoint="chaosmonkey/watchers",
        method="POST",
        watchers_configuration=watchers_configuration,
        headers=None,
        timeout=None,
        verify=True,
        configuration=None,
        secrets=None,
    )
    assert "Change ChaosMonkey Assaults Configuration failed" in str(ex)
