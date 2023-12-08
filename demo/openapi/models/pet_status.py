from enum import Enum


class PetStatus(str, Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
