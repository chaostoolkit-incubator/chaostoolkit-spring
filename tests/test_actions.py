# -*- coding: utf-8 -*-
from unittest import mock
from unittest.mock import MagicMock

import pytest
from chaoslib.exceptions import FailedActivity
from requests import codes, Response

from chaosspring.actions import enable_chaosmonkey, \
    disable_chaosmonkey, change_assaults_configuration


def test_enable_chaosmonkey():
    mock_response = MagicMock(Response, status_code=codes.ok, text="Chaos Monkey is enabled")
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        text = enable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/enable",
                                          method="POST",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert text == "Chaos Monkey is enabled"


def test_enable_chaosmonkey_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            enable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/enable",
                                          method="POST",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "Enable ChaosMonkey failed" in str(ex)


def test_disable_chaosmonkey():
    mock_response = MagicMock(Response, status_code=codes.ok, text="Chaos Monkey is disabled")
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        text = disable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/disable",
                                          method="POST",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert text == "Chaos Monkey is disabled"


def test_disable_chaosmonkey_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            disable_chaosmonkey(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/disable",
                                          method="POST",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "Disable ChaosMonkey failed" in str(ex)


def test_change_assaults_configuration():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False
    }

    mock_response = MagicMock(Response, status_code=codes.ok, text="Assault config has changed")

    actuator_endpoint = "http://localhost:8080/actuator"
    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        changed = change_assaults_configuration(base_url=actuator_endpoint,
                                                assaults_configuration=assaults_configuration)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/assaults",
                                          method="POST",
                                          assaults_configuration=assaults_configuration,
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert changed == "Assault config has changed"


def test_change_assaults_configuration_fails():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False
    }

    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            change_assaults_configuration(base_url=actuator_endpoint, assaults_configuration=assaults_configuration)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/assaults",
                                          method="POST",
                                          assaults_configuration=assaults_configuration,
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "Change ChaosMonkey Assaults Configuration failed" in str(ex)
