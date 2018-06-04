# -*- coding: utf-8 -*-
from chaoslib.exceptions import FailedActivity
import pytest
import requests
import requests_mock

from chaosspring.actions import enable_chaosmonkey, disable_chaosmonkey


def test_enable_chaosmonkey():
    with requests_mock.mock() as m:
        m.post(
            "http://localhost:8080/actuator/chaosmonkey/enable",
            status_code=200,
            text="Chaos Monkey is enabled")

        enabled = enable_chaosmonkey(
            base_url="http://localhost:8080/actuator")


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
