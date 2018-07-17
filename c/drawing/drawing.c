#include <stdlib.h>

#include "drawing.h"
#include "../native/drawing/drawing.h"
#include "../native/bridge.h"

NativeBridge* get_bridge()
{
	static NativeBridge* bridge = NULL;
	if (bridge == NULL) bridge = Drawing_get_bridge();
	return bridge;
}

Bitmap* new_bitmap_from_file(const char* path)
{
	// TODO: verify file exists
	set_bridge_args_length(1);
	set_bridge_arg_string(0, path);

	int sc = send(get_bridge(), "create-bitmap-file");
	int* int_out = get_bridge()->integer_out;
	
	Bitmap* bmp = (Bitmap*) malloc(sizeof(Bitmap));
	bmp->native_object_id = int_out[0];
	bmp->width = int_out[1];
	bmp->height = int_out[2];
	
	return bmp;
}

Bitmap* new_bitmap_from_size(int width, int height)
{
	set_bridge_args_length(2);
	set_bridge_arg_int(0, width);
	set_bridge_arg_int(1, height);

	int sc = send(get_bridge(), "create-bitmap-size");
	int* int_out = get_bridge()->integer_out;
	
	Bitmap* bmp = (Bitmap*) malloc(sizeof(Bitmap));
	bmp->native_object_id = int_out[0];
	bmp->width = int_out[1];
	bmp->height = int_out[2];

	return bmp;
}

void bitmap_save(Bitmap* bmp, const char* path)
{
	set_bridge_args_length(2);
	set_bridge_arg_int(0, bmp->native_object_id);
	set_bridge_arg_string(1, path);

	send(get_bridge(), "save-bitmap");
}
