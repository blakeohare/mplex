
#ifndef NATIVE_DRAWING_METHODS_H
#define NATIVE_DRAWING_METHODS_H

#include "../bridge.h"

int native_drawing_create_bitmap_file(NativeBridge* bridge, const char* path);

int native_drawing_create_bitmap_size(NativeBridge* bridge, int width, int height);

int native_drawing_save_bitmap(NativeBridge* bridge, int object_id, const char* path);

#endif // NATIVE_DRAWING_METHODS_H
