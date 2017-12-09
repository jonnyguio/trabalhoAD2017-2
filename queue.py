# -*- coding: utf-8 -*-
import collections as clt


class Queue(object):
	"""docstring for Queue"""
	def __init__(self, queue_type="fcfs"):
		super(Queue, self).__init__()
		self.__queue_type = queue_type
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

	def pushleft(self, client):
		self.__params["deque"].appendleft(client)

	def pop(self):
		if len(self.__params["deque"]) == 0:
			return None
		if self.__queue_type == "fcfs":
			return self.__params["deque"].popleft()
		return self.__params["deque"].pop()