import dataclasses


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    number: str
    day: str
    month: str
    year: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str