import native

class Bitmap:

	def __init__(self, widthOrFilePath, height = None):
		if height == None and type(widthOrFilePath) == type(''):
			sc = native.send('create-bitmap-file', (self, widthOrFilePath))
			if sc == 0:
				self.width = native.int256[0]
				self.height = native.int256[1]
			else:
				raise Exception(native.error_msg)
		elif type(widthOrFilePath) == type(1) and type(height) == type(1):
			sc = native.send('create-bitmap-size', (self, widthOrFilePath, height))
			if sc == 0:
				self.width = native.int256[0]
				self.height = native.int256[1]
			else:
				raise Exception(native.error_msg)
		else:
			raise Exception("Invalid arguments")
	
	def save(self, path):
		sc = native.send('save-bitmap', (self, path))
		if sc != 0:
			raise Exception(native.error_msg)
	
	