# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
import pytest
import requests
import requests_mock

from chaosspring.actions import enable_chaosmonkey, \
    disable_chaosmonkey, change_assaults_configuration


def test_enable_chaosmonkey():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/enable",
            status_code=200,
            text="Chaos Monkey is enabled")

        enabled = enable_chaosmonkey(
            base_url="http://localhost:8080/actuator")

    assert enabled == "Chaos Monkey is enabled"


def test_enable_chaosmonkey_fails():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/enable",
            status_code=404)

        with pytest.raises(FailedActivity) as ex:
            enable_chaosmonkey(
                base_url="http://localhost:8080/actuator")

        assert "Enable ChaosMonkey failed" in str(ex)


def test_disable_chaosmonkey():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/disable",
            status_code=200,
            text="Chaos Monkey is disabled")

        enabled = disable_chaosmonkey(
            base_url="http://localhost:8080/actuator")


def test_disable_chaosmonkey_fails():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/disable",
            status_code=404)

        with pytest.raises(FailedActivity) as ex:
            disable_chaosmonkey(
                base_url="http://localhost:8080/actuator")

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

    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/assaults",
            status_code=200,
            text="Assault config has changed")

        changed = change_assaults_configuration(
            base_url="http://localhost:8080/actuator",
            assaults_configuration=assaults_configuration)

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

    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/assaults",
            status_code=404)

        with pytest.raises(FailedActivity) as ex:
            change_assaults_configuration(
                base_url="http://localhost:8080/actuator",
                assaults_configuration=assaults_configuration)

        assert "Change ChaosMonkey Assaults Configuration failed" in str(ex)
