# -*- coding: utf-8 -*-



class Client(object):
	"""docstring for Queue"""
	def __init__(self, time_in, time_out, color):
		super(Client, self).__init__()
		self.time_in = time_in
		self.time_out = time_out