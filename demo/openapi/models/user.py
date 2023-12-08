from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 10.
        username (Union[Unset, str]):  Example: theUser.
        first_name (Union[Unset, str]):  Example: John.
        last_name (Union[Unset, str]):  Example: James.
        email (Union[Unset, str]):  Example: john@email.com.
        password (Union[Unset, str]):  Example: 12345.
        phone (Union[Unset, str]):  Example: 12345.
        user_status (Union[Unset, int]): User Status Example: 1.
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    user_status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        password = self.password
        phone = self.phone
        user_status = self.user_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if phone is not UNSET:
            field_dict["phone"] = phone
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        phone = d.pop("phone", UNSET)

        user_status = d.pop("userStatus", UNSET)

        user = cls(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone,
            user_status=user_status,
        )

        user.additional_properties = d
        return user

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
