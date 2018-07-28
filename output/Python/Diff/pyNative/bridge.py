from .pastelgen import *
from .genbridge import GeneratedBridge

class Bridge(GeneratedBridge):
	def DiffText(self, text1, text1Length, text2, text2Length, textOut, changeOut):
		GenerateTextDiff(text1, text1Length, text2, text2Length, textOut, changeOut)

BRIDGE = Bridge()
