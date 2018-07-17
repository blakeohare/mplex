
# TODO: auto-generate this file from metadata

import mplex.native as _native

from .methods import *
#import mplex.native.drawing.methods as _methods

_commands = {
	'create-bitmap-file': create_bitmap_file,
	'create-bitmap-size': create_bitmap_size,
	'save-bitmap': save_bitmap,
}

_native.REGISTRY.register('Drawing', _native.NativeBridge(_commands))
