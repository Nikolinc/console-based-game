from src.character import BaseCharacter
from src.item.shield import NoShield
from src.item.armor import NoArmor
from src.item.weapon import NoWeapon


class Player(BaseCharacter):
	def __init__(self, class_):
		stats = self.Stats(
			self,
			hp=100,
			mp=100,
			evasion=0.3,
			accuracy=1.0
		)
		info = self.Info(
			self,
			name='You',
			class_=class_
		)
		weapon = NoWeapon(self)
		armor = NoArmor(self)
		shield = NoShield(self)
		super().__init__(stats, info, weapon, armor, shield)
