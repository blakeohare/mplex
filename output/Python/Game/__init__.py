from .pyNative import BRIDGE as _BRIDGE

class BaseGame:
	def __init__(self): pass
	def on_mouse_move(self, pos): pass
	def on_mouse_move(self, pos): pass
	def on_mouse_left_down(self, pos): pass
	def on_mouse_left_up(self, pos): pass
	def on_mouse_right_down(self, pos): pass
	def on_mouse_right_up(self, pos): pass
	def on_key_up(self, key): pass
	def on_key_down(self, key): pass
	def update(self): pass
	def render(self, renderer): pass
		
class GameWindow:
	def __init__(self, title, fps, game, game_size, screen_size = None):
		if screen_size == None:
			screen_size = game_size
		self._id = _BRIDGE.CreateWindow(game_size[0], game_size[1], screen_size[0], screen_size[1], title, fps)
		_BRIDGE.SetGameLoopCallback(self._id, self._gameLoop)
		self._renderer = Renderer2D(self)
		self._game = game
	
	def show(self):
		_BRIDGE.ShowWindow(self._id)
	
	def close(self):
		_BRIDGE.DestroyWindow(self._id)
	
	def setClearColor(self, color):
		_BRIDGE.SetClearColor(self._id, color[0], color[1], color[2])
	
	def _gameLoop(self):
		intOut = []
		strOut = []
		count = _BRIDGE.PopEvents(self._id, intOut, strOut)
		iIndex = 0
		sIndex = 0
		for i in range(count):
			e = intOut[iIndex]
			if e == 1:
				xy = (intOut[iIndex + 1], intOut[iIndex + 2])
				is_click = intOut[iIndex + 3] == 1
				is_down = intOut[iIndex + 4] == 1
				is_left = intOut[iIndex + 5] == 1
				if is_click:
					if is_down:
						if is_left:
							self._game.on_mouse_left_down(xy)
						else:
							self._game.on_mouse_right_down(xy)
					else:
						if is_left:
							self._game.on_mouse_left_up(xy)
						else:
							self._game.on_mouse_right_up(xy)
				else:
					self._game.on_mouse_move(xy)
				iIndex += 6
			elif e == 2:
				is_down = intOut[index + 1]
				kc = intOut[iIndex + 2]
				if is_down:
					self._game.on_key_down(kc)
				else:
					self._game.on_key_up(kc)
				iIndex += 2
		
		self._game.update()
		self._game.render(self._renderer)

class Renderer2D:
	def __init__(self, window):
		self._window = window
		self._id = window._id
	
	def drawRectangle(self, bounds, rgba):
		a = 255 if len(rgba) == 3 else rgba[3]
		return _BRIDGE.DrawRectangle(self._id, bounds[0], bounds[1], bounds[2], bounds[3], rgba[0], rgba[1], rgba[2], a)
