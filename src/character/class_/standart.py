from src.item.armor.light import Cloak
from src.item.armor.heavy import ChestPlate
from src.item.weapon.melee import Sword
from src.item.weapon.ranged import Staff
from . import BaseClass


class Wizard(BaseClass):
	def __init__(self):
		self.name = "Wizard"

	def activate(self, character):
		character.stats.max_hp = 20
		character.stats.max_mp = 50
		character.stats.accuracy = 0.8
		character.stats.evasion = 0.4
		character.armor = Cloak(character)
		character.weapon = Staff(character)
		character.reset()


class Warrior(BaseClass):
	def __init__(self):
		self.name = "Warrior"

	def activate(self, character):
		character.stats.max_hp = 40
		character.stats.max_mp = 10
		character.stats.accuracy = 1.2
		character.stats.evasion = 0.2
		character.armor = ChestPlate(character)
		character.weapon = Sword(character)
		character.reset()
