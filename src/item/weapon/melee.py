from . import BaseWeapon


class Sword(BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=5)
		info = self.Info(owner, name='Sword')
		super().__init__(owner, stats, info)


class Whinger(BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=3)
		info = self.Info(owner, name='Whinger')
		super().__init__(owner, stats, info)

class Hammer(BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=7)
		info = self.Info(owner, name='Whinger')
		super().__init__(owner, stats, info)

class Brand (BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=4)
		info = self.Info(owner, name='Whinger')
		super().__init__(owner, stats, info)