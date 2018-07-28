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

class MType:
	def __init__(self, root):
		self.root = root
		self.generics = None
		self.has_generics = False
	def set_generics(self, generics):
		self.generics = generics
		self.has_generics = True
	
def parse_type(type_string):
	t = type_string.replace('<', ' < ')
	t = t.replace('>', ' > ')
	t = t.replace(',', ' , ')
	tokens = t.strip().split()
	tokens.reverse()
	try:
		output = parse_type_impl(tokens)
		if len(tokens) != 0: raise Exception("Bad type")
	except:
		raise Exception("Bad type: '" + type_string + "'")
	return output

_GENERICS = {
	'Dictionary': 2,
	'Function': 2,
	'Array': 1,
	'List': 1,
}

def parse_type_impl(tokens):
	root = tokens.pop()
	mtype = MType(root)
	g_count = _GENERICS.get(root)
	if g_count != None:
		if tokens.pop() != '<': raise Exception("Generics expected for this type")
		generics = []
		for i in range(g_count):
			if i > 0:
				if tokens.pop() != ',': raise Exception("Bad type")
			generics.append(parse_type_impl(tokens))
		if tokens.pop() != '>': raise Exception("Bad type")
		mtype.set_generics(generics)
		
		# An unfortunate limitation of Func<Input, Output> type in C#
		if root == 'Function':
			if mtype.generics[0] == 'void': raise Exception("Function must take 1 input.")
			if mtype.generics[1] == 'void': raise Exception("Function types cannot have void output.")
	
	return mtype

class GeneratorBase:
	def __init__(self):
		pass
	
	def serialize_type(self, type_string):
		output = self.type_cache.get(type_string)
		if output == None:
			mtype = parse_type(type_string)
			output = self.serialize_type_impl(mtype)
			self.type_cache[type_string] = output
		return output
	
class CodeBuilder:
	def __init__(self):
		self.lines = [[]]
		self._nl = '\n'
		self._tab = '\t'
	
	def use_carriage_return(self):
		#self._nl = '\r\n'
		return self
	
	def set_tab(self, tab_string):
		self._tab = tab_string
		return self
	
	def append(self, text):
		return self.add(text)
	
	def add(self, text):
		self.lines[-1].append(text)
		return self
	
	def tab(self, amount = 1):
		self.lines[-1].append(self._tab * amount)
		return self
		
	def nl(self):
		self.lines.append([])
		return self
	
	def to_string(self):
		output = []
		for line in self.lines:
			for chunk in line:
				output.append(chunk)
			output.append(self._nl)
		return ''.join(output)
