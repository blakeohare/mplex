import json
import os

def read_file_text(path):
	c = open(path, 'rt')
	text = c.read()
	c.close()
	return text
	
def write_file_text(path, content):
	c = open(path, 'wt')
	c.write(content)
	c.close()

def get_library_manifests():
	libs_directory = os.path.join('..', 'libs')
	output = []
	
	for file in os.listdir(libs_directory):
		file_path = os.path.join(libs_directory, file, 'metadata.json')
		if os.path.exists(file_path):
			contents = read_file_text(file_path)
			error = None
			try:
				json_data = json.loads(contents)
			except:
				error = "@@@@@ " + file_path + " seems to contain a syntax error @@@@@@"
			
			if error != None:
				print(error)
				json.loads(contents)
			
			output.append(json_data)
	return output

def get_python_bridge_header(lib_name):
	return ("""
# DO NOT MODIFY THIS FILE DIRECTLY!
#
# It is autogenerated from libs/""" + lib_name + """/metadata.json.
# Update that file and then run scripts/generate_stubs.py to re-generate
# this file.

import mplex.native as _native

from .methods import *

_commands = {""").strip()

def get_python_bridge_footer():
	return """}

_native.REGISTRY.register('Drawing', _native.NativeBridge(_commands))
""".strip()

def generate_python_templates(library):
	bridge_code = [get_python_bridge_header(library['name'])]
	
	library_native_dir = os.path.join('..', 'python', 'mplex', 'native', library['name'].lower())
	methods_path = os.path.join(library_native_dir, 'methods.py')
	bridge_path = os.path.join(library_native_dir, '__init__.py')
	has_methods_file = os.path.exists(methods_path)
	if has_methods_file:
		method_file_content = read_file_text(methods_path)
	else:
		method_file_content = ''
	method_file_new_content = [method_file_content.rstrip()]
	
	method_names = []
	for method in library['methods']:
		name = method['name']
		py_name = name.replace('-', '_')
		bridge_code.append('\n')
		bridge_code.append('\t"')
		bridge_code.append(name)
		bridge_code.append('": ')
		bridge_code.append(py_name)
		bridge_code.append(',')
		
		if py_name not in method_file_content:
			method_file_new_content.append("\ndef ")
			method_file_new_content.append(py_name)
			method_file_new_content.append("(bridge, args):\n")
			if len(method['args']) > 0:
				method_file_new_content.append('  ')
				first = True
				for arg in method['args']:
					if first: first = False
					else: method_file_new_content.append(', ')
					method_file_new_content.append(arg['name']) # TODO: convert from camelCase to snake_case
				method_file_new_content.append(' = args\n  return -1\n')
	
	bridge_code.append('\n')
	bridge_code.append(get_python_bridge_footer())
	bridge_code.append('\n')
	
	write_file_text(bridge_path, ''.join(bridge_code))
	write_file_text(methods_path, ''.join(method_file_new_content).strip() + "\n")

def main():
	for library in get_library_manifests():
		generate_python_templates(library)
		#generate_csharp_templaets(library)
		
	
main()
