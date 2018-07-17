from mplex.native import REGISTRY as _reg

_BRIDGE = _reg.get('Drawing')

class Bitmap:

	def __init__(self, widthOrFilePath, height = None):
		self.nativeData = {}
		if height == None and isinstance(widthOrFilePath, str):
			sc = _BRIDGE.send('create-bitmap-file', (self.nativeData, widthOrFilePath))
			if sc != 0:
				raise Exception(_BRIDGE.error_msg)
		elif isinstance(widthOrFilePath, int) and isinstance(height, int):
			sc = _BRIDGE.send('create-bitmap-size', (self.nativeData, widthOrFilePath, height))
			if sc != 0:
				raise Exception(_BRIDGE.error_msg)
		else:
			raise Exception("Invalid arguments")
		self.width = self.nativeData['width']
		self.height = self.nativeData['height']
	
	def save(self, path):
		if not isinstance(path, str):
			raise Exception("Invalid arguments.")
		sc = _BRIDGE.send('save-bitmap', (self.nativeData, path))
		if sc != 0:
			raise Exception(_BRIDGE.error_msg)
