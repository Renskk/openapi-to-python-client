from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.pet_status import PetStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.tag import Tag


T = TypeVar("T", bound="Pet")


@attr.s(auto_attribs=True)
class Pet:
    """
    Attributes:
        name (str):  Example: doggie.
        photo_urls (List[str]):
        id (Union[Unset, int]):  Example: 10.
        category (Union[Unset, Category]):
        tags (Union[Unset, List['Tag']]):
        status (Union[Unset, PetStatus]): pet status in the store
    """

    name: str
    photo_urls: List[str]
    id: Union[Unset, int] = UNSET
    category: Union[Unset, "Category"] = UNSET
    tags: Union[Unset, List["Tag"]] = UNSET
    status: Union[Unset, PetStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        photo_urls = self.photo_urls

        id = self.id
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "photoUrls": photo_urls,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category import Category
        from ..models.tag import Tag

        d = src_dict.copy()
        name = d.pop("name")

        photo_urls = cast(List[str], d.pop("photoUrls"))

        id = d.pop("id", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, Category]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PetStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PetStatus(_status)

        pet = cls(
            name=name,
            photo_urls=photo_urls,
            id=id,
            category=category,
            tags=tags,
            status=status,
        )

        pet.additional_properties = d
        return pet

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
