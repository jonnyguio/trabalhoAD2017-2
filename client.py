# -*- coding: utf-8 -*-

class Client(object):
	"""docstring for Queue"""
	end_service_1 = None
	end_service_2 = None
	start_queue_1 = None
	start_queue_2 = None
	service_time_1 = None
	service_time_2 = None
	
	color = None

	random_generator = None

	def __init__(self, time_in, color="green"):
		super(Client, self).__init__()
		self.start_queue_1 = time_in
		self.color = color
		# self.service_time_1 = Generator.random_service_time()
		# self.service_time_2 = Generator.random_service_time()
	
	def set_end_service_1(self, n_end_service_1):
		self.end_service_1 = n_end_service_1

	def get_end_service_1(self):
		return self.end_service_1

	def set_end_service_2(self, n_end_service_2):
		self.end_service_2 = n_end_service_2
		
	def get_end_service_2(self):
		return self.end_service_2

	def set_start_queue1(self, n_start_queue1):
		self.start_queue1 = n_start_queue1
		
	def get_start_queue1(self):
		return self.start_queue1

	def set_start_queue2(self, n_start_queue2):
		self.start_queue2 = n_start_queue2

	def get_start_queue2(self):
		return self.start_queue2

	def get_service_time_1(self):
		return self.service_time_1

	def get_service_time_2(self):
		return self.service_time_2

	def set_service_time_1(self, time):
		self.service_time_1 = time

	def set_service_time_2(self, time):
		self.service_time_2 = time