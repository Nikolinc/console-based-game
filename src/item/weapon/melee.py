from . import BaseWeapon


class Sword(BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=5)
		info = self.Info(owner, name='Sword')
		super().__init__(owner, stats, info)
