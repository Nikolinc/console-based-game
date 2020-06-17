from . import BaseWeapon


class Staff(BaseWeapon):
	def __init__(self, owner):
		stats = self.Stats(owner, damage=7)
		info = self.Info(owner, name='Staff')
		super().__init__(owner, stats, info)
