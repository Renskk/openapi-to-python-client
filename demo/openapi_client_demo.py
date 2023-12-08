import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))


from demo.openapi import Client
from demo.openapi.models import User

base_url = "https://petstore3.swagger.io/api/v3"

client = Client(base_url=base_url)
user_data = client.create_user.sync_detailed(
    form_data=User(),
    json_body=User(
        id=10,
        username="tom",
        first_name="John",
        last_name="James",
        email="john@email.com",
        password="12345",
        phone="12345",
        user_status=1,
    ),
).json()
print(user_data)
