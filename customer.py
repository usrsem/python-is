from typing import NamedTuple


class Customer(NamedTuple):
	username: str
	password: str
	full_name: str
	dob: str
	city: str
	phone_number: str
