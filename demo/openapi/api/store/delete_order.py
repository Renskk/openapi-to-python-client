from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors


class Deleteorder:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        order_id: int,
    ) -> Dict[str, Any]:
        url = "{}/store/order/{orderId}".format(self.client.base_url, orderId=order_id)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

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
        if response.status_code == HTTPStatus.NOT_FOUND:
            return None
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(
        self, order_id: int, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Delete purchase order by ID

         For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will
        generate API errors

        Args:
            order_id (int):
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
            order_id=order_id,
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
        self, order_id: int, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Delete purchase order by ID

         For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will
        generate API errors

        Args:
            order_id (int):
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
            order_id=order_id,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response
