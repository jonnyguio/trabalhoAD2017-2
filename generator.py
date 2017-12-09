# -*- coding: utf-8 -*-
import numpy as np
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE_1, EVENT_TYPE_END_SERVICE_2

class Generator:
    def __init__(self, lamb, mu1):
        self.__betha = [1./lamb, 1./mu1] 
    
    def next_arrival_event(time):
        time_sample = np.random.exponential(scale=self.__betha[0], size=None)
        return Event({} , time+time_sample, EVENT_TYPE_ARRIVAL)

    def next_end_service_1_event(time):
        time_sample = np.random.exponential(scale=self.__betha[1], size=None)
        return Event({} , time+time_sample, EVENT_TYPE_END_SERVICE_1)

    def next_end_service_2_event(time):
        time_sample = np.random.exponential(scale=self.__betha[1], size=None)
        return Event({} , time+time_sample, EVENT_TYPE_END_SERVICE_2)