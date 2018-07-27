import os

def fix_path(path):
	return os.path.abspath(path.replace('/', os.sep))

def write_file_and_create_dir(path, content):
	path = fix_path(path)
	dir = os.path.dirname(path)
	if not os.path.isdir(dir):
		os.makedirs(dir)
	c = open(path, 'wt')
	c.write(content)
	c.close()

def hyphens_to_snake(s):
	return s.replace('-', '_')

def hyphens_to_pascal(s):
	parts = s.split('-')
	output = []
	for part in parts:
		output.append(part[0].upper() + part[1:])
	return ''.join(output)

def hyphens_to_camel(s):
	output = hyphens_to_pascal(s)
	return output[0].lower() + output[1:]
