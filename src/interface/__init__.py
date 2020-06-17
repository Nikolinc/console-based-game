from . import exception
import time


class Interface:
	def __init__(self):
		pass

	def sleep(self, delay: int) -> None:
		time.sleep(delay)

	def input(self) -> str:
		return input(">>> ")

	def print(self, lines: "list, str", delay: int = 0) -> None:
		if isinstance(lines, str):
			lines = [lines]
		for line in lines:
			print(line)
			self.sleep(delay)

	def _check_permitted_answers_validity(self, permitted_answers: dict) -> bool:
		if not isinstance(permitted_answers, dict):
			for permitted_answer in permitted_answers:
				if not isinstance(permitted_answer, list):
					return False
		return True

	def ask(self, question: str, permitted_answers: dict) -> "int, str, bool":
		"""
		PlEASE: don't use int and bool values in dict at the same time!
		This can cause problems.
		Problem dict example:
			d={
				0: ['int'],
				False: ['bool'],
				1: ['int'],
				True: ['bool']
			}
		Try to understand what is wrong :)
		"""
		if not self._check_permitted_answers_validity:
			raise exception.InvalidFormatForDict()

		while True:
			self.print(question)
			answer = self.input().lower()
			for permitted_answer in permitted_answers:
				if answer in permitted_answers[permitted_answer]:
					return permitted_answer

	def create_readable_text(self, permitted_answers: dict) -> str:
		"""
		PlEASE: don't use int and bool values in dict at the same time!
		This can cause problems.
		Problem dict example:
			d={
				0: ['int'],
				False: ['bool'],
				1: ['int'],
				True: ['bool']
			}
		Try to understand what is wrong :)
		"""
		if not self._check_permitted_answers_validity:
			raise exception.InvalidFormatForDict()

		text = "Ты должен ввести:\n\t"
		for permitted_answer in permitted_answers:
			for answer in permitted_answers[permitted_answer]:
				text += f'"{answer}", '

			if isinstance(permitted_answer, bool):
				bool_name = 'Да' if permitted_answer else 'Нет'
				text += f'чтобы выбрать вариант "{bool_name}"\n\t'
			elif isinstance(permitted_answer, int):
				text += f'чтобы выбрать {permitted_answer} вариант\n\t'
			elif isinstance(permitted_answer, str):
				text += f'чтобы выбрать "{permitted_answer}"\n\t'

		return text[:-2]  # cuts last "\n\t" symbols


if __name__ == '__main__':
	pass
