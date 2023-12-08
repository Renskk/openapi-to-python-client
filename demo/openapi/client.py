import ssl
from typing import Dict, Union

import attr

from demo.openapi.api.pet.add_pet import Addpet
from demo.openapi.api.pet.delete_pet import Deletepet
from demo.openapi.api.pet.find_pets_by_status import Findpetsbystatus
from demo.openapi.api.pet.find_pets_by_tags import Findpetsbytags
from demo.openapi.api.pet.get_pet_by_id import Getpetbyid
from demo.openapi.api.pet.update_pet import Updatepet
from demo.openapi.api.pet.update_pet_with_form import Updatepetwithform
from demo.openapi.api.pet.upload_file import Uploadfile
from demo.openapi.api.store.delete_order import Deleteorder
from demo.openapi.api.store.get_inventory import Getinventory
from demo.openapi.api.store.get_order_by_id import Getorderbyid
from demo.openapi.api.store.place_order import Placeorder
from demo.openapi.api.user.create_user import Createuser
from demo.openapi.api.user.create_users_with_list_input import Createuserswithlistinput
from demo.openapi.api.user.delete_user import Deleteuser
from demo.openapi.api.user.get_user_by_name import Getuserbyname
from demo.openapi.api.user.login_user import Loginuser
from demo.openapi.api.user.logout_user import Logoutuser
from demo.openapi.api.user.update_user import Updateuser


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
    """

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)

    @property
    def update_pet(self) -> Updatepet:
        if not hasattr(self, "_update_pet"):
            self._update_pet = Updatepet(client=self)
        return self._update_pet

    @property
    def add_pet(self) -> Addpet:
        if not hasattr(self, "_add_pet"):
            self._add_pet = Addpet(client=self)
        return self._add_pet

    @property
    def find_pets_by_status(self) -> Findpetsbystatus:
        if not hasattr(self, "_find_pets_by_status"):
            self._find_pets_by_status = Findpetsbystatus(client=self)
        return self._find_pets_by_status

    @property
    def find_pets_by_tags(self) -> Findpetsbytags:
        if not hasattr(self, "_find_pets_by_tags"):
            self._find_pets_by_tags = Findpetsbytags(client=self)
        return self._find_pets_by_tags

    @property
    def get_pet_by_id(self) -> Getpetbyid:
        if not hasattr(self, "_get_pet_by_id"):
            self._get_pet_by_id = Getpetbyid(client=self)
        return self._get_pet_by_id

    @property
    def update_pet_with_form(self) -> Updatepetwithform:
        if not hasattr(self, "_update_pet_with_form"):
            self._update_pet_with_form = Updatepetwithform(client=self)
        return self._update_pet_with_form

    @property
    def delete_pet(self) -> Deletepet:
        if not hasattr(self, "_delete_pet"):
            self._delete_pet = Deletepet(client=self)
        return self._delete_pet

    @property
    def upload_file(self) -> Uploadfile:
        if not hasattr(self, "_upload_file"):
            self._upload_file = Uploadfile(client=self)
        return self._upload_file

    @property
    def get_inventory(self) -> Getinventory:
        if not hasattr(self, "_get_inventory"):
            self._get_inventory = Getinventory(client=self)
        return self._get_inventory

    @property
    def place_order(self) -> Placeorder:
        if not hasattr(self, "_place_order"):
            self._place_order = Placeorder(client=self)
        return self._place_order

    @property
    def get_order_by_id(self) -> Getorderbyid:
        if not hasattr(self, "_get_order_by_id"):
            self._get_order_by_id = Getorderbyid(client=self)
        return self._get_order_by_id

    @property
    def delete_order(self) -> Deleteorder:
        if not hasattr(self, "_delete_order"):
            self._delete_order = Deleteorder(client=self)
        return self._delete_order

    @property
    def create_user(self) -> Createuser:
        if not hasattr(self, "_create_user"):
            self._create_user = Createuser(client=self)
        return self._create_user

    @property
    def create_users_with_list_input(self) -> Createuserswithlistinput:
        if not hasattr(self, "_create_users_with_list_input"):
            self._create_users_with_list_input = Createuserswithlistinput(client=self)
        return self._create_users_with_list_input

    @property
    def login_user(self) -> Loginuser:
        if not hasattr(self, "_login_user"):
            self._login_user = Loginuser(client=self)
        return self._login_user

    @property
    def logout_user(self) -> Logoutuser:
        if not hasattr(self, "_logout_user"):
            self._logout_user = Logoutuser(client=self)
        return self._logout_user

    @property
    def get_user_by_name(self) -> Getuserbyname:
        if not hasattr(self, "_get_user_by_name"):
            self._get_user_by_name = Getuserbyname(client=self)
        return self._get_user_by_name

    @property
    def update_user(self) -> Updateuser:
        if not hasattr(self, "_update_user"):
            self._update_user = Updateuser(client=self)
        return self._update_user

    @property
    def delete_user(self) -> Deleteuser:
        if not hasattr(self, "_delete_user"):
            self._delete_user = Deleteuser(client=self)
        return self._delete_user


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}
