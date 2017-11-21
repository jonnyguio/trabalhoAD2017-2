# -*- coding: utf-8 -*-
import numpy as np

class Server(object):
	"""docstring for Server"""
	def __init__(self, mu=1.0, start_time=0.0):
		super(Server, self).__init__()
		self.__params = self.make_params_dict(mu, start_time)

	def make_params_dict(self, mu, start_time):
		return dict(zip(
			["is_empty","mu","start_time","service"],
			[True, mu, start_time, start_time]
		))

	#Retorna os parâmetros da classe
	def get_params(self):
		return self.__params

	#Avisa quando o servitor está ocupado ou não
	def is_empty(self):
		return self.__params["is_empty"]

	#Este método executará o serviço e retornará o tempo de serviço
	def do_service(self, start_time):
		#Caso o servidor esteja ocupado, não faça o serviço
		assert self.__params["is_empty"]

		beta = 1./ self.__params["mu"]
		self.__params["is_empty"] = False
		self.__params["start_time"] = start_time
		self.__params["service"] = np.random.exponential(scale=beta, size=None)
		return self.__params["service"]

	#Dado o tempo atual da simulação, este método atualiza o servidor
	def update(self, start_time):
		self.__params["is_empty"] = (start_time - self.__params["start_time"]) >= (self.__params["service"] - 0.0001)
		self.__params["start_time"] = start_time