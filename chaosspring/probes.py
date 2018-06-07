# -*- coding: utf-8 -*-
from typing import Any, Dict

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
import requests

__all__ = ["chaosmonkey_enabled",
           "watcher_configuration",
           "assaults_configuration"]


def chaosmonkey_enabled(base_url: str, timeout: float = None,
                        configuration: Configuration = None,
                        secrets: Secrets = None) -> bool:
    """
    Enquire whether Chaos Monkey is enabled on the
    specified service.
    """

    url = "{base_url}/chaosmonkey/status".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.get(
        url, headers={"Accept": "application/json"}, params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "ChaosMonkey status enquiry failed: {m}".format(m=r.text))

    if r.text == "You switched me off!":
        return False

    return True


def watcher_configuration(base_url: str, timeout: float = None,
                          configuration: Configuration = None,
                          secrets: Secrets = None) -> Dict[str, Any]:
    """
    Get the current watcher configuraton from the specified service.
    """

    url = "{base_url}/chaosmonkey/watcher".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.get(
        url, headers={"Accept": "application/json"}, params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "ChaosMonkey watcher enquiry failed: {m}".format(m=r.text))

    return r.json()


def assaults_configuration(base_url: str, timeout: float = None,
                           configuration: Configuration = None,
                           secrets: Secrets = None) -> Dict[str, Any]:
    """
    Get the current assaults configuraton from the specified service.
    """

    url = "{base_url}/chaosmonkey/assaults".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.get(
        url, headers={"Accept": "application/json"}, params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "ChaosMonkey assaults enquiry failed: {m}".format(m=r.text))

    return r.json()
