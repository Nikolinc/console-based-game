from src.scene.ui import Menu
from src.scene import BaseScene
from src.util import check_isinstance
import pickle


class Game:
	def __init__(self, save_file_location):
		self.is_running = True
		self.save_file_location = save_file_location
		self._scene = Menu()
		self._prev_scene = Menu()

	def save(self):
		with open(self.save_file_location, 'wb') as file:
			pickle.dump(self.__dict__, file)

	def load(self):
		with open(self.save_file_location, 'rb') as file:
			self.__dict__.update(pickle.load(file))

	def run(self):
		while self.is_running:
			self.scene.execute(self)

	@property
	def scene(self):
		return self._scene

	@scene.setter
	def scene(self, value: BaseScene):
		check_isinstance(value, BaseScene)
		self.scene.exit(self)
		self._prev_scene = self.scene
		self._scene = value
		self.scene.enter(self)
