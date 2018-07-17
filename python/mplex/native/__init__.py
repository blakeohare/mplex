
class NativeBridge:
	def __init__(self, cmdByName):
		self.error_msg = None
		self.commands = cmdByName
	
	def send(self, cmd, args):
		sc = self.commands[cmd](self, args)
		if sc == -1: self.error_msg = "An unknown error occurred."
		return sc
	
	def sendOrThrow(self, cmd, args):
		if self.send(cmd, args) != 0:
			raise Exception(self.error_msg)
	
	def set_error(self, id, message):
		self.error_msg = message
		return id

class BridgeRegistry:
	def __init__(self):
		self.bridges = {}
	
	def register(self, name, bridge):
		self.bridges[name] = bridge
	
	def get(self, name):
		return self.bridges[name]

REGISTRY = BridgeRegistry()
