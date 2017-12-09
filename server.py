# -*- coding: utf-8 -*-
import collections as clt


class Server(object):
	"""docstring for Server"""
	def __init__(self, maxlen=1):
		super(Server, self).__init__()
		self.__params = self.make_params_dict(clt.deque(maxlen=maxlen))
		self.__params = self.make_params_dict(clt.deque())

	def make_params_dict(self, deque):
		return dict(zip(
			["deque"],
			[deque]
		))

	def get_params(self):
		return self.__params

	def get_len(self):
		return len(self.__params["deque"])

	def is_empty(self):
		return self.get_len() == 0

	def push(self, client):
		self.__params["deque"].append(client)

	def pop(self):
		if len(self.__params["deque"]) == 0:
			return None
		return self.__params["deque"].pop()

	def service_type(self):
		if len(self.__params["deque"]) == 0:
			return 0
		elif self.__params["deque"][0].get_start_queue_2() == None:
			return 1
		return 2