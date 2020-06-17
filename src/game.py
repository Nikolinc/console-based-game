from src.scene.ui import Menu
from src.scene import BaseScene
from src.util import check_isinstance
import pickle
import os


class Game:
	def __init__(self):
		self.PATH_TO_SAVES = os.path.join(os.path.dirname(__file__), '..', 'saves')
		os.makedirs(self.PATH_TO_SAVES, exist_ok=True)
		self.SAVE_FILE_NAME = 'save.pyc0d3'
		self.PATH_TO_SAVE_FILE = os.path.join(
			self.PATH_TO_SAVES, self.SAVE_FILE_NAME)

		self.is_running = True
		self._scene = Menu()
		self._prev_scene = Menu()

	def save(self):
		with open(self.PATH_TO_SAVE_FILE, 'wb') as file:
			pickle.dump(self.__dict__, file)

	def load(self):
		with open(self.PATH_TO_SAVE_FILE, 'rb') as file:
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
