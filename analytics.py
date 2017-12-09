# -*- coding: utf-8 -*-
import numpy

class Analytics():

    metrics_base = {
        "E[T1]": 0,
        "E[W1]": 0,
        "E[N1]": 0,
        "E[Nq1]": 0,
        "E[T2]": 0,
        "E[W2]": 0,
        "E[N2]": 0,
        "E[Nq2]": 0,
        "V[W1]": 0,
        "V[W2]": 0
    }

    def __init__(self):
        self.clients_list = np.array(dtype={names: ["end_service_1", "end_service_2", "start_queue_1", "start_queue_2"], formats: []})
        self.total_clients = 0
        self.metrics = []
    
    def add(self, new_client):
        self.clients_list.append(new_client)
    
    def add_round(self):
        metrics.append(self.__new_metric_entry())
    
    def __new_metric_entry():
        new_metrics = metrics_base
        
        return new_metrics
