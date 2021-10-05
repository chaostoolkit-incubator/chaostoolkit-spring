from typing import Any, Dict

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
from requests import codes

from chaosspring import api

__all__ = ["enable_chaosmonkey", "disable_chaosmonkey", "change_assaults_configuration"]


def enable_chaosmonkey(
    base_url: str,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> str:
    """
    Enable Chaos Monkey on a specific service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/enable",
        method="POST",
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code != codes.ok:
        raise FailedActivity(f"Enable ChaosMonkey failed: {response.text}")

    return response.text


def disable_chaosmonkey(
    base_url: str,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> str:
    """
    Disable Chaos Monkey on a specific service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/disable",
        method="POST",
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code != codes.ok:
        raise FailedActivity(f"Disable ChaosMonkey failed: {response.text}")

    return response.text


def change_assaults_configuration(
    base_url: str,
    assaults_configuration: Dict[str, Any],
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> str:
    """
    Change Assaults configuration on a specific service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/assaults",
        method="POST",
        assaults_configuration=assaults_configuration,
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code != codes.ok:
        raise FailedActivity(
            f"Change ChaosMonkey Assaults Configuration failed: {response.text}"
        )

    return response.text
