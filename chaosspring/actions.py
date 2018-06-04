# -*- coding: utf-8 -*-
from chaoslib.types import Configuration, Secrets
import requests

__all__ = ["enable_chaosmonkey", "disable_chaosmonkey"]


def enable_chaosmonkey(base_url: str, timeout: float = None,
                       configuration: Configuration = None,
                       secrets: Secrets = None):
    """
    Enable Chaos Monkey on a specific service
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


def disable_chaosmonkey(base_url: str, timeout: float = None,
                        configuration: Configuration = None,
                        secrets: Secrets = None):
    """
    Disable Chaos Monkey on a specific service
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
