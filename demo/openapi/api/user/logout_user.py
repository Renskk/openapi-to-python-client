from typing import Any, Dict, Optional

import httpx

from ... import errors


class Logoutuser:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
    ) -> Dict[str, Any]:
        url = "{}/user/logout".format(self.client.base_url)

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
    ) -> Optional[Any]:
        if raise_on_unexpected_status:
            raise errors.UnexpectedStatus(response.status_code, response.content)
        else:
            return None

    def sync_detailed(self, raise_on_unexpected_status: bool = False) -> httpx.Response:
        """Logs out current logged in user session

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

    async def asyncio_detailed(
        self, raise_on_unexpected_status: bool = False
    ) -> httpx.Response:
        """Logs out current logged in user session

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
