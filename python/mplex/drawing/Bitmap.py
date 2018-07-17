from mplex.native import REGISTRY as _reg

_BRIDGE = _reg.get('Drawing')

class Bitmap:

	def __init__(self, widthOrFilePath, height = None):
		self.nativeData = {}
		if height == None and isinstance(widthOrFilePath, str):
			_BRIDGE.sendOrThrow('create-bitmap-file', (self.nativeData, widthOrFilePath))
		elif isinstance(widthOrFilePath, int) and isinstance(height, int):
			_BRIDGE.sendOrThrow('create-bitmap-size', (self.nativeData, widthOrFilePath, height))
		else:
			raise Exception("Invalid arguments")
		self.width = self.nativeData['width']
		self.height = self.nativeData['height']
	
	def save(self, path):
		if not isinstance(path, str):
			raise Exception("Invalid arguments.")
		_BRIDGE.sendOrThrow('save-bitmap', (self.nativeData, path))
