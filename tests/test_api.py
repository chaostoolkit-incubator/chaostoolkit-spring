# -*- coding: utf-8 -*-

import requests_mock
from requests import codes

from chaosspring.api import call_api


def test_call_api_get():
    with requests_mock.mock() as m:
        m.request(
            "GET",
            "http://localhost:8080/actuator/chaosmonkey/status",
            status_code=codes.ok,
            text="Ready to be evil!")

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/status",
            assaults_configuration=None,
            timeout=3000,
            configuration=None,
            secrets=None)

    assert response.status_code == codes.ok
    assert response.text == "Ready to be evil!"


def test_call_api_post():
    with requests_mock.mock() as m:
        m.request(
            "POST",
            "http://localhost:8080/actuator/chaosmonkey/enable",
            status_code=codes.ok,
            text="Chaos Monkey is enabled")

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/enable",
            method="POST",
            assaults_configuration=None,
            timeout=None,
            configuration=None,
            secrets=None)

    assert response.status_code == codes.ok
    assert response.text == "Chaos Monkey is enabled"


def test_call_api_get_with_header_extension():
    request_headers = {"Accept": "application/json",
               "X-CF-APP-INSTANCE": "d5e95e17-9ed0-40ec-bdf0-a5d9cd298e87:1"}

    headers = {"X-CF-APP-INSTANCE": "d5e95e17-9ed0-40ec-bdf0-a5d9cd298e87:1"}

    with requests_mock.mock() as m:
        m.request(
            "GET",
            "http://localhost:8080/actuator/chaosmonkey/status",
            request_headers=request_headers,
            status_code=codes.ok,
            text="Ready to be evil!")

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/status",
            headers=headers,
            assaults_configuration=None,
            timeout=None,
            configuration=None,
            secrets=None)

    assert response.status_code == codes.ok
    assert response.text == "Ready to be evil!"


def test_call_api_post_with_assaults_configuration():
    assaults_configuration = {
        "level": 5,
        "latencyRangeStart": 2000,
        "latencyRangeEnd": 5000,
        "latencyActive": True,
        "exceptionsActive": True,
        "killApplicationActive": False,
        "restartApplicationActive": False
    }
    request_headers = {"Accept": "application/json",
                       "Content-Type": "application/json"}

    with requests_mock.mock() as m:
        m.request(
            "POST",
            "http://localhost:8080/actuator/chaosmonkey/assaults",
            request_headers=request_headers,
            status_code=codes.ok,
            text="Chaos Monkey assaults configuration changed!")

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/assaults",
            method="POST",
            assaults_configuration=assaults_configuration,
            timeout=None,
            configuration=None,
            secrets=None)

    assert response.status_code == codes.ok
    assert response.text == "Chaos Monkey assaults configuration changed!"
