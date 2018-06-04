# -*- coding: utf-8 -*-

import requests

from chaoslib.types import Configuration, Secrets

__all__ = ["chaosmonkey_enabled"]


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
