# import all the relevant classes
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
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
				size_hint = (None, None), size = (300, 300))
	window.open()

# class to accept user info and validate it
class loginWindow(Screen):
	email = ObjectProperty(None)
	pwd = ObjectProperty(None)
	def validate(self):

		# validating if the email already exists
		if self.email.text not in users['Email'].unique():
			popFun()
		else:

			# switching the current screen to display validation result
			sm.current = 'logdata'

			# reset TextInput widget
			self.email.text = ""
			self.pwd.text = ""


# class to accept sign up info
class signupWindow(Screen):
	username = ObjectProperty(None)
	password = ObjectProperty(None)
	full_name = ObjectProperty(None)
	dob = ObjectProperty(None)
	city = ObjectProperty(None)
	phone_number = ObjectProperty(None)

	def signupbtn(self):

		new_customer: Customer = Customer(
			self.username.text,
			self.password.text,
			self.full_name.text,
			self.dob.text,
			self.city.text,
			self.phone_number.text
		)

		try:
			customer_service.register_customer(new_customer)
		except Exception:
			popFun()

		# creating a DataFrame of the info
		# user = pd.DataFrame([[self.username.text, self.full_name.text, self.password.text]],
		# 					columns = ['Name', 'Email', 'Password'])
		# if self.full_name.text != "":
		# 	if self.full_name.text not in users['Email'].unique():

		# 		# if email does not exist already then append to the csv file
		# 		# change current screen to log in the user now
		# 		user.to_csv('login.csv', mode = 'a', header = False, index = False)
		# 		sm.current = 'login'
		# 		self.username.text = ""
		# 		self.full_name.text = ""
		# 		self.password.text = ""
		# else:
		# 	# if values are empty or invalid show pop up
		# 	popFun()

# class to display validation result
class logDataWindow(Screen):
	pass

# class for managing screens
class windowManager(ScreenManager):
	pass

# kv file
kv = Builder.load_file('login.kv')
sm = windowManager()

# reading all the data stored
# users=pd.read_csv('login.csv')

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
