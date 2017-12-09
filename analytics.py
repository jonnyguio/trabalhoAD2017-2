# -*- coding: utf-8 -*-
import numpy as np

class Analytics():

    __metrics_base = {
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
        self.clients_list = []
            #dtype={
            #"names": ["end_service_1", "end_service_2", "start_queue_1", "start_queue_2"],
            #"formats": []})
        self.total_clients = 0
        self.__metrics = []
        self.__final_metrics = {}
        self.__people_on_queue1 = []
        self.__people_on_queue2 = []

    def add_people_on_queue1(self, new_count):
        self.__people_on_queue1.append(new_count)
    def get_people_on_queue1(self):
        return self.__people_on_queue1

    def add_people_on_queue2(self, new_count):
        self.__people_on_queue2.append(new_count)
    def get_people_on_queue2(self):
        return self.__people_on_queue2

    def add(self, new_client):
        self.clients_list.append(new_client)

    def get_final_metrics(self):
        return self.__final_metrics

    def run(self):
        final_metrics = self.__metrics_base.copy()
        final_metrics["E[T1]"] = np.mean([metric["E[T1]"] for metric in self.__metrics])
        final_metrics["E[W1]"] = np.mean([metric["E[W1]"] for metric in self.__metrics])
        final_metrics["E[T2]"] = np.mean([metric["E[T2]"] for metric in self.__metrics])
        final_metrics["E[W2]"] = np.mean([metric["E[W2]"] for metric in self.__metrics])
        final_metrics["E[N1]"] = np.mean([metric["E[N1]"] for metric in self.__metrics])
        final_metrics["E[N2]"] = np.mean([metric["E[N2]"] for metric in self.__metrics])
        final_metrics["E[Nq1]"] = np.mean([metric["E[Nq1]"] for metric in self.__metrics])
        final_metrics["E[Nq2]"] = np.mean([metric["E[Nq2]"] for metric in self.__metrics])
        final_metrics["V[W1]"] = np.mean([metric["V[W1]"] for metric in self.__metrics])
        final_metrics["V[W2]"] = np.mean([metric["V[W2]"] for metric in self.__metrics])
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
        new_metrics["E[T1]"] = np.mean([client.get_end_service_1() - client.get_start_queue_1() for client in self.clients_list])
        new_metrics["E[W1]"] = np.mean([client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1() for client in self.clients_list])
        new_metrics["E[T2]"] = np.mean([client.get_end_service_2() - client.get_start_queue_2() for client in self.clients_list])
        new_metrics["E[W2]"] = np.mean([client.get_end_service_2() - client.get_start_queue_2() - client.get_total_service_time_2() for client in self.clients_list])
        new_metrics["E[Nq1]"] = np.mean(self.__people_on_queue1)
        new_metrics["E[Nq2]"] = np.mean(self.__people_on_queue2)
        return new_metrics
