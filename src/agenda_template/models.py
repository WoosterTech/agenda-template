import enum
from datetime import date

from pydantic import BaseModel, EmailStr, create_model, field_validator


class ChurchEnum(enum.StrEnum):
    KENNEWICK = "K"
    PASCO = "P"
    RICHLAND = "R"


class Church(BaseModel):
    name: str
    positions: int

    @field_validator("elected", mode="after")
    @classmethod
    def populate_elected(cls, value: list["Member | None"]) -> list["Member | None"]:
        if (count := len(value)) == cls.positions:
            return value
        return value + [None] * (cls.positions - count)

    @property
    def abbreviation(self) -> str:
        return self.name[0].upper()

    @classmethod
    def factory(cls, name: str, positions: int):
        model_name = 
        new_model = create_model()


class Member(BaseModel):
    name: str
    email: EmailStr
