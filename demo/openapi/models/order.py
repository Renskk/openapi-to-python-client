import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_status import OrderStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 10.
        pet_id (Union[Unset, int]):  Example: 198772.
        quantity (Union[Unset, int]):  Example: 7.
        ship_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, OrderStatus]): Order Status Example: approved.
        complete (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    pet_id: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    ship_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, OrderStatus] = UNSET
    complete: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        pet_id = self.pet_id
        quantity = self.quantity
        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        complete = self.complete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if pet_id is not UNSET:
            field_dict["petId"] = pet_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date
        if status is not UNSET:
            field_dict["status"] = status
        if complete is not UNSET:
            field_dict["complete"] = complete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        pet_id = d.pop("petId", UNSET)

        quantity = d.pop("quantity", UNSET)

        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderStatus(_status)

        complete = d.pop("complete", UNSET)

        order = cls(
            id=id,
            pet_id=pet_id,
            quantity=quantity,
            ship_date=ship_date,
            status=status,
            complete=complete,
        )

        order.additional_properties = d
        return order

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
