from unittest.mock import MagicMock, Mock, patch

import requests_mock
from requests import codes
from requests.models import Response

from chaosspring.api import call_api


def test_call_api_get():
    with requests_mock.mock() as m:
        m.request(
            "GET",
            "http://localhost:8080/actuator/chaosmonkey/status",
            status_code=codes.ok,
            text="Ready to be evil!",
        )

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/status",
            assaults_configuration=None,
            timeout=3000,
            configuration=None,
            secrets=None,
        )

    assert response.status_code == codes.ok
    assert response.text == "Ready to be evil!"


@patch("chaosspring.api.requests.request", autospec=True)
def test_call_api_without_verification(mocked_request: MagicMock):
    mock_resp = Mock(Response)
    expected_status_code = codes.ok
    expected_text = "Ready to be evil"
    mock_resp.status_code = expected_status_code
    mock_resp.text = expected_text
    mocked_request.return_value = mock_resp
    response = call_api(
        base_url="http://localhost:8080/actuator",
        api_endpoint="chaosmonkey/status",
        assaults_configuration=None,
        timeout=3000,
        verify=False,
        configuration=None,
        secrets=None,
    )

    assert response.status_code == expected_status_code
    assert response.text == expected_text

    mocked_request.assert_called_once_with(
        method="GET",
        url="http://localhost:8080/actuator/chaosmonkey/status",
        params={"timeout": 3000, "verify": False},
        data=None,
        headers={"Accept": "application/json"},
    )


@patch("chaosspring.api.requests.request", autospec=True)
def test_call_api_with_verification(mocked_request: MagicMock):
    mock_resp = Mock(Response)
    expected_status_code = codes.ok
    expected_text = "Ready to be evil"
    mock_resp.status_code = expected_status_code
    mock_resp.text = expected_text
    mocked_request.return_value = mock_resp
    response = call_api(
        base_url="http://localhost:8080/actuator",
        api_endpoint="chaosmonkey/status",
        assaults_configuration=None,
        timeout=3000,
        configuration=None,
        secrets=None,
    )

    assert response.status_code == expected_status_code
    assert response.text == expected_text

    mocked_request.assert_called_once_with(
        method="GET",
        url="http://localhost:8080/actuator/chaosmonkey/status",
        params={"timeout": 3000, "verify": True},
        data=None,
        headers={"Accept": "application/json"},
    )


def test_call_api_post():
    with requests_mock.mock() as m:
        m.request(
            "POST",
            "http://localhost:8080/actuator/chaosmonkey/enable",
            status_code=codes.ok,
            text="Chaos Monkey is enabled",
        )

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/enable",
            method="POST",
            assaults_configuration=None,
            timeout=None,
            configuration=None,
            secrets=None,
        )

    assert response.status_code == codes.ok
    assert response.text == "Chaos Monkey is enabled"


def test_call_api_get_with_header_extension():
    request_headers = {
        "Accept": "application/json",
        "X-CF-APP-INSTANCE": "d5e95e17-9ed0-40ec-bdf0-a5d9cd298e87:1",
    }

    headers = {"X-CF-APP-INSTANCE": "d5e95e17-9ed0-40ec-bdf0-a5d9cd298e87:1"}

    with requests_mock.mock() as m:
        m.request(
            "GET",
            "http://localhost:8080/actuator/chaosmonkey/status",
            request_headers=request_headers,
            status_code=codes.ok,
            text="Ready to be evil!",
        )

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/status",
            headers=headers,
            assaults_configuration=None,
            timeout=None,
            configuration=None,
            secrets=None,
        )

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
        "restartApplicationActive": False,
    }
    request_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    with requests_mock.mock() as m:
        m.request(
            "POST",
            "http://localhost:8080/actuator/chaosmonkey/assaults",
            request_headers=request_headers,
            status_code=codes.ok,
            text="Chaos Monkey assaults configuration changed!",
        )

        response = call_api(
            base_url="http://localhost:8080/actuator",
            api_endpoint="chaosmonkey/assaults",
            method="POST",
            assaults_configuration=assaults_configuration,
            timeout=None,
            configuration=None,
            secrets=None,
        )

    assert response.status_code == codes.ok
    assert response.text == "Chaos Monkey assaults configuration changed!"
