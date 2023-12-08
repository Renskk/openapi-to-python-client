from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...models.user import User


class Createuserswithlistinput:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        json_body: List["User"],
    ) -> Dict[str, Any]:
        url = "{}/user/createWithList".format(self.client.base_url)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        json_json_body = []
        for json_body_item_data in json_body:
            json_body_item = json_body_item_data.to_dict()

            json_json_body.append(json_body_item)

        return {
            "method": "post",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
            "json": json_json_body,
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[User]:
        if response.status_code == HTTPStatus.OK:
            response_200 = User.from_dict(response.json())

            return response_200
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self, json_body: List["User"], raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Creates list of users with given input array

         Creates list of users with given input array

        Args:
            json_body (List['User']):
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

    def sync(
        self,
        json_body: List["User"],
    ) -> Optional[User]:
        """Creates list of users with given input array

         Creates list of users with given input array

        Args:
            json_body (List['User']):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            User
        """

        return sync_detailed(
            json_body=json_body,
        ).parsed

    async def asyncio_detailed(
        self, json_body: List["User"], raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Creates list of users with given input array

         Creates list of users with given input array

        Args:
            json_body (List['User']):
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
            json_body=json_body,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
        json_body: List["User"],
    ) -> Optional[User]:
        """Creates list of users with given input array

         Creates list of users with given input array

        Args:
            json_body (List['User']):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            User
        """

        return (
            await asyncio_detailed(
                json_body=json_body,
            )
        ).parsed
