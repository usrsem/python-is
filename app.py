from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random

from kivy.uix.textinput import TextInput


class Lab1(App):
	""""
	b1, b2, b3 — случайные цифры; b4, b5 — случайные символы из
	множества {!, ”, #, $, %, &, ’, (, ), *}; b7 — случайная заглавная
	буква  английского  алфавита;  b8 —  P-ая  по  счету  малая  буква
	английского алфавита, где P = N^2 mod10 + N^3 mod10 + 1
	"""


	def build(self):
		root_widget: BoxLayout = BoxLayout(orientation='vertical')

		input_field: TextInput = TextInput(font_size = 50, size_hint_y = None, height = 100)
		output_label: Label = Label(size_hint_y=1, font_size=70)

		clear_button: Button = Button(text='clear', size_hint_y=None, height=100, font_size=50)
		generate_button: Button = Button(text='generate', size_hint_y=None, height=100, font_size=50)


		def clear_label(instance):
			output_label.text = ''
			input_field.text = ''
		clear_button.bind(on_press=clear_label)

		def generate_password(instance):
			output_label.text = self._generate_password(input_field.text)
		generate_button.bind(on_press=generate_password)


		root_widget.add_widget(output_label)
		root_widget.add_widget(input_field)
		root_widget.add_widget(generate_button)
		root_widget.add_widget(clear_button)

		return root_widget

	@staticmethod
	def _generate_password(input: str) -> str:
		password: str = ''
		symbols: list[str] = ['!', '”', '#', '$', '%', '&', '’', '(', ')', '*']
		symbols_len: int = len(symbols)

		N: int = len(input)
		P: int = (N * N) % 10 + (N * N * N) % 10 + 1

		for _ in range(0, 3):
			password += str(random.randint(0, 9))

		for _ in range(0, 2):
			password += symbols[random.randint(0, symbols_len - 1)]

		password += chr(random.randint(65, 90))

		password += chr(96 + P)

		return password


if __name__ == "__main__":
	Lab1().run()
