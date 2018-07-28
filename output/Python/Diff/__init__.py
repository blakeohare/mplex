from .pyNative import BRIDGE as BRIDGE_

class DiffEngine:
	def __init__(self):
		# TODO: configure options
		pass
	
	def diff(self, left, right):
		left_lines = left.replace('\r\n', '\n').split('\n')
		right_lines = right.replace('\r\n', '\n').split('\n')
		lines_out = []
		ops_out = []
		BRIDGE_.DiffText(left_lines, len(left_lines), right_lines, len(right_lines), lines_out, ops_out)
		return DiffResult(lines_out, ops_out)

class DiffResult:
	def __init__(self, lines, ops):
		self.lines = []
		for line, op in zip(lines, ops):
			op_char = ' '
			if op == 1: op_char = '+'
			elif op == -1: op_char = '-'
			self.lines.append(DiffLine(line, op_char))

class DiffLine:
	def __init__(self, value, op):
		self.value = value
		self.op = op
