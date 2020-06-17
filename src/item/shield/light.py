from . import BaseShield


class Cardboard(BaseShield):
	def __init__(self, owner):
		stats = self.Stats(owner, defence=2, block_chance=0.08)
		info = self.Info(owner, name='Cardboard')
		super().__init__(owner, stats, info)
