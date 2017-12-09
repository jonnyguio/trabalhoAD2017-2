# -*- coding: utf-8 -*-
import numpy as np
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE1, EVENT_TYPE_END_SERVICE2

class Generator:
    def __init__(self, lamb, mu):
        self.__betha = [1./lamb, 1./mu]

    def arrival_time(self):
        return np.random.exponential(scale=self.__betha[0], size=None)

    def end_service_time(self):
        return np.random.exponential(scale=self.__betha[1], size=None)
    
    def arrival_event(self, time):
        time_sample = self.arrival_time()
        # print("Tempo de chegada: {}".format(time_sample))
        return Event(time+time_sample, EVENT_TYPE_ARRIVAL)

    def end_service_1_event(self, time, client):
        return Event(time + client.get_service_time_1(), EVENT_TYPE_END_SERVICE1)

    def end_service_2_event(self, time, client):
        return Event(time + client.get_service_time_2(), EVENT_TYPE_END_SERVICE2)