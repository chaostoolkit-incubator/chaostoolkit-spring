# -*- coding: utf-8 -*-
import pytest
import requests
import requests_mock

from chaosspring.probes import chaosmonkey_enabled


def test_chaosmonkey_is_enabled():
    with requests_mock.mock() as m:
        m.get(
            "http://localhost:8080/actuator/chaosmonkey/status",
            status_code=200,
            text="Ready to be evil!")

        enabled = chaosmonkey_enabled(
            base_url="http://localhost:8080/actuator")

    assert enabled is True


def test_chaosmonkey_not_enabled():
    with requests_mock.mock() as m:
        m.get(
            "http://localhost:8080/actuator/chaosmonkey/status",
            status_code=200,
            text="You switched me off!")

        enabled = chaosmonkey_enabled(
            base_url="http://localhost:8080/actuator")

    assert enabled is False
