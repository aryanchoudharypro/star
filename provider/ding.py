from provider import star_provider

class ding(star_provider):
	def synthesize(self, voice, text, *args, **kwargs):
		with open("C:\\windows\\media\\ding.wav", "rb") as f: return f.read()
	def get_voices(self): return "dingthing"

ding()
