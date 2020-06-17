from abc import ABC, abstractmethod
from src.interface import Interface


class BaseScene(ABC):
	def __init__(self):
		self.interface = Interface()

	def blip(self, game):
		game.scene = game._prev_scene

	@abstractmethod
	def execute(self, game): pass

	def exit(self, game):
		game.save()

	def enter(self, game): pass


class GameOver(BaseScene):
	def exit(self, game):
		pass

	def execute(self, game):
		self.interface.print("Game over")
		game.scene = Quit()


class Quit(BaseScene):
	def exit(self, game):
		pass

	def execute(self, game):
		self.interface.print("Quit")
		game.is_running = False
