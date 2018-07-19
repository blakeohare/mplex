#include <stdio.h>

#include "util/dictionary.h"
#include "drawing/drawing.h"

int main()
{
	printf("Hello, World!\n");

	Dictionary* d = new_dictionary_int();
	dictionary_set_int_int(d, 1, 10);
	dictionary_set_int_int(d, 2, 20);
	printf("Dictionary size: %d\n", d->size);
	printf("Dictionary at 2: %d\n", dictionary_get_int_int(d, 2, -1));

	Bitmap* bmp = new_bitmap_from_file("sample_image.png");
	printf("Image is %d by %d pixels.\n", bmp->width, bmp->height);
	bitmap_save(bmp, "totoro3.png");
}
