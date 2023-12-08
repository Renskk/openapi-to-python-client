from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...models.find_pets_by_status_status import FindPetsByStatusStatus
from ...models.pet import Pet
from ...types import UNSET, Unset


class Findpetsbystatus:
    def __init__(self, client):
        self.client = client

    def _get_kwargs(
        self,
        status: Union[
            Unset, None, FindPetsByStatusStatus
        ] = FindPetsByStatusStatus.AVAILABLE,
    ) -> Dict[str, Any]:
        url = "{}/pet/findByStatus".format(self.client.base_url)

        headers: Dict[str, str] = self.client.get_headers()
        cookies: Dict[str, Any] = self.client.get_cookies()

        params: Dict[str, Any] = {}
        json_status: Union[Unset, None, str] = UNSET
        if not isinstance(status, Unset):
            json_status = status.value if status else None

        params["status"] = json_status

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
    ) -> Optional[Union[Any, List["Pet"]]]:
        if response.status_code == HTTPStatus.OK:
            response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Pet.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
        status: Union[
            Unset, None, FindPetsByStatusStatus
        ] = FindPetsByStatusStatus.AVAILABLE,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Finds Pets by status

         Multiple status values can be provided with comma separated strings

        Args:
            status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
                FindPetsByStatusStatus.AVAILABLE.
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
            status=status,
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
        status: Union[
            Unset, None, FindPetsByStatusStatus
        ] = FindPetsByStatusStatus.AVAILABLE,
    ) -> Optional[Union[Any, List["Pet"]]]:
        """Finds Pets by status

         Multiple status values can be provided with comma separated strings

        Args:
            status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
                FindPetsByStatusStatus.AVAILABLE.
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, List['Pet']]
        """

        return sync_detailed(
            status=status,
        ).parsed

    async def asyncio_detailed(
        self,
        status: Union[
            Unset, None, FindPetsByStatusStatus
        ] = FindPetsByStatusStatus.AVAILABLE,
        raise_on_unexpected_status: bool = False,
    ) -> httpx.Response:
        """Finds Pets by status

         Multiple status values can be provided with comma separated strings

        Args:
            status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
                FindPetsByStatusStatus.AVAILABLE.
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
            status=status,
        )

        async with httpx.AsyncClient(verify=self.client.verify_ssl) as _client:
            response = await _client.request(**kwargs)
        self._parse_response(
            response=response, raise_on_unexpected_status=raise_on_unexpected_status
        )

        return response

    async def asyncio(
        self,
        status: Union[
            Unset, None, FindPetsByStatusStatus
        ] = FindPetsByStatusStatus.AVAILABLE,
    ) -> Optional[Union[Any, List["Pet"]]]:
        """Finds Pets by status

         Multiple status values can be provided with comma separated strings

        Args:
            status (Union[Unset, None, FindPetsByStatusStatus]):  Default:
                FindPetsByStatusStatus.AVAILABLE.
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
                    status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
                    argument to the constructor.
        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[Any, List['Pet']]
        """

        return (
            await asyncio_detailed(
                status=status,
            )
        ).parsed
