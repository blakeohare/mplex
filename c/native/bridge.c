#include <stdlib.h>

#include "bridge.h"
#include "../util/dictionary.h"

NativeBridge* new_native_bridge(const char* name)
{
	NativeBridge* bridge = (NativeBridge*) malloc(sizeof(NativeBridge));
	bridge->status_code = 0;
	bridge->next_obj_id = 1;
	bridge->integer_out_length = 256;
	bridge->integer_out = malloc(sizeof(int) * bridge->integer_out_length);
	bridge->native_objects_by_id = new_dictionary_int();

	return bridge;
}

void* get_native_object(NativeBridge* bridge, int obj_id)
{
	return dictionary_get_int_obj(bridge->native_objects_by_id, obj_id);
}

int register_native_object(NativeBridge* bridge, void* obj)
{
	int obj_id = bridge->next_obj_id++;
	dictionary_add_int_obj(bridge->native_objects_by_id, obj_id, obj);
	return obj_id;
}

void ensure_bridge_int_allocation(NativeBridge* bridge, int size)
{
	if (bridge->integer_out_length < size)
	{
		free(bridge->integer_out);
		bridge->integer_out = malloc(sizeof(int) * size);
		bridge->integer_out_length = size;
	}
}

int send(NativeBridge* bridge, const char* cmd)
{
	BridgeArgs* args = get_bridge_args();
	return bridge->send_impl(bridge, cmd, args->count, args->args);
}

BridgeArgs* get_bridge_args()
{
	static BridgeArgs* args = NULL;
	if (args == NULL)
	{
		args = (BridgeArgs*) malloc(sizeof(BridgeArgs));
		args->count = 0;
		args->allocated = 10;
		args->args = (BridgeArg*) malloc(sizeof(BridgeArg) * args->allocated);
	}
	return args;	
}

void set_bridge_args_length(int arg_count)
{
	BridgeArgs* args = get_bridge_args();
	if (args->allocated < arg_count)
	{
		args->allocated = arg_count;
		free(args->args);
		args->args = (BridgeArg*) malloc(sizeof(BridgeArg) * args->allocated);
	}
	args->count = arg_count;
}

void set_bridge_arg_int(int argn, int value)
{
	BridgeArg* args = get_bridge_args()->args;
	args[argn].type = 'I';
	args[argn].int_value = value;
}

void set_bridge_arg_string(int argn, const char* value)
{
	BridgeArg* args = get_bridge_args()->args;
	args[argn].type = 'S';
	args[argn].string_value = value;
}

int get_bridge_int_arg(BridgeArg* args, int index)
{
	if (args[index].type != 'I')
	{
		// TODO: assert
	}
	return args[index].int_value;
}

const char* get_bridge_string_arg(BridgeArg* args, int index)
{
	if (args[index].type != 'S')
	{
		// TODO: assert
	}
	return args[index].string_value;	
}
