
class Pingu:
	
	def __init__(self, x, y, images):
		self.x = x
		self.y = y
		self.animationframe = 1
		self.imgs = [images.sprite_pingu1, images.sprite_pingu2]
	
	def draw(self):
		img = self.imgs[self.animationframe]
		self.animationframe = (self.animationframe + 1) % len(self.imgs)
		return img