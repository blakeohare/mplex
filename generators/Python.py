from .common import *

class PythonGenerator:

	def get_lang_name(self):
		return 'Python'
	
	def generate_bridge_files(self, metadata, output_directory):
		output = []
		output.append('# This code is generated.\n')
		output.append('class GeneratedBridge:\n')
		
		for method in metadata['methods']:
			name = method['name']
			args = method['args']
			output.append('\tdef ')
			output.append(hyphens_to_pascal(name))
			output.append('(self')
			for arg in args:
				output.append(', ')
				output.append(hyphens_to_camel(arg['name']))
			output.append('):\n')
			output.append('\t\traise Exception("Not implemented.")\n\n')
		output.append('\tdef _mplex_validate(): pass\n')
		write_file_and_create_dir(os.path.join(output_directory, 'pyNative', 'genbridge.py'), ''.join(output))
		write_file_and_create_dir(os.path.join(output_directory, 'pyNative', '__init__.py'), 'from .bridge import BRIDGE\nBRIDGE._mplex_validate()\n')
		# TODO: if output directory does not have a bridge.py, then create one that extends GeneratedBridge.
		
