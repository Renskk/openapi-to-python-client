from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...types import UNSET, Unset


class Deletepet:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        pet_id: int,
        api_key: Union[Unset, str] = UNSET,
    ) -> Dict[str, Any]:
        url = "{}/pet/{petId}".format(self.client.base_url, petId=pet_id)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        if not isinstance(api_key, Unset):
            headers["api_key"] = api_key

        return {
            "method": "delete",
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "timeout": self.client.get_timeout(),
        }

    def _parse_response(
        self, *, response: httpx.Response, raise_on_unexpected_status: bool
    ) -> Optional[Any]:
        if response.status_code == HTTPStatus.BAD_REQUEST:
            return None
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self,
        pet_id: int,
        api_key: Union[Unset, str] = UNSET,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Deletes a pet

         delete a pet

        Args:
            pet_id (int):
            api_key (Union[Unset, str]):
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
            api_key=api_key,
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
        pet_id: int,
        api_key: Union[Unset, str] = UNSET,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Deletes a pet

         delete a pet

        Args:
            pet_id (int):
            api_key (Union[Unset, str]):
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
            api_key=api_key,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response
