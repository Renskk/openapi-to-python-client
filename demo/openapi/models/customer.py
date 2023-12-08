from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="Customer")


@attr.s(auto_attribs=True)
class Customer:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 100000.
        username (Union[Unset, str]):  Example: fehguy.
        address (Union[Unset, List['Address']]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    address: Union[Unset, List["Address"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        address: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.address, Unset):
            address = []
            for address_item_data in self.address:
                address_item = address_item_data.to_dict()

                address.append(address_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        address = []
        _address = d.pop("address", UNSET)
        for address_item_data in _address or []:
            address_item = Address.from_dict(address_item_data)

            address.append(address_item)

        customer = cls(
            id=id,
            username=username,
            address=address,
        )

        customer.additional_properties = d
        return customer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
