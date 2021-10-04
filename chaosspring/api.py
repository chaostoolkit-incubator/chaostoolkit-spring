import json
from typing import Any, Dict

import requests
from chaoslib.types import Configuration, Secrets
from requests import Response


def call_api(
    base_url: str,
    api_endpoint: str,
    method: str = "GET",
    assaults_configuration: Dict[str, Any] = None,
    headers: Dict[str, Any] = None,
    timeout: float = None,
    verify: bool = True,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Response:
    """common http api call to spring boot chaos monkey. Both actions and
    probes call spring boot chaos monkey rest api by using this function.

    :param base_url: base url of target application
    :param api_endpoint: spring boot chaos monkey actuator endpoint
    :param method: Http method, default is 'GET'
    :param headers: Additional headers when calling spring boot chaos monkey
            rest api
    :param assaults_configuration: assaults configuration to change spring
            boot chaos monkey setting
    :param timeout: the waiting time before connection timeout
    :param verify: bool representing whether requests performs SSL Verification
        (For providing trusted CAs, see
        https://github.com/chaostoolkit-incubator/chaostoolkit-spring#ssl-verification)
    :param configuration: It provides runtime value to actions and probes in
            Key/value, it may contains platform
                    specific api parameters.
    :param secrets: It declare values that need to be passed on to Actions or
            Probes in secure manner, for example auth token.
    :return: return requests.Response
    """

    url = f"{base_url}/{api_endpoint}"

    headers = headers or {}
    headers.setdefault("Accept", "application/json")

    params = {"verify": verify}
    if timeout:
        params["timeout"] = timeout

    data = None
    if assaults_configuration:
        data = json.dumps(assaults_configuration)
        headers.update({"Content-Type": "application/json"})

    return requests.request(
        method=method, url=url, params=params, data=data, headers=headers
    )
