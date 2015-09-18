class song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = song(["Happy Birthday to you",
		"I dont want to get sued",
		"So ill stop right there"])

happy_bday.sing_me_a_song()
