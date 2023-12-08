from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...models.user import User


class Getuserbyname:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        username: str,
    ) -> Dict[str, Any]:
        url = "{}/user/{username}".format(self.client.base_url, username=username)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        return {
            "method": "get",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[Union[Any, User]]:
        if response.status_code == HTTPStatus.OK:
            response_200 = User.from_dict(response.json())

            return response_200
        if response.status_code == HTTPStatus.BAD_REQUEST:
            response_400 = cast(Any, None)
            return response_400
        if response.status_code == HTTPStatus.NOT_FOUND:
            response_404 = cast(Any, None)
            return response_404
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self, username: str, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Get user by user name

        Args:
            username (str):
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
        username: str,
    ) -> Optional[Union[Any, User]]:
        """Get user by user name

        Args:
            username (str):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, User]
        """

        return sync_detailed(
            username=username,
        ).parsed

    async def asyncio_detailed(
        self, username: str, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Get user by user name

        Args:
            username (str):
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
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
        username: str,
    ) -> Optional[Union[Any, User]]:
        """Get user by user name

        Args:
            username (str):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, User]
        """

        return (
            await asyncio_detailed(
                username=username,
            )
        ).parsed
