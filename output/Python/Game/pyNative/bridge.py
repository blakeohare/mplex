import time as time
import os, sys

# As of PyGame 1.9.4, import pygame prints spurious output that cannot be disabled.
with open(os.devnull, 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    import pygame
    sys.stdout = oldstdout
	
class GameContainer:
	def __init__(self, gw, gh, pw, ph, title, fps):
		self.game_screen = None
		self.pixel_screen = None
		self.gsize = (gw, gh)
		self.psize = (pw, ph)
		self.scaled = gw != pw or gh != ph
		self.fps = fps
		self.title = title
		self.callback = None
		self.bgcolor = (0, 0, 0)
		
		self.render_queue = []
		self.render_size = 0
		self.render_capacity = 0
		self.event_count = 0
		self.int_events = []
		self.str_events = []
		
		self.destroyed = False

	def convertXY(self, xy):
		return (xy[0] * self.gsize[0] // self.psize[0], xy[1] * self.gsize[1] // self.psize[1])

	def run(self):
		
		pygame.init()
		self.pixel_screen = pygame.display.set_mode(self.psize)
		self.game_screen = self.pixel_screen
		if self.scaled:
			self.game_screen = pygame.Surface(self.gsize).convert()
		
		screen = self.game_screen
		
		while not self.destroyed:
			start_time = time.time()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.MOUSEMOTION:
					xy = self.convertXY(event.pos)
					self.int_events += [1, xy[0], xy[1], 0, 0, 0]
					self.event_count += 1
				elif event.type == pygame.MOUSEBUTTONDOWN:
					xy = self.convertXY(event.pos)
					self.int_events += [1, xy[0], xy[1], 1, 1, event.button == 0]
					self.event_count += 1
				elif event.type == pygame.MOUSEBUTTONUP:
					xy = self.convertXY(event.pos)
					self.int_events += [1, xy[0], xy[1], 1, 0, event.button == 0]
					self.event_count += 1
				elif event.type == pygame.KEYDOWN:
					self.int_events += [2, 1, event.key]
					self.event_count += 1
				elif event.type == pygame.KEYUP:
					self.int_events += [2, 0, event.key]
					self.event_count += 1
				
			if self.callback != None:
				self.callback()
			
			screen.fill(self.bgcolor)
			
			i = 0
			q = self.render_queue
			while i < self.render_size:
				cmd = q[i]
				if cmd == 1:
					alpha = q[i + 3]
					if alpha == 255:
						pygame.draw.rect(screen, q[i + 2], q[i + 1])
					else:
						raise Exception() #TODO: alpha rectangle
				else:
					raise Exception() #TODO: others
				i += 16
			self.render_size = 0
			
			if self.scaled:
				pygame.transform.scale(self.game_screen, self.pixel_screen.get_size(), self.pixel_screen)

			pygame.display.flip()
			
			now = time.time()
			diff = now - start_time
			delay = 1.0 / self.fps - diff
			if delay > 0:
				time.sleep(delay)
			
	def increase_render_capacity(self):
		for i in range(16):
			self.render_queue.append(0)
			self.render_capacity += 1

	def popEvents(self, intOut, strOut):
		for t in self.int_events:
			intOut.append(t)
		for t in self.str_events:
			strOut.append(t)
		cnt = self.event_count
		self.event_count = 0
		self.int_events = []
		self.str_events = []
		return cnt

class Bridge(GeneratedBridge):
	def __init__(self):
		self.containers = {}
		self.next_id = 1
	
	def CreateWindow(self, gameWidth, gameHeight, pixelWidth, pixelHeight, title, fps):
		id = self.next_id
		self.containers[id] = GameContainer(gameWidth, gameHeight, pixelWidth, pixelHeight, title, fps)
		self.next_id += 1
		
		return id
		
	def ShowWindow(self, winId):
		self.containers[winId].run()
		
	def IsWindowCreationBlocking(self):
		return True
	
	def SetGameLoopCallback(self, winId, callback):
		self.containers[winId].callback = callback
	
	def DestroyWindow(self, winId):
		self.containers[winId].destroy = True
	
	def SetClearColor(self, winId, r, g, b):
		self.containers[winId].bgcolor = (r, g, b)
	
	def DrawRectangle(self, winId, x, y, width, height, r, g, b, a):
		# TODO: if this is all integers, use Pastel code, maybe?
		c = self.containers[winId]
		if a == 0: return
		q = c.render_queue
		size = c.render_size
		capacity = c.render_capacity
		if size == capacity:
			c.increase_render_capacity()
		q[size] = 1
		q[size + 1] = pygame.Rect(x, y, width, height)
		q[size + 2] = (r, g, b)
		q[size + 3] = a
		c.render_size += 16
	
	def DrawEllipse(self, winId, x, y, width, height, r, g, b, a):
		raise Exception()
	
	def DrawTriangle(self, winId, x1, y1, x2, y2, x3, y3, r, g, b, a):
		raise Exception()
	
	def PopEvents(self, winId, intOut, strOut):
		c = self.containers[winId]
		return c.popEvents(intOut, strOut)

BRIDGE = Bridge()
