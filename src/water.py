
class Water:
	
	def __init__(self, x, y, images):
		self.x = x
		self.y = y
		self.img = images.sprite_water
	
		self.animationframe = 1
		self.imgs_win = [images.sprite_water_win1, images.sprite_water_win2]
	
	def draw(self, win=False):
		if win:
			img = self.imgs_win[int(self.animationframe)]
			self.animationframe = (self.animationframe + 0.1) % len(self.imgs_win)
		else:
			img = self.img
		return img