
#include "methods.h"
#include "structs.h"

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"


int native_drawing_create_bitmap_file(NativeBridge* bridge, const char* path)
{
	int width, height, bpp;
	unsigned char* rgb = stbi_load(path, &width, &height, &bpp, 3);

	Image* img = (Image*) malloc(sizeof(Image));
	int obj_id = register_native_object(bridge, img);
	img->object_id = obj_id;
	img->width = width;
	img->height = height;
	img->bpp = bpp;
	img->rgb = rgb;

	bridge->integer_out[0] = obj_id;
	bridge->integer_out[1] = width;
	bridge->integer_out[2] = height;

	return 0;
}

int native_drawing_create_bitmap_size(NativeBridge* bridge, int width, int height)
{
	Image* img = (Image*) malloc(sizeof(Image));
	int obj_id = register_native_object(bridge, img);
	img->object_id = obj_id;
	img->width = width;
	img->height = height;
	img->bpp = 32;
	img->rgb = malloc(sizeof(unsigned char) * width * height * 4);

	bridge->integer_out[0] = obj_id;
	bridge->integer_out[1] = width;
	bridge->integer_out[2] = height;

	return 0;
}

int native_drawing_save_bitmap(NativeBridge* bridge, int object_id, const char* path)
{
	Image* img = (Image*) get_native_object(bridge, object_id);
	stbi_write_png(path, img->width, img->height, 3, img->rgb, 0);
	return 0;
}
