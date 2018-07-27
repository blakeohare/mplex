from .pyNative import BRIDGE as _BRIDGE

def _throwErr(self):
	id = _BRIDGE.error_id
	msg = _BRIDGE.error_msg
	raise Exception(msg)

class Bitmap:

	def __init__(self, widthOrFilePath, height = None):
		self._nativeData = {}
		self._pixelSession = None
		if height == None and isinstance(widthOrFilePath, str):
			_BRIDGE.CreateBitmapFile(self._nativeData, widthOrFilePath)
		elif isinstance(widthOrFilePath, int) and isinstance(height, int):
			_BRIDGE.CreateBitmapSize(self._nativeData, widthOrFilePath, height)
		else:
			raise Exception("Invalid arguments")

		if _BRIDGE.has_error: _throwErr()
		
		self.width = self._nativeData['width']
		self.height = self._nativeData['height']
	
	def save(self, path):
		if not isinstance(path, str):
			raise Exception("Invalid arguments.")
		_BRIDGE.SaveBitmap(self._nativeData, path)
		
		if _BRIDGE.has_error: _throwErr()
		return self
		
	def edit(self):
		self._pixelSession = PixelSession(self)
		return self._pixelSession

class PixelSession:
	
	def __init__(self, bmp):
		self._bmp = bmp
		self._nativeData = {}
		self._is_valid = True
		
		_BRIDGE.GetBitmapEditSession(self._nativeData, bmp._nativeData)
		if _BRIDGE.has_error: _throwErr()
	
	def drawRectangle(self, x, y, width, height, r, g, b, a):
		if not self._is_valid: self._notValid()
		_BRIDGE.DrawRectangle(self._nativeData, x, y, width, height, r, g, b, a)
		if _BRIDGE.has_error: _throwErr()
		return self
	
	def drawBitmap(self, bmp, x, y):
		if not self._is_valid: self._notValid()
		_BRIDGE.BlitBitmap(self._nativeData, bmp._nativeData, bmp._pixelSession._nativeData, x, y)
		if _BRIDGE.has_error: _throwErr()
		return self
	
	def flush(self):
		if not self._is_valid: self._notValid()
		_BRIDGE.FlushBitmapEditSession(self._nativeData, self._bmp._nativeData)
		if _BRIDGE.has_error: _throwErr()
		self._is_valid = False
		return self

	def _notValid(self):
		raise Exception("This session has been closed and is no longer valid.")
	
	