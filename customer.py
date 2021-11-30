from typing import NamedTuple


class Customer(NamedTuple):
	id: int
	username: str
	password: str
	full_name: str
	dob: str
	city: str
	phone_number: str
