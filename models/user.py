from dataclasses import dataclass, asdict
import bcrypt
from typing import Tuple

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    phone: str
    is_admin: bool = False  # hard coaded to always Customer=True

    # to access data using dict
    # self points to the current instance (is kind of equals to this keyword)
    def to_dict(self):
        # converts User to dictionary
        data = asdict(self)
        del data['password']
        # data["is_admin"] = "YES" if self.is_admin else "NO"
        del data['is_admin']
        return data

    # pythonc version of java constructor
    @classmethod
    def from_row(cls, row: Tuple) -> "User": 
        # return cls(*row) -> unpacks tuple into User (the sequence of data has to be accurate)
        return cls(
            id = row[0],
            name = row[1],
            email = row[2],
            password = row[3],
            is_admin = row[4],
            phone = row[6],
        )