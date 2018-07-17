
#ifndef UTIL_DICTIONARY_H
#define UTIL_DICTIONARY_H

typedef struct DictionaryItem {
	int hash;
	union {
		int int_key;
		const char* string_key;
	};
	char value_type; // { I | S | O }
	union {
		int int_value;
		const char* string_value;
		void* obj_value;
	};
	void* next;
} DictionaryItem;


typedef struct Dictionary {
	char key_type; // { I | S }

	int size;
	int bucket_count;
	DictionaryItem** buckets;
} Dictionary;

Dictionary* new_dictionary_int();
Dictionary* new_dictionary_string();

void clear_dictionary(Dictionary* d);

void dictionary_add_int_int(Dictionary* d, int key, int value);
void dictionary_set_int_int(Dictionary* d, int key, int value);
void dictionary_add_string_int(Dictionary* d, const char* key, int value);
void dictionary_set_string_int(Dictionary* d, const char* key, int value);
void dictionary_add_int_obj(Dictionary* d, int key, void* value);
void dictionary_set_int_obj(Dictionary* d, int key, void* value);
void dictionary_add_string_obj(Dictionary* d, const char* key, void* value);
void dictionary_set_string_obj(Dictionary* d, const char* key, void* value);

int dictionary_get_int_int(Dictionary* d, int key, int default_value);
int dictionary_get_string_int(Dictionary* d, const char* key, int default_value);
void* dictionary_get_int_obj(Dictionary* d, int key);
void* dictionary_get_string_obj(Dictionary* d, const char* key);

#endif // UTIL_DICTIONARY_H
