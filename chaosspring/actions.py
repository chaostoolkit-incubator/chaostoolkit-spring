# -*- coding: utf-8 -*-
from typing import Any, Dict
import json

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets
import requests

__all__ = ["enable_chaosmonkey",
           "disable_chaosmonkey",
           "change_assaults_configuration"]


def enable_chaosmonkey(base_url: str, timeout: float = None,
                       configuration: Configuration = None,
                       secrets: Secrets = None) -> str:
    """
    Enable Chaos Monkey on a specific service.
    """

    url = "{base_url}/chaosmonkey/enable".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.post(
        url, headers={"Accept": "application/json"}, params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "Enable ChaosMonkey failed: {m}".format(m=r.text))

    return r.text


def disable_chaosmonkey(base_url: str, timeout: float = None,
                        configuration: Configuration = None,
                        secrets: Secrets = None) -> str:
    """
    Disable Chaos Monkey on a specific service.
    """

    url = "{base_url}/chaosmonkey/disable".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.post(
        url, headers={"Accept": "application/json"}, params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "Disable ChaosMonkey failed: {m}".format(m=r.text))

    return r.text


def change_assaults_configuration(base_url: str,
                                  assaults_configuration: Dict[str, Any],
                                  timeout: float = None,
                                  configuration: Configuration = None,
                                  secrets: Secrets = None) -> str:
    """
    Change Assaults configuration on a specific service.
    """

    url = "{base_url}/chaosmonkey/assaults".format(base_url=base_url)

    params = {}

    if timeout is not None:
        params["timeout"] = timeout

    r = requests.post(
        url, headers={"Accept": "application/json",
                      "Content-Type": "application/json"},
        data=json.dumps(assaults_configuration), params=params)

    if r.status_code != 200:
        raise FailedActivity(
            "Change ChaosMonkey Assaults Configuration failed: {m}".format(
                m=r.text))

    return r.text
