#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

int dictionary_hash_string(const char* s)
{
	int output = 0;
	int index = 0;
	char c;
	while ((c = s[index++]) != '\0')
	{
		output = output * 31 + c;
	}
	return output;
}

Dictionary* new_dictionary_common(char type)
{
	Dictionary* d = (Dictionary*)malloc(sizeof(Dictionary));
	d->key_type = type;
	d->size = 0;
	d->bucket_count = 10;
	d->buckets = (DictionaryItem**)malloc(sizeof(DictionaryItem*) * d->bucket_count);
	for (int i = 0; i < d->bucket_count; ++i)
	{
		d->buckets[i] = NULL;
	}
	return d;
}

DictionaryItem* dictionary_get_bucket_int(Dictionary* d, int key)
{
	// TODO: assert key type
	DictionaryItem* bucket = d->buckets[key % d->bucket_count];
	while (bucket != NULL)
	{
		if (bucket->int_key == key)
		{
			return bucket;
		}
	}
	return NULL;
}

DictionaryItem* dictionary_get_bucket_string(Dictionary* d, const char* key)
{
	// TODO: assert key type
	int hash = dictionary_hash_string(key);
	DictionaryItem* bucket = d->buckets[hash % d->bucket_count];
	while (bucket != NULL)
	{
		if (bucket->hash == hash && 
			(key == bucket->string_key || strcmp(key, bucket->string_key) == 0))
		{
			return bucket;
		}
	}
	return NULL;
}

void dictionary_rehash(Dictionary* d)
{
	// TODO: re-hash
}

DictionaryItem* dictionary_create_bucket_common(Dictionary* d, DictionaryItem* item)
{
	int bucket_id = item->hash % d->bucket_count;
	item->next = d->buckets[bucket_id];
	d->buckets[bucket_id] = item;
	if (d->size++ * 2 > d->bucket_count * 3)
	{
		dictionary_rehash(d);
	}
	return item;
}

DictionaryItem* dictionary_create_bucket_int(Dictionary* d, int key)
{
	DictionaryItem* item = (DictionaryItem*)malloc(sizeof(DictionaryItem));
	item->hash = key;
	item->int_key = key;
	return dictionary_create_bucket_common(d, item);
}

DictionaryItem* dictionary_create_bucket_string(Dictionary* d, const char* key)
{
	DictionaryItem* item = (DictionaryItem*)malloc(sizeof(DictionaryItem));
	item->hash = dictionary_hash_string(key);
	item->string_key = key;
	return dictionary_create_bucket_common(d, item);

}

Dictionary* new_dictionary_int() { return new_dictionary_common('I'); }
Dictionary* new_dictionary_string() { return new_dictionary_common('S'); }

void clear_dictionary(Dictionary* d)
{
	for (int i = 0; i < d->bucket_count; ++i)
	{
		DictionaryItem* walker = d->buckets[i];
		while (walker != NULL)
		{
			DictionaryItem* next = walker->next;
			free(walker);
			walker = (DictionaryItem*) next;
		}
		d->buckets[i] = NULL;
	}
	d->size = 0;
}

void dictionary_set_impl_int_int(Dictionary* d, int key, int value, int allow_collision)
{
	DictionaryItem* item = dictionary_get_bucket_int(d, key);
	if (item == NULL) item = dictionary_create_bucket_int(d, key);
	else { /* TODO: assert allow_collision is true */ }

	item->value_type = 'I';
	item->int_value = value;
}

void dictionary_set_impl_string_int(Dictionary* d, const char* key, int value, int allow_collision)
{
	DictionaryItem* item = dictionary_get_bucket_string(d, key);
	if (item == NULL) item = dictionary_create_bucket_string(d, key);
	else { /* TODO: assert allow_collision is true */ }

	item->value_type = 'I';
	item->int_value = value;
}

void dictionary_set_impl_int_obj(Dictionary* d, int key, void* value, int allow_collision)
{
	DictionaryItem* item = dictionary_get_bucket_int(d, key);
	if (item == NULL) item = dictionary_create_bucket_int(d, key);
	else { /* TODO: assert allow_collision is true */ }

	item->value_type = 'O';
	item->obj_value = value;
}
void dictionary_set_impl_string_obj(Dictionary* d, const char* key, void* value, int allow_collision)
{
	DictionaryItem* item = dictionary_get_bucket_string(d, key);
	if (item == NULL) item = dictionary_create_bucket_string(d, key);
	else { /* TODO: assert allow_collision is true */ }

	item->value_type = 'O';
	item->obj_value = value;
}


void dictionary_set_int_int(Dictionary* d, int key, int value) { dictionary_set_impl_int_int(d, key, value, 1); }
void dictionary_add_int_int(Dictionary* d, int key, int value) { dictionary_set_impl_int_int(d, key, value, 0); }

void dictionary_set_string_int(Dictionary* d, const char* key, int value) { dictionary_set_impl_string_int(d, key, value, 1); }
void dictionary_add_string_int(Dictionary* d, const char* key, int value) { dictionary_set_impl_string_int(d, key, value, 0); }

void dictionary_set_int_obj(Dictionary* d, int key, void* value) { dictionary_set_impl_int_obj(d, key, value, 1); }
void dictionary_add_int_obj(Dictionary* d, int key, void* value) { dictionary_set_impl_int_obj(d, key, value, 0); }

void dictionary_set_string_obj(Dictionary* d, const char* key, void* value) { dictionary_set_impl_string_obj(d, key, value, 1); }
void dictionary_add_string_obj(Dictionary* d, const char* key, void* value) { dictionary_set_impl_string_obj(d, key, value, 0); }

int dictionary_get_int_int(Dictionary* d, int key, int default_value)
{
	DictionaryItem* existing = dictionary_get_bucket_int(d, key);
	if (existing == NULL) return default_value;
	// TODO: assert value is int
	return existing->int_value;
}

int dictionary_get_string_int(Dictionary* d, const char* key, int default_value)
{
	DictionaryItem* existing = dictionary_get_bucket_string(d, key);
	if (existing == NULL) return default_value;
	// TODO: assert value is int
	return existing->int_value;
}

void* dictionary_get_int_obj(Dictionary* d, int key)
{
	DictionaryItem* existing = dictionary_get_bucket_int(d, key);
	if (existing == NULL) return NULL;
	// TODO: assert value is obj
	return existing->obj_value;
}

void* dictionary_get_string_obj(Dictionary* d, const char* key)
{
	DictionaryItem* existing = dictionary_get_bucket_string(d, key);
	if (existing == NULL) return NULL;
	// TODO: assert value is obj
	return existing->obj_value;	
}
