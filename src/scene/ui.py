from src.character.player import Player
from src.character.class_.standart import Warrior, Wizard, Assassin, Cleric, Archer, Paladin, Witcher
from .notification import ShowPlayerStats
from . import BaseScene, Quit


class Menu(BaseScene):
	def exit(self, game):
		pass

	def execute(self, game):
		text = [	'Привет. Это моя игра в консоли.',
                    '1. Старт',
                    '2. Загрузка',
                    '2. Выход', ]
		valid_answers = {
                    1: ['1', 'start', 'new'],
                    2: ['2', 'load'],
                    3: ['3', 'exit', 'quit']
		}
		question = self.interface.create_readable_text(valid_answers)
		self.interface.print(text, delay=0.2)
		answer = self.interface.ask(question, valid_answers)
		if answer == 1:
			game.scene = PlayerClassChoice()

		elif answer == 2:
			game.load()

		elif answer == 3:
			game.scene = Quit()


class PlayerClassChoice(BaseScene):
	def execute(self, game):
		text = [
			'Выбор класса:',
			'1. Warrior',
			'2. Mage',
			'3. Assassin',
			'4. Cleric',
			'5. Archer',
			'6. Paladin',
			'7. Witcher',
		]
		self.interface.print(text, delay=0.2)
		valid_answers = {
                    1: ['1', 'warrior'],
                    2: ['2', 'mage', 'wizard'],
                    3: ['3', 'Assassin'],
                    4: ['4', 'Cleric'],
                    5: ['5', 'Archer'],
                    6: ['6', 'Paladin'],
                    7: ['7', 'Witcher'],
		}
		question = self.interface.create_readable_text(valid_answers)
		answer = self.interface.ask(question, valid_answers)
		if answer == 1:
			game.player = Player(Warrior())
		elif answer == 2:
			game.player = Player(Wizard())
		elif answer == 3:
			game.player = Player(Assassin())
		elif answer == 4:
			game.player = Player(Cleric())
		elif answer == 5:
			game.player = Player(Archer())
		elif answer == 6:
			game.player = Player(Paladin())
		elif answer == 7:
			game.player = Player(Witcher())
		game.scene = ShowPlayerStats()
