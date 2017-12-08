# -*- coding: utf-8 -*-
EVENT_TYPE_ARRIVAL = "ARRIVAL"
EVENT_TYPE_END_SERVICE = "END_OF_SERVICE"
EVENT_TYPE_PREEMPTION = "PREEMPTION"


class Event:
    def __init__(self, event_data, arrive_time, n_type):
        self.data = event_data
        self.type = n_type
        self.arrive_time = arrive_time
        self.next = None
    
    def set_next(self, n_next):
        self.next = n_next
    
    def get_next(self):
        return self.next

    def set_event_data(self, n_event_data):
        self.event_data = n_event_data

    def get_event_data(self):
        return self.data

    def set_arrive_time(self, n_arrive_time):
        self.arrive_time = n_arrive_time
        
    def get_arrive_time(self):
        return self.arrive_time

    def insert_event(event_list_begin, new_event):
        if event_list_begin.get_next() is not None:
            insert_event(event_list_begin.get_next(), new_event)
        else:
            event_list_begin.set_next(new_event)
    
    def pop_event(event_list_begin)
        event = event_list_begin
        event_list_begin = event_list_begin.get_next()
        return event.data, event.type, event.arrive_time
