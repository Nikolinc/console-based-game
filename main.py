from src import game
import os

if __name__ == '__main__':
	os.makedirs('saves', exist_ok=True)
	save_file_location = os.path.join(
		os.path.dirname(__file__), 'saves', 'save.pyc0d3')
	game.Game(save_file_location).run()
