// TODO: auto-generate this file
#include "drawing.h"

#include <stdlib.h>

#include "../bridge.h"
#include "../../util/dictionary.h"
#include "methods.h"

Dictionary* Drawing_get_cmd_lookup()
{
	static Dictionary* lookup = NULL;
	if (lookup == NULL)
	{
		lookup = new_dictionary_string();
		dictionary_add_string_int(lookup, "create-bitmap-file", 1);
		dictionary_add_string_int(lookup, "create-bitmap-size", 2);
		dictionary_add_string_int(lookup, "save-bitmap", 3);
	}
	return lookup;
}

int Drawing_send_impl(void* bridge, const char* cmd, int argc, BridgeArg* args)
{
	switch (dictionary_get_string_int(Drawing_get_cmd_lookup(), cmd, -1))
	{
		case 1: // create-bitmap-file
			if (argc != 1) { } // TODO: assert
			return native_drawing_create_bitmap_file((NativeBridge*)bridge, get_bridge_string_arg(args, 0));
		case 2: // create-bitmap-size
			if (argc != 2) { } // TODO: assert
			return native_drawing_create_bitmap_size((NativeBridge*)bridge, get_bridge_int_arg(args, 0), get_bridge_int_arg(args, 1));
		case 3: // save-bitmap
			if (argc != 2) { } // TODO: assert
			return native_drawing_save_bitmap((NativeBridge*)bridge, get_bridge_int_arg(args, 0), get_bridge_string_arg(args, 1));
		default:
			return -1;
	}
}

NativeBridge* Drawing_get_bridge()
{
	static NativeBridge* bridge = NULL;
	if (bridge == NULL)
	{
		bridge = new_native_bridge();
		bridge->send_impl = &Drawing_send_impl;
	}
	return bridge;
}
