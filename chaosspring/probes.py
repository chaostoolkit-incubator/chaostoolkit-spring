from typing import Any, Dict

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
from requests.status_codes import codes

from chaosspring import api

__all__ = ["chaosmonkey_enabled", "watcher_configuration", "assaults_configuration"]


def chaosmonkey_enabled(
    base_url: str,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> bool:
    """
    Enquire whether Chaos Monkey is enabled on the
    specified service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/status",
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code == codes.ok:
        return True
    elif response.status_code == codes.service_unavailable:
        return False
    else:
        raise FailedActivity(f"ChaosMonkey status enquiry failed: {response.text}")


def watcher_configuration(
    base_url: str,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Dict[str, Any]:
    """
    Get the current watcher configuraton from the specified service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/watcher",
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code != codes.ok:
        raise FailedActivity(f"ChaosMonkey watcher enquiry failed: {response.text}")

    return response.json()


def assaults_configuration(
    base_url: str,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify_ssl: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Dict[str, Any]:
    """
    Get the current assaults configuraton from the specified service.
    """

    response = api.call_api(
        base_url=base_url,
        api_endpoint="chaosmonkey/assaults",
        headers=headers,
        timeout=timeout,
        verify=verify_ssl,
        configuration=configuration,
        secrets=secrets,
    )

    if response.status_code != codes.ok:
        raise FailedActivity(f"ChaosMonkey assaults enquiry failed: {response.text}")

    return response.json()
