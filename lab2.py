# import all the relevant classes
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from customer import Customer

import customer_service

# class to call the popup function
class PopupWindow(Widget):
	def btn(self):
		popFun()

# class to build GUI for a popup window
class P(FloatLayout):
	pass

# function that displays the content
def popFun():
	show = P()
	window = Popup(title = "popup", content = show,
				size_hint = (None, None), size = (600, 600))
	window.open()

# class to accept user info and validate it
class loginWindow(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)
	def validate(self):
		if (customer_service.auth_customer(self.username.text, self.password.text)):
			sm.current = 'logdata'
			self.username.text = ""
			self.password.text = ""
		else:
			popFun()


# class to accept sign up info
class signupWindow(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)
	full_name = ObjectProperty(None)
	dob = ObjectProperty(None)
	city = ObjectProperty(None)
	phone_number = ObjectProperty(None)

	def signupbtn(self):
		try:
			new_customer: Customer = self._create_customer_from_input()

			customer_service.register_customer(new_customer)

			sm.current = 'login'

			self._clear_input_fields()

		except Exception:
			popFun()


	def _create_customer_from_input(self) -> Customer:
		return Customer(
			self.username.text,
			self.password.text,
			self.full_name.text,
			self.dob.text,
			self.city.text,
			self.phone_number.text
		)


	def _clear_input_fields(self) -> None:
		self.username.text = ""
		self.password.text = ""
		self.full_name.text = ""
		self.dob.text = ""
		self.city.text = ""
		self.phone_number.text = ""

# class to display validation result
class logDataWindow(Screen):
	pass

# class for managing screens
class windowManager(ScreenManager):
	pass

# kv file
kv = Builder.load_file('login.kv')
sm = windowManager()

# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))

# class that builds gui
class loginMain(App):
	def build(self):
		return sm

# driver function
if __name__=="__main__":
	loginMain().run()
