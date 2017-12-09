# -*- coding: utf-8 -*-
import numpy as np

class Analytics():

    __metrics_base = {
        "E[T1]": 0,
    }

    def __init__(self):
        self.clients_list = []
            #dtype={
            #"names": ["end_service_1", "end_service_2", "start_queue_1", "start_queue_2"],
            #"formats": []})
        self.total_clients = 0
        self.__metrics = []
        self.__final_metrics = {}

    def add(self, new_client):
        self.clients_list.append(new_client)

    def get_final_metrics(self):
        return self.__final_metrics

    def run(self):
        final_metrics = self.__metrics_base.copy()
        final_metrics["E[T1]"] = np.mean([metric["E[T1]"] for metric in self.__metrics])
        self.__final_metrics = final_metrics
        return final_metrics

    def run_round(self):
        self.__add_round()

    def get_metrics(self):
        return self.__metrics

    def __add_round(self):
        new_metric = self.__new_metric_entry()
        self.__metrics.append(new_metric)

    def __new_metric_entry(self):
        new_metrics = self.__metrics_base.copy()
        new_metrics["E[T1]"] = np.mean([client.get_end_service_2() - client.get_start_queue_1() for client in self.clients_list])
        return new_metrics
