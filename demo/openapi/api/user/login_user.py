from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...types import UNSET, Unset


class Loginuser:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        username: Union[Unset, None, str] = UNSET,
        password: Union[Unset, None, str] = UNSET,
    ) -> Dict[str, Any]:
        url = "{}/user/login".format(self.client.base_url)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        params: Dict[str, Any] = {}
        params["username"] = username

        params["password"] = password

        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

        return {
            "method": "get",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
            "params": params,
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[Union[Any, str]]:
        if response.status_code == HTTPStatus.OK:
            response_200 = cast(str, response.json())
            return response_200
        if response.status_code == HTTPStatus.BAD_REQUEST:
            response_400 = cast(Any, None)
            return response_400
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self,
        username: Union[Unset, None, str] = UNSET,
        password: Union[Unset, None, str] = UNSET,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Logs user into the system

        Args:
            username (Union[Unset, None, str]):
            password (Union[Unset, None, str]):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            hppx.Response
        """

        kwargs = self._get_kwargs(
            username=username,
            password=password,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    def sync(
        self,
        username: Union[Unset, None, str] = UNSET,
        password: Union[Unset, None, str] = UNSET,
    ) -> Optional[Union[Any, str]]:
        """Logs user into the system

        Args:
            username (Union[Unset, None, str]):
            password (Union[Unset, None, str]):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, str]
        """

        return sync_detailed(
            username=username,
            password=password,
        ).parsed

    async def asyncio_detailed(
        self,
        username: Union[Unset, None, str] = UNSET,
        password: Union[Unset, None, str] = UNSET,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Logs user into the system

        Args:
            username (Union[Unset, None, str]):
            password (Union[Unset, None, str]):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            hppx.Response
        """

        kwargs = self._get_kwargs(
            username=username,
            password=password,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
        username: Union[Unset, None, str] = UNSET,
        password: Union[Unset, None, str] = UNSET,
    ) -> Optional[Union[Any, str]]:
        """Logs user into the system

        Args:
            username (Union[Unset, None, str]):
            password (Union[Unset, None, str]):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, str]
        """

        return (
            await asyncio_detailed(
                username=username,
                password=password,
            )
        ).parsed
