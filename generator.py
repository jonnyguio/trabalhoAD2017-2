# -*- coding: utf-8 -*-
import numpy as np
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE_1, EVENT_TYPE_END_SERVICE_2

class Generator:
    def __init__(self, lamb, mu1, mu2):
        self.__betha = [1./lamb, 1./mu1]

    def arrival_time(self):
        return np.random.exponential(scale=self.__betha[0], size=None)

    def end_service_1_time(self):
        return np.random.exponential(scale=self.__betha[1], size=None)

    def end_service_2_time(self):
        return np.random.exponential(scale=self.__betha[1], size=None)
    
    def arrival_event(self, time):
        time_sample = self.arrival_time()
        return Event(time+time_sample, EVENT_TYPE_ARRIVAL)

    def end_service_1_event(self, time, client):
        return Event(time + client.get_service_time_1(), EVENT_TYPE_END_SERVICE_1)

    def end_service_2_event(self, time, client):
        return Event(time + client.get_service_time_2(), EVENT_TYPE_END_SERVICE_2)