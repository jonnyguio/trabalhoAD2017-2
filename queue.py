
# -*- coding: utf-8 -*-
import numpy as np
import collections as clt


class Queue(object):
	"""docstring for Queue"""
	def __init__(self, lamb=1.0, start_time=0.0):
		super(Queue, self).__init__()
		self.__params = self.make_params_dict(lamb, start_time, clt.deque())

	def make_params_dict(self, lamb, start_time, deque):
		return dict(zip(
			["lambda", "beta", "start_time", "deque"],
			[lamb, 1./lamb, start_time, deque]
		))

	def get_params(self):
		return self.__params

	def get_len(self):
		return len(self.__params["deque"])

	def get_time(self):
		return self.__params["start_time"]

	def add_client(self, size=None):
		time_client = np.random.exponential(scale=self.__params["beta"], size=size)
		if size is None:
			self.__params["deque"].append(time_client)
			self.__params["start_time"] += time_client
			return time_client
		else:
			self.__params["deque"].extend(time_client)
			return sum(time_client)

	def pop_fcfs(self):
		if len(self.__params["deque"]) == 0:
			return None
		return self.__params["deque"].popleft()

	def pop_lcfs(self):
		if len(self.__params["deque"]) == 0:
			return None
		return self.__params["deque"].pop()

	def update(self, time, prot='FCFS'):
		acc_time = 0.0
		delta_time = time - self.__params["start_time"]

		assert delta_time >= 0

		while acc_time <= (delta_time-0.0001):
			acc_time += self.add_client()

		if prot == 'LCFS':
			self.pop_lcfs()
		else:
			self.pop_fcfs()

		self.__params["start_time"] = time
