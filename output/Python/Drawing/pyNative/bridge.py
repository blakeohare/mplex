from PIL import Image
import os

from .genbridge import GeneratedBridge

class Bridge(GeneratedBridge):
	def CreateBitmapFile(self, nativeData, path):
		if not os.path.exists(path):
			return bridge.set_error(1, "File does not exist.")
		Image.open(path)
		try:
			img = Image.open(path)
		except:
			return bridge.set_error(1, "Invalid image file.")
		
		if img.mode != 'RGBA':
			img = img.convert('RGBA')
		
		nativeData['bmp'] = img
		nativeData['width'] = img.size[0]
		nativeData['height'] = img.size[1]
		nativeData['pixels'] = None
		
		return 0

	def CreateBitmapSize(self, nativeData, width, height):
		if width < 1 or width > 5000 or height < 1 or height > 5000:
			return bridge.set_error(1, "Image size is invalid.")
		try:
			img = Image.new('RGBA', (width, height))
		except:
			return bridge.set_error(1, "Could not create image.")
		
		nativeData['bmp'] = img
		nativeData['width'] = width
		nativeData['height'] = height
		nativeData['pixels'] = None
		
		return 0

	def SaveBitmap(self, nativeData, path):
		try:
			nativeData['bmp'].save(path)
		except:
			return bridge.set_error(1, "Could not write to file.")
		return 0

	def GetBitmapEditSession(self, nativeData, bmpNativeData):
		raise Exception("Not implemented.")

	def FlushBitmapEditSession(self, nativeData, bmpNativeData):
		raise Exception("Not implemented.")

	def DrawRectangle(self, nativeData, x, y, r, g, b, a):
		raise Exception("Not implemented.")

	def DrawBitmap(self, pixelNativeData, bmp2NativeData, pixel2NativeData, x, y):
		raise Exception("Not implemented.")

BRIDGE = Bridge()
