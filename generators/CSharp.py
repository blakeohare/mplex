from .common import *

class CSharpGenerator(GeneratorBase):

	def __init__(self):
		self.type_cache = {}
		
	def get_lang_name(self):
		return 'CSharp'
	
	def serialize_type_impl(self, mtype):
		if mtype.root == 'Array':
			output = self.serialize_type_impl(mtype.generics[0]) + '[]'
		elif mtype.root == 'Dictionary':
			output = 'System.Collections.Generic.Dictionary<' + self.serialize_type_impl(mtype.generics[0]) + ', ' + self.serialize_type_impl(mtype.generics[1]) + '>'
		elif mtype.root == 'List':
			output = 'System.Collections.Generic.List<' + self.serialize_type_impl(mtype.generics[0]) + '>'
		elif mtype.root == 'Function':
			output = 'System.Func<' + self.serialize_type_impl(mtype.generics[0]) + ', ' + self.serialize_type_impl(mtype.generics[1]) + '>'
		else:
			output = mtype.root
		return output
	
	def generate_bridge_files(self, metadata, output_directory):
		cb = CodeBuilder().use_carriage_return().set_tab(' ' * 4)
		cb.add('namespace ').add(metadata['name']).nl()
		cb.add('{').nl()
		cb.tab(1).add('internal abstract class AbstractBridge').nl()
		cb.tab(1).add('{').nl()
		
		for method in metadata['methods']:
			name = method['name']
			args = method['args']
			return_type = 'void'
			if method.get('returns') != None:
				return_type = self.serialize_type(method['returns']['type'])
			cb.tab(2).add('public abstract ').add(return_type).add(' ').add(hyphens_to_pascal(name)).add('(')
			first = True
			for arg in args:
				arg_name = hyphens_to_camel(arg['name'])
				arg_type = self.serialize_type(arg['type'])
				if first: first = False
				else: cb.add(', ')
				cb.add(arg_type)
				cb.add(' ')
				cb.add(arg_name)
			cb.add(');').nl()
		cb.tab(1).add('}').nl()
		cb.add('}').nl()
		
		write_file_and_create_dir(os.path.join(output_directory, 'mplexgen', 'AbstractBridge.cs'), cb.to_string())
