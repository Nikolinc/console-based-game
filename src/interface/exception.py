class InvalidFormatForDict(Exception):
	def __init__(self, *args, **kwargs):
		super().__init__(
			"Try to reformat your dict to {'true':list(), 'false':list()}", *args, **kwargs)
