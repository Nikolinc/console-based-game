from src.item.armor.light import Cloak, Robe, Jacket, Pallium
from src.item.armor.heavy import ChestPlate, Breastplate
from src.item.weapon.melee import Sword, Whinger,Hammer, Brand
from src.item.weapon.ranged import Staff, Pikestaff, Bow
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
		character.stats.max_hp = 50
		character.stats.max_mp = 10
		character.stats.accuracy = 1.2
		character.stats.evasion = 0.2
		character.armor = ChestPlate(character)
		character.weapon = Sword(character)
		character.reset()


class Assassin(BaseClass):
	def __init__(self):
		self.name = "Assassin"

	def activate(self, character):
		character.stats.max_hp = 30
		character.stats.max_mp = 50
		character.stats.accuracy = 0.7
		character.stats.evasion = 0.6
		character.armor = Robe(character)
		character.weapon = Whinger(character)
		character.reset()


class Cleric(BaseClass):
	def __init__(self):
		self.name = "Cleric"

	def activate(self, character):
		character.stats.max_hp = 30
		character.stats.max_mp = 50
		character.stats.accuracy = 0.8
		character.stats.evasion = 0.4
		character.armor = Pallium(character)
		character.weapon = Pikestaff(character)
		character.reset()


class Archer(BaseClass):
	def __init__(self):
		self.name = "Archer"

	def activate(self, character):
		character.stats.max_hp = 30
		character.stats.max_mp = 50
		character.stats.accuracy = 0.8
		character.stats.evasion = 0.4
		character.armor = Gambeson(character)
		character.weapon = Bow(character)
		character.reset()



class Paladin(BaseClass):
	def __init__(self):
		self.name = "Paladin"

	def activate(self, character):
		character.stats.max_hp = 60
		character.stats.max_mp = 50
		character.stats.accuracy = 0.8
		character.stats.evasion = 0.4
		character.armor = Breastplate(character)
		character.weapon = Hammer(character)
		character.reset()


class Witcher(BaseClass):
	def __init__(self):
		self.name = "Witcher"

	def activate(self, character):
		character.stats.max_hp = 40
		character.stats.max_mp = 50
		character.stats.accuracy = 0.8
		character.stats.evasion = 0.4
		character.armor = Jacket(character)
		character.weapon = Brand(character)
		character.reset()