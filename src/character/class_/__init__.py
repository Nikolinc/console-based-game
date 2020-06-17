from src.util import check_isinstance


class BaseClass:
	class Info:
		def __init__(self, name):
			self.name = name

	def __init__(self, info):
		self.info = info

	@property
	def info(self):
		return self._info

	@info.setter
	def info(self, value):
		check_isinstance(value, self.Info)
		self._info = value
