from customer import Customer
import customer_repository
import re


def register_customer(customer: Customer) -> bool:
	_validate_password(customer.password)
	try:
		customer._replace(password=_process_hash(customer.password))
		customer_repository.save_customer(customer)
		return True
	except Exception:
		return False


def update_password(customer: Customer, new_password: str) -> bool:
	_validate_password(new_password)
	try:
		customer._replace(password=_process_hash(new_password))

		customer_repository.update_customer(customer)

		return True
	except Exception:
		return False


def auth_customer(username: str, password: str) -> bool:
	try:
		customer: Customer = customer_repository.get_customer_by_username(username)
		return True if _process_hash(password) == _process_hash(customer.password) else False
	except Exception:
		return False


def _validate_password(password: str):
	if not re.search('\d+', password):
		raise Exception("Wrong password format! Must cotain only digits")


def _process_hash(row_password: str) -> int:
	hashed_password: int = 0

	for digit in row_password:
		hashed_password += int(digit)

	return hashed_password
