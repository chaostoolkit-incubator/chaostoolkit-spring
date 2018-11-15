# -*- coding: utf-8 -*-
from unittest import mock
from unittest.mock import MagicMock

import pytest
from chaoslib.exceptions import FailedActivity
from requests import Response, codes

from chaosspring.probes import chaosmonkey_enabled, \
    watcher_configuration, assaults_configuration


def test_chaosmonkey_is_enabled():
    mock_response = MagicMock(Response, status_code=codes.ok)
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        enabled = chaosmonkey_enabled(base_url=actuator_endpoint)

    assert enabled
    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/status",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)


def test_chaosmonkey_is_enabled_with_headers():
    mock_response = MagicMock(Response, status_code=codes.ok)
    actuator_endpoint = "http://localhost:8080/actuator"
    headers = {
        "key1": "value1",
        "key2": "value2"
    }

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        enabled = chaosmonkey_enabled(base_url=actuator_endpoint, headers=headers)

    assert enabled
    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/status",
                                          headers=headers,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)


def test_chaosmonkey_is_enabled_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            chaosmonkey_enabled(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/status",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "ChaosMonkey status enquiry failed" in str(ex)


def test_chaosmonkey_not_enabled():
    mock_response = MagicMock(Response, status_code=codes.service_unavailable)
    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        enabled = chaosmonkey_enabled(base_url=actuator_endpoint)

    assert not enabled
    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/status",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)


def test_watcher_configuration():
    text_response = {
        "controller": True,
        "restController": False,
        "service": True,
        "repository": False,
        "component": False
    }

    mock_response = MagicMock(Response, status_code=codes.ok)
    mock_response.json.return_value = text_response

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        configuration = watcher_configuration(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/watcher",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)

    assert "service" in configuration
    assert configuration["service"] is True


def test_watcher_configuration_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            watcher_configuration(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/watcher",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "ChaosMonkey watcher enquiry failed" in str(ex)


def test_assaults_configuration():
    text_response = {
        "level": 3,
        "latencyRangeStart": 1000,
        "latencyRangeEnd": 3000,
        "latencyActive": True,
        "exceptionsActive": False,
        "killApplicationActive": False,
        "restartApplicationActive": False
    }

    mock_response = MagicMock(Response, status_code=codes.ok)
    mock_response.json.return_value = text_response

    actuator_endpoint = "http://localhost:8080/actuator"
    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        configuration = assaults_configuration(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/assaults",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "level" in configuration
    assert configuration["level"] == 3


def test_assaults_configuration_fails():
    mock_response = MagicMock(Response, status_code=codes.not_found, text="Not Found")

    actuator_endpoint = "http://localhost:8080/actuator"

    with mock.patch('chaosspring.api.call_api', return_value=mock_response) as mock_call_api:
        with pytest.raises(FailedActivity) as ex:
            assaults_configuration(base_url=actuator_endpoint)

    mock_call_api.assert_called_once_with(base_url=actuator_endpoint,
                                          api_endpoint="chaosmonkey/assaults",
                                          headers=None,
                                          timeout=None,
                                          configuration=None,
                                          secrets=None)
    assert "ChaosMonkey assaults enquiry failed" in str(ex)
