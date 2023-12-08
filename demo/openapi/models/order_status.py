from enum import Enum


class OrderStatus(str, Enum):
    APPROVED = "approved"
    DELIVERED = "delivered"
    PLACED = "placed"

    def __str__(self) -> str:
        return str(self.value)
