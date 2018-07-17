
#ifndef NATIVE_DRAWING_STRUCTS_H
#define NATIVE_DRAWING_STRUCTS_H

typedef struct Image {
	int object_id;
	int width;
	int height;
	int bpp;
	unsigned char* rgb;
} Image;

#endif // NATIVE_DRAWING_STRUCTS_H
