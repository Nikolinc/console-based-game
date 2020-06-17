from src.item.armor import BaseArmor
from src.item.weapon import BaseWeapon
from src.item.shield import BaseShield
from src.util import check_isinstance
from src.flag.battle import *
from .class_ import BaseClass

import random


class BaseCharacter:
	class Stats:
		def __init__(self, owner, hp=0, mp=0, accuracy=1.0, evasion=0):
			self.owner = owner
			self._max_hp = hp
			self._hp = hp
			self._max_mp = mp
			self._mp = mp
			self.accuracy = accuracy
			self.evasion = evasion

		def __str__(self):
			hp = f'''HP: {self.hp}/{self.max_hp}\n'''
			mp = f'''MP: {self.mp}/{self.max_mp}\n'''
			acc = f'''ACC: {self.accuracy * 100}%\n'''
			eva = f'''EVA: {self.evasion * 100}%\n'''
			discription = hp + mp + acc + eva
			return discription

		def __repr__(self):
			return self.__str__()

		@property
		def block_chance(self):
			return self.owner.shield.stats.block_chance

		@property
		def damage(self):
			return self.owner.weapon.stats.damage

		@property
		def defence(self):
			return (self.owner.armor.stats.defence + self.owner.shield.stats.defence)

		@property
		def max_hp(self):
			return self._max_hp

		@max_hp.setter
		def max_hp(self, value):
			self._max_hp = value

		@property
		def max_mp(self):
			return self._max_mp

		@max_mp.setter
		def max_mp(self, value):
			self._max_mp = value

		@property
		def hp(self):
			return self._hp

		@hp.setter
		def hp(self, value):
			self._hp = value if value <= self.max_hp else self.max_hp

		@property
		def mp(self):
			return self._mp

		@mp.setter
		def mp(self, value):
			self._mp = value if value <= self.max_mp else self.max_mp

	class Info:
		def __init__(self, owner, name, class_):
			self.owner = owner
			self._name = name
			self._class = class_

		def __str__(self):
			class_name = f'CLASS NAME: {self.class_.name}\n'
			name = f'NAME: {self.name}\n'
			return name + class_name

		def __repr__(self):
			return self.__str__()

		@property
		def name(self):
			return self._name

		@property
		def class_(self):
			return self._class

		@class_.setter
		def class_(self, value: BaseClass):
			check_isinstance(value, BaseClass)
			self._class = value

	def __init__(self, stats, info, weapon, armor, shield):
		self.stats = stats
		self.info = info
		self.weapon = weapon
		self.armor = armor
		self.shield = shield
		self.info.class_.activate(self)

	def is_dodged(self, accuracy: float, enemy_evasion: float) -> bool:
		return random.choices(
			[True, False], [accuracy - enemy_evasion, 1 - accuracy - enemy_evasion])[0]

	def is_blocked(self, block_chance: float) -> bool:
		return random.choices(
			[True, False], [block_chance, 1 - block_chance])[0]

	def is_critical_hit(self, critical_hit_chance: float) -> bool:
		return random.choices(
			[True, False], [critical_hit_chance, 1 - critical_hit_chance])[0]

	def reset(self):
		self.stats.hp = self.stats.max_hp
		self.stats.mp = self.stats.max_mp

	def attack(self, enemy):
		if self.is_dodged(self.stats.accuracy, enemy.stats.evasion):
			return DODGED
		if self.is_blocked(self.stats.block_chance):
			return BLOCKED
		if self.is_critical_hit(self.stats.critical_hit_chance):
			multiplicator = self.stats.critical_hit_multiplicator
		else:
			multiplicator = 1

		damage = (self.stats.damage - enemy.stats.defence) * multiplicator
		damage = damage if damage >= 0 else 0
		enemy.stats.hp -= damage
		return CRIT(damage) if multiplicator != 1 else ATTACKED(damage)

	@property
	def info(self):
		return self._info

	@info.setter
	def info(self, value):
		check_isinstance(value, self.Info)
		self._info = value

	@property
	def stats(self):
		return self._stats

	@stats.setter
	def stats(self, value):
		check_isinstance(value, self.Stats)
		self._stats = value

	@property
	def weapon(self):
		return self._weapon

	@weapon.setter
	def weapon(self, value):
		check_isinstance(value, BaseWeapon)
		self._weapon = value

	@property
	def armor(self):
		return self._armor

	@armor.setter
	def armor(self, value):
		check_isinstance(value, BaseArmor)
		self._armor = value

	@property
	def shield(self):
		return self._shield

	@shield.setter
	def shield(self, value):
		check_isinstance(value, BaseShield)
		self._shield = value
