
#ifndef NATIVE_BRIDGE_H
#define NATIVE_BRIDGE_H

#include "../util/dictionary.h"

typedef struct BridgeArg {
	char type; // { I | S | B }
	union {
		int int_value;
		const char* string_value;
		int bool_value;
	};
} BridgeArg;

typedef struct BridgeArgs {
	int count;
	int allocated;
	BridgeArg* args;
} BridgeArgs;

typedef struct NativeBridge {
	int status_code;
	int next_obj_id;

	int integer_out_length;
	int* integer_out;

	Dictionary* native_objects_by_id;

	int (*send_impl)(void* bridge, const char* cmd, int argc, BridgeArg* args);
} NativeBridge;

void* get_native_object(NativeBridge* bridge, int obj_id);

int register_native_object(NativeBridge* bridge, void* obj);

void ensure_bridge_int_allocation(NativeBridge* bridge, int size);

NativeBridge* new_native_bridge();

int send(NativeBridge* bridge, const char* cmd);

BridgeArgs* get_bridge_args();
void set_bridge_args_length(int arg_count);
void set_bridge_arg_int(int argn, int value);
void set_bridge_arg_string(int argn, const char* value);
int get_bridge_int_arg(BridgeArg* args, int index);
const char* get_bridge_string_arg(BridgeArg* args, int index);

#endif // NATIVE_BRIDGE_H
