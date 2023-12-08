from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...models.pet import Pet


class Getpetbyid:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        pet_id: int,
    ) -> Dict[str, Any]:
        url = "{}/pet/{petId}".format(self.client.base_url, petId=pet_id)

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
    ) -> Optional[Union[Any, Pet]]:
        if response.status_code == HTTPStatus.OK:
            response_200 = Pet.from_dict(response.json())

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
        self, pet_id: int, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Find pet by ID

         Returns a single pet

        Args:
            pet_id (int):
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
            pet_id=pet_id,
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
        pet_id: int,
    ) -> Optional[Union[Any, Pet]]:
        """Find pet by ID

         Returns a single pet

        Args:
            pet_id (int):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, Pet]
        """

        return sync_detailed(
            pet_id=pet_id,
        ).parsed

    async def asyncio_detailed(
        self, pet_id: int, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Find pet by ID

         Returns a single pet

        Args:
            pet_id (int):
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
            pet_id=pet_id,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
        pet_id: int,
    ) -> Optional[Union[Any, Pet]]:
        """Find pet by ID

         Returns a single pet

        Args:
            pet_id (int):
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, Pet]
        """

        return (
            await asyncio_detailed(
                pet_id=pet_id,
            )
        ).parsed
