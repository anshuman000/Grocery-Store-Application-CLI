from dataclasses import dataclass

@dataclass
class Order:
    def to_dict():
        pass

    @classmethod
    def from_row(cls, row: tuple) -> "Order":
        pass