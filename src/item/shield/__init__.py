from src.util import check_isinstance


class BaseShield:
	class Stats:
		def __init__(self, owner, defence, block_chance):
			self.owner = owner
			self.defence = defence
			self.block_chance = block_chance

	class Info:
		def __init__(self, owner, name):
			self.owner = owner
			self.name = name

	def __init__(self, owner, stats, info):
		self.owner = owner
		self.stats = stats
		self.info = info

	@property
	def stats(self):
		return self._stats

	@stats.setter
	def stats(self, value):
		check_isinstance(value, self.Stats)
		self._stats = value

	@property
	def info(self):
		return self._info

	@info.setter
	def info(self, value):
		check_isinstance(value, self.Info)
		self._info = value


class NoShield(BaseShield):
	def __init__(self, owner):
		stats = self.Stats(owner, defence=0, block_chance=0)
		info = self.Info(owner, name='No shield')
		super().__init__(owner, stats, info)
