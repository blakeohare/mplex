import Image
import os

int256 = [0] * 256
error_msg = None

def _error(id, msg):
	global error_msg
	error_msg = msg
	return id

def _create_bitmap_file(args):
	ubmp, path = args
	global error_msg
	if not os.path.exists(path):
		return _error(1, "File does not exist.")
	try:
		img = Image.open(filepath)
	except:
		return _error(1, "Invalid image file.")
	if img.mode != 'RGBA':
		img = img.convert('RGBA')
	width, height = img.size[0], img.size[1]
	ubmp._nativeData = {
		'bmp': img,
		'width': width,
		'height': height,
		'pixels': None
	}
	int256[0], int256[1] = width, height
	
	return 0
	
	
def _create_bitmap_size(args):
	ubmp, width, height = args
	global error_msg
	if width < 1 or width > 5000 or height < 1 or height > 5000:
		return _error(1, "Image size is invalid.")
	try:
		img = Image.new('RGBA', (width, height))
	except:
		return _error(1, "Could not create image.")
	ubmp._nativeData = {
		'bmp': img,
		'width': width,
		'height': height,
		'pixels': None
	}
	int256[0], int256[1] = width, height
	return 0
	
	
def _save_bitmap(args):
	ubmp, path = args
	global error_msg
	try:
		ubmp._nativeData['bmp'].save(path)
	except:
		return _error(1, "Could not write to file.")
	return 0
	

_NATIVE_COMMANDS = {
	'create-bitmap-file': _create_bitmap_file,
	'create-bitmap-size': _create_bitmap_size,
	'save-bitmap': _save_bitmap,
}

def send(cmd, args):
	return _NATIVE_COMMANDS[cmd](args)
	