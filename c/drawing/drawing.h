
#ifndef DRAWING_DRAWING_H
#define DRAWING_DRAWING_H

typedef struct Bitmap {
	int width;
	int height;
	int native_object_id;
} Bitmap;

Bitmap* new_bitmap_from_file(const char* path);
Bitmap* new_bitmap_from_size(int width, int height);
void bitmap_save(Bitmap* bmp, const char* path);

#endif // DRAWING_DRAWING_H
