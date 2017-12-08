# -*- coding: utf-8 -*-
EVENT_TYPE_ARRIVAL = "ARRIVAL"
EVENT_TYPE_END_SERVICE1 = "END_OF_SERVICE1"
EVENT_TYPE_END_SERVICE2 = "END_OF_SERVICE2"
EVENT_TYPE_PREEMPTION = "PREEMPTION"

class Event:
    def __init__(self, event_data, start_time, n_type):
        self.data = event_data
        self.type = n_type
        self.start_time = start_time
        self.next = None
    
    #função de comparação para ordenar na heap
    def __lt__(self, other):
        return self.start_time < other.start_time
    
    def set_next(self, n_next):
        self.next = n_next
    
    def get_next(self):
        return self.next

    def set_event_data(self, n_event_data):
        self.event_data = n_event_data

    def get_event_data(self):
        return self.data

    def set_start_time(self, n_start_time):
        self.start_time = n_start_time
        
    def get_start_time(self):
        return self.start_time

    def insert_event(event_list_begin, new_event):
        if event_list_begin.get_next() is not None:
            insert_event(event_list_begin.get_next(), new_event)
        else:
            event_list_begin.set_next(new_event)
    
    def pop_event(event_list_begin):
        event = event_list_begin
        event_list_begin = event_list_begin.get_next()
        return event.data, event.type, event.start_time
