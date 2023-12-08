from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...models.pet import Pet


class Addpet:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        form_data: Pet,
        json_body: Pet,
    ) -> Dict[str, Any]:
        url = "{}/pet".format(self.client.base_url)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        json_body.to_dict()

        return {
            "method": "post",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
            "data": form_data.to_dict(),
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[Union[Any, Pet]]:
        if response.status_code == HTTPStatus.OK:
            response_200 = Pet.from_dict(response.json())

            return response_200
        if response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
            response_405 = cast(Any, None)
            return response_405
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self, form_data: Pet, json_body: Pet, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Add a new pet to the store

         Add a new pet to the store

        Args:
            json_body (Pet):
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

    def sync(
        self,
        form_data: Pet,
        json_body: Pet,
    ) -> Optional[Union[Any, Pet]]:
        """Add a new pet to the store

         Add a new pet to the store

        Args:
            json_body (Pet):
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
            form_data=form_data,
            json_body=json_body,
        ).parsed

    async def asyncio_detailed(
        self, form_data: Pet, json_body: Pet, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Add a new pet to the store

         Add a new pet to the store

        Args:
            json_body (Pet):
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
            form_data=form_data,
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
        form_data: Pet,
        json_body: Pet,
    ) -> Optional[Union[Any, Pet]]:
        """Add a new pet to the store

         Add a new pet to the store

        Args:
            json_body (Pet):
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
                form_data=form_data,
                json_body=json_body,
            )
        ).parsed
