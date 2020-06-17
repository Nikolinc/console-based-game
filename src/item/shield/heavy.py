from . import BaseShield


class Stool(BaseShield):
	def __init__(self, owner):
		stats = self.Stats(owner, defence=3, block_chance=0.04)
		info = self.Info(owner, name='Stool')
		super().__init__(owner, stats, info)
