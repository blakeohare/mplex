from PIL import Image
import os

def create_bitmap_file(bridge, args):
	nativeData, path = args
	global error_msg
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

def create_bitmap_size(bridge, args):
	nativeData, width, height = args
	global error_msg
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

def save_bitmap(bridge, args):
	nativeData, path = args
	global error_msg
	try:
		nativeData['bmp'].save(path)
	except:
		return bridge.set_error(1, "Could not write to file.")
	return 0
	
