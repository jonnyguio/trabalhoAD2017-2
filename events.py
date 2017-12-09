# -*- coding: utf-8 -*-
EVENT_TYPE_ARRIVAL = "ARRIVAL"
EVENT_TYPE_END_SERVICE1 = "END_OF_SERVICE1"
EVENT_TYPE_END_SERVICE2 = "END_OF_SERVICE2"
EVENT_TYPE_PREEMPTION = "PREEMPTION"

class Event(object):
    def __init__(self, start_time, n_type):
        self.__start_time = start_time
        self.__type = n_type
    
    #função de comparação para ordenar na heap
    def __lt__(self, other):
        return self.__start_time < other.__start_time

    def set_start_time(self, n_start_time):
        self.__start_time = n_start_time
        
    def get_start_time(self):
        return self.__start_time

    def get_type(self):
        return self.__type