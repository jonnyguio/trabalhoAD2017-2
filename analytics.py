# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class Analytics():

    __metrics_base = {
        "E[T1]": 0.0,
        "E[W1]": 0.0,
        "E[N1]": 0.0,
        "E[Nq1]": 0.0,
        "E[T2]": 0.0,
        "E[W2]": 0.0,
        "E[N2]": 0.0,
        "E[Nq2]": 0.0,
        "V[W1]": 0.0,
        "V[W2]": 0.0
    }

    def __init__(self, total_samples):
        self.clients_list = []
            #dtype={
            #"names": ["end_service_1", "end_service_2", "start_queue_1", "start_queue_2"],
            #"formats": []})
        self.total_clients = 0
        self.__metrics = []
        self.__final_metrics = {}
        self.__people_on_queue1 = []
        self.__people_on_queue2 = []
        self.__service_type = []
        self.__total_samples = total_samples
        self.__new_metrics = self.__metrics_base.copy()
        self.__pd = []

    def __str__(self):
        return self.__pd.__str__()

    def add_people_on_queue1(self, new_count):
        self.__people_on_queue1.append(new_count)
    def get_people_on_queue1(self):
        return self.__people_on_queue1

    def add_people_on_queue2(self, new_count):
        self.__people_on_queue2.append(new_count)
    def get_people_on_queue2(self):
        return self.__people_on_queue2

    def add_service_type(self, new_server_type):
        self.__service_type.append(new_server_type)
    def get_service_type(self):
        return self.__service_type

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
        self.__pd = pd.DataFrame(final_metrics.items())
        return final_metrics

    def run_round(self):
        # self.__add_round()
        self.__new_metrics["E[Nq1]"] /= float(self.__total_samples)
        self.__new_metrics["E[Nq2]"] /= float(self.__total_samples)
        self.__new_metrics["E[N1]"] /= float(self.__total_samples)
        self.__new_metrics["E[N2]"] /= float(self.__total_samples)
        self.__new_metrics["E[T1]"] /= float(self.__total_samples)
        self.__new_metrics["E[W1]"] /= float(self.__total_samples)
        self.__new_metrics["E[T2]"] /= float(self.__total_samples)
        self.__new_metrics["E[W2]"] /= float(self.__total_samples)
        self.__metrics.append(self.__new_metrics.copy())
        self.__new_metrics["E[Nq1]"] = 0.0
        self.__new_metrics["E[Nq2]"] = 0.0
        self.__new_metrics["E[N1]"] = 0.0
        self.__new_metrics["E[N2]"] = 0.0
        self.__new_metrics["E[T1]"] = 0.0
        self.__new_metrics["E[W1]"] = 0.0
        self.__new_metrics["E[T2]"] = 0.0
        self.__new_metrics["E[W2]"] = 0.0

    def get_metrics(self):
        return self.__metrics

    def add_sample_queues(self, queue1, queue2, server):
        self.__new_metrics["E[Nq1]"] += queue1.get_len()
        self.__new_metrics["E[Nq2]"] += queue2.get_len()
        self.__new_metrics["E[N1]"] += (queue1.get_len() + 1 if server.service_type() == 1 else queue1.get_len())
        self.__new_metrics["E[N2]"] += (queue2.get_len() + 1 if server.service_type() == 2 else queue2.get_len())
    
    def add_sample_end_1(self, client):
        self.__new_metrics["E[T1]"] += client.get_end_service_1() - client.get_start_queue_1()
        self.__new_metrics["E[W1]"] += client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1()
    
    def add_sample_end_2(self, client):
        self.__new_metrics["E[T2]"] += client.get_end_service_2() - client.get_start_queue_2()
        self.__new_metrics["E[W2]"] += client.get_end_service_2() - client.get_start_queue_2() - client.get_total_service_time_2()

        
    # def __add_round(self):
    #     new_metric = self.__new_metric_entry()
    #     self.__metrics.append(new_metric)

    # def __new_metric_entry(self):
    #     new_metrics = self.__metrics_base.copy()
    #     new_metrics["E[T1]"] = np.mean([client.get_end_service_1() - client.get_start_queue_1() for client in self.clients_list])
    #     new_metrics["E[W1]"] = np.mean([client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1() for client in self.clients_list])
    #     new_metrics["E[T2]"] = np.mean([client.get_end_service_2() - client.get_start_queue_2() for client in self.clients_list])
    #     new_metrics["E[W2]"] = np.mean([client.get_end_service_2() - client.get_start_queue_2() - client.get_total_service_time_2() for client in self.clients_list])
    #     new_metrics["E[Nq1]"] = np.mean(self.__people_on_queue1)
    #     new_metrics["E[Nq2]"] = np.mean(self.__people_on_queue2)
    #     new_metrics["E[N1]"] = np.mean([people + 1 if self.__service_type[index] == 1 else people for index, people in enumerate(self.__people_on_queue1)])
    #     new_metrics["E[N2]"] = np.mean([people + 1 if self.__service_type[index] == 2 else people for index, people in enumerate(self.__people_on_queue2)])
    #     return new_metrics
