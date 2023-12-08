from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...models.get_inventory_response_200 import GetInventoryResponse200


class Getinventory:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
    ) -> Dict[str, Any]:
        url = "{}/store/inventory".format(self.client.base_url)

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
    ) -> Optional[GetInventoryResponse200]:
        if response.status_code == HTTPStatus.OK:
            response_200 = GetInventoryResponse200.from_dict(response.json())

            return response_200
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(self, raise_on_unexpected_status: bool = False) -> httpx.Response:
        """Returns pet inventories by status

         Returns a map of status codes to quantities

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            hppx.Response
        """

        kwargs = self._get_kwargs()

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
    ) -> Optional[GetInventoryResponse200]:
        """Returns pet inventories by status

         Returns a map of status codes to quantities

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            GetInventoryResponse200
        """

        return sync_detailed().parsed

    async def asyncio_detailed(
        self, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Returns pet inventories by status

         Returns a map of status codes to quantities

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            hppx.Response
        """

        kwargs = self._get_kwargs()

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
    ) -> Optional[GetInventoryResponse200]:
        """Returns pet inventories by status

         Returns a map of status codes to quantities

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            GetInventoryResponse200
        """

        return (await asyncio_detailed()).parsed
