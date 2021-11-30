import sqlite3
from customer import Customer


def save_customer(customer: Customer) -> Customer:
	print(f'Saving {customer=}')

	query: str = """INSERT INTO customer (username, password, full_name, dob, city, phone_number) VALUES (?, ?, ?, ?, ?, ?)"""
	_query_executor(query, customer)

	return customer


def update_customer(customer: Customer) -> Customer:
	print(f'Updating {customer=}')

	query: str = """UPDATE customer (username, password, full_name, dob, city, phone_number) VALUES (?, ?, ?, ?, ?, ?)"""
	_query_executor(query, customer)

	return customer


def get_customer_by_username(username: str) -> Customer:
	print(f'Getting customer by {username=}')

	con = sqlite3.connect('customers.db')
	cur = con.cursor()

	query: str = """SELECT * FROM customer WHERE username=?"""
	cur.execute(query, (username,))
	customer = cur.fetchone()

	if (customer == None):
		raise Exception(f'No customer with {username=}')


	print(f'{customer=}')
	res = Customer(
		customer[1],
		customer[6],
		customer[2],
		customer[3],
		customer[4],
		customer[5],
	)

	print(f"{res=}")
	return res


def _query_executor(query: str, data: tuple) -> None:
	con = sqlite3.connect('customers.db')
	cur = con.cursor()
	cur.execute(query, data)
	con.commit()
	con.close()


if __name__ == "__main__":
	c: Customer = Customer(
		'username',
		'password',
		'fullname',
		'01.01.1970',
		'city',
		'phone_number'
	)

	save_customer(c)
	new_customer: Customer = get_customer_by_username('lalala')
	print(f'{new_customer=}')
