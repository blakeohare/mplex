import os
import json
from generators import *

ABSOLUTE_PATH = 1
RELATIVE_TO_ROOT = 2
FILES_ONLY = 3

def get_directories(path, type):
	output = []
	root = os.path.abspath('.')
	path = os.path.abspath(path.replace('/', os.sep))
	
	for file in os.listdir(path):
		fullpath = os.path.join(path, file)
		if os.path.isdir(fullpath):
			if type == ABSOLUTE_PATH:
				output.append(fullpath)
			elif type == FILES_ONLY:
				output.append(file)
			else:
				output.append(fullpath[len(root):])
	return output

def read_file_text(path):
	c = open(path, 'rt')
	text = c.read()
	c.close()
	return text

def parse_json(text):
	return json.loads(text)
	
def get_libraries():
	library_names = get_directories('libs', FILES_ONLY)
	output = []
	for name in library_names:
		manifest_file = os.path.join('libs', name, 'metadata.json')
		if os.path.exists(manifest_file):
			metadata = parse_json(read_file_text(manifest_file))
			metadata['path'] = os.path.join('libs', name)
			output.append(metadata)
	return output

def main():
	generators = [
		#CGenerator(),
		#CSharpGenerator(),
		#JavaGenerator(),
		#JavaScriptGenerator(),
		#PHPGenerator(),
		PythonGenerator(),
	]
	libraries = get_libraries()
	for library in libraries:
		for generator in generators:
			generator.generate_bridge_files(library, os.path.join('output', generator.get_lang_name(), library['name']))
	

main()
