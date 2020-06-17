from . import BaseScene


class ShowPlayerStats(BaseScene):
	def execute(self, game):
		text = [
			f"Info:\n{game.player.info}"
			f"Stats:\n{game.player.stats}",
		]
		self.interface.print(text)
		game.scene.blip(game)
