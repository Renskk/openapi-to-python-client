from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...models.user import User


class Updateuser:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        username: str,
        form_data: User,
        json_body: User,
    ) -> Dict[str, Any]:
        url = "{}/user/{username}".format(self.client.base_url, username=username)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        json_body.to_dict()

        return {
            "method": "put",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
            "data": form_data.to_dict(),
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[Any]:
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self,
        username: str,
        form_data: User,
        json_body: User,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Update user

         This can only be done by the logged in user.

        Args:
            username (str):
            json_body (User):
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
            form_data=form_data,
            json_body=json_body,
        )

        response = httpx.request(
            verify=self.client.verify_ssl,
            **kwargs,
        )
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio_detailed(
        self,
        username: str,
        form_data: User,
        json_body: User,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Update user

         This can only be done by the logged in user.

        Args:
            username (str):
            json_body (User):
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
            form_data=form_data,
            json_body=json_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response
