# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import chi2, t
import pandas as pd

path = "testes/fase_transiente/metrics"

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
    metrics_name = ["E[Nq1]", "E[Nq2]", "E[N1]", "E[N2]", "E[T1]", "E[W1]", "E[T2]", "E[W2]", "V[W1]", "V[W2]"]

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
        self.__area_people_time_line_1 = 0
        self.__area_people_time_line_2 = 0
        self.__area_people_time_1 = 0
        self.__area_people_time_2 = 0

    def __str__(self):
        return self.__pd.__str__()

    def mean_confidence_interval(self, samples, confidence=0.95):
        n = len(samples)
        alpha = 1 - confidence
        mean = np.mean(samples)
        stdn = np.std(samples) / (n**0.5)
        e0 = t.ppf( alpha/2., n-1 )*stdn
        return (mean-e0, mean+e0)

    def mean_confidence_precision(self, final_metrics, metric):
        return (final_metrics[metric][0] - final_metrics[metric][1]) / (final_metrics[metric][0] + final_metrics[metric][1])

    def variance_confidence_interval(self, samples, confidence=0.95):
        n = len(samples)
        alpha = 1 - confidence
        Sn = np.mean(samples) * (n-1)
        right = chi2.ppf( alpha/2., n-1 )
        left = chi2.ppf( 1-alpha/2., n-1 )
        return (Sn/left, Sn/right)

    def variance_confidence_precision(self, n, confidence=0.95):
        alpha = 1-confidence
        a = chi2.ppf(1-alpha/2., n-1)
        b = chi2.ppf(alpha/2., n-1)
        p = (a - b)/(a + b)
        return p

    def add_service_type(self, new_server_type):
        self.__service_type.append(new_server_type)
    def get_service_type(self):
        return self.__service_type

    def add(self, new_client):
        self.clients_list.append(new_client)

    def get_final_metrics(self):
        return self.__final_metrics

    def run(self, clients):
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

        final_metrics["S(E[T1])"] = self.mean_confidence_interval([metric["E[T1]"] for metric in self.__metrics])
        final_metrics["S(E[W1])"] = self.mean_confidence_interval([metric["E[W1]"] for metric in self.__metrics])
        final_metrics["S(E[T2])"] = self.mean_confidence_interval([metric["E[T2]"] for metric in self.__metrics])
        final_metrics["S(E[W2])"] = self.mean_confidence_interval([metric["E[W2]"] for metric in self.__metrics])
        final_metrics["S(E[N1])"] = self.mean_confidence_interval([metric["E[N1]"] for metric in self.__metrics])
        final_metrics["S(E[N2])"] = self.mean_confidence_interval([metric["E[N2]"] for metric in self.__metrics])
        final_metrics["S(E[Nq1])"] = self.mean_confidence_interval([metric["E[Nq1]"] for metric in self.__metrics])
        final_metrics["S(E[Nq2])"] = self.mean_confidence_interval([metric["E[Nq2]"] for metric in self.__metrics])
        final_metrics["S(V[W1])"] = self.variance_confidence_interval([metric["V[W1]"] for metric in self.__metrics])
        final_metrics["S(V[W2])"] = self.variance_confidence_interval([metric["V[W2]"] for metric in self.__metrics])

        final_metrics["p(S(E[T1]))"] = self.mean_confidence_precision(final_metrics, "S(E[T1])")
        final_metrics["p(S(E[W1]))"] = self.mean_confidence_precision(final_metrics, "S(E[W1])")
        final_metrics["p(S(E[T2]))"] = self.mean_confidence_precision(final_metrics, "S(E[T2])")
        final_metrics["p(S(E[W2]))"] = self.mean_confidence_precision(final_metrics, "S(E[W2])")
        final_metrics["p(S(E[N1]))"] = self.mean_confidence_precision(final_metrics, "S(E[N1])")
        final_metrics["p(S(E[N2]))"] = self.mean_confidence_precision(final_metrics, "S(E[N2])")
        final_metrics["p(S(E[Nq1]))"] = self.mean_confidence_precision(final_metrics, "S(E[Nq1])")
        final_metrics["p(S(E[Nq2]))"] = self.mean_confidence_precision(final_metrics, "S(E[Nq2])")
        final_metrics["p(S(V[W1]))"] = self.variance_confidence_precision(clients)
        final_metrics["p(S(V[W2]))"] = self.variance_confidence_precision(clients)
        final_metrics["p2(S(V[W1]))"] = self.mean_confidence_precision(final_metrics, "S(V[W1])")
        final_metrics["p2(S(V[W2]))"] = self.mean_confidence_precision(final_metrics, "S(V[W2])")

        self.__final_metrics = final_metrics
        self.__pd = pd.DataFrame(final_metrics.items())
        return final_metrics

    def run_event(self, clients_now): 
        return [self.__new_metrics["E[Nq1]"] / float(clients_now),
                     self.__new_metrics["E[Nq2]"] / float(clients_now),
                     self.__new_metrics["E[N1]"] / float(clients_now),
                     self.__new_metrics["E[N2]"] / float(clients_now),
                     self.__new_metrics["E[T1]"] / float(clients_now),
                     self.__new_metrics["E[W1]"] / float(clients_now),
                     self.__new_metrics["E[T2]"] / float(clients_now),
                     self.__new_metrics["E[W2]"] / float(clients_now),
                     self.__new_metrics["V[W1]"] / float(clients_now) - (self.__new_metrics["E[W1]"] / float(clients_now))**2,
                     self.__new_metrics["V[W2]"] / float(clients_now) - (self.__new_metrics["E[W2]"] / float(clients_now))**2]

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
        self.__new_metrics["V[W1]"] = self.__new_metrics["V[W1]"] / float(self.__total_samples) - self.__new_metrics["E[W1]"]**2
        self.__new_metrics["V[W2]"] = self.__new_metrics["V[W2]"] / float(self.__total_samples) - self.__new_metrics["E[W2]"]**2
        # self.__new_metrics["area_people_time_1"] = self.__area_people_time_1
        # self.__new_metrics["area_people_time_2"] = self.__area_people_time_2
        # self.__new_metrics["area_people_time_line_1"] = self.__area_people_time_line_1
        # self.__new_metrics["area_people_time_line_2"] = self.__area_people_time_line_2
        self.__metrics.append(self.__new_metrics.copy())
        self.__new_metrics["E[Nq1]"] = 0.0
        self.__new_metrics["E[Nq2]"] = 0.0
        self.__new_metrics["E[N1]"] = 0.0
        self.__new_metrics["E[N2]"] = 0.0
        self.__new_metrics["E[T1]"] = 0.0
        self.__new_metrics["E[W1]"] = 0.0
        self.__new_metrics["E[T2]"] = 0.0
        self.__new_metrics["E[W2]"] = 0.0
        self.__new_metrics["V[W1]"] = 0.0
        self.__new_metrics["V[W2]"] = 0.0

    def print_last_round(self):
        _pd = pd.DataFrame(self.__metrics[len(self.__metrics) - 1].items())
        print(_pd)

    def get_metrics(self):
        return self.__new_metrics

    def add_sample_queue1(self, queue1, server, time_i, time_i_1):
        self.__area_people_time_line_1 += (time_i_1 - time_i) * queue1.get_len()
        self.__area_people_time_1 += (time_i_1 - time_i) * (queue1.get_len() + 1 if server.service_type() == 1 else queue1.get_len())

    def add_sample_queue2(self, queue2, server, time_i, time_i_1):
        self.__area_people_time_line_2 += (time_i_1 - time_i) * queue2.get_len()
        self.__area_people_time_2 += (time_i_1 - time_i) * (queue2.get_len() + 1 if server.service_type() == 2 else queue2.get_len())

    def add_sample_queues(self, queue1, queue2, server):
        self.__new_metrics["E[Nq1]"] += queue1.get_len()
        self.__new_metrics["E[Nq2]"] += queue2.get_len()
        self.__new_metrics["E[N1]"] += (queue1.get_len() + 1 if server.service_type() == 1 else queue1.get_len())
        self.__new_metrics["E[N2]"] += (queue2.get_len() + 1 if server.service_type() == 2 else queue2.get_len())
    
    def add_sample_end_1(self, client):
        # values = {}
        # values["E[T1]"] = client.get_end_service_1() - client.get_start_queue_1()
        # values["E[W1]"] = client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1()
        # values["V[W1]"] = (client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1())**2
        self.__new_metrics["E[T1]"] += client.get_end_service_1() - client.get_start_queue_1()
        self.__new_metrics["E[W1]"] += client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1()
        self.__new_metrics["V[W1]"] += (client.get_end_service_1() - client.get_start_queue_1() - client.get_service_time_1())**2
        # for metric in ['E[T1]', 'E[W1]', 'V[W1]']:
        #     with file("{}-{}.txt".format(path, metric), 'a') as new_file:
        #         new_file.write("{}\n".format(values[metric]))
    
    def add_sample_end_2(self, client):
        # values = {}
        # values["E[T2]"] = client.get_end_service_2() - client.get_start_queue_2()
        # values["E[W2]"] = client.get_end_service_2() - client.get_start_queue_2() - client.get_service_time_2()
        # values["V[W2]"] = (client.get_end_service_2() - client.get_start_queue_2() - client.get_service_time_2())**2
        self.__new_metrics["E[T2]"] += client.get_end_service_2() - client.get_start_queue_2()
        self.__new_metrics["E[W2]"] += client.get_end_service_2() - client.get_start_queue_2() - client.get_total_service_time_2()
        self.__new_metrics["V[W2]"] += (client.get_end_service_2() - client.get_start_queue_2() - client.get_total_service_time_2())**2
        # for metric in ['E[T2]', 'E[W2]', 'V[W2]']:
        #     with file("{}-{}.txt".format(path, metric), 'a') as new_file:
        #         new_file.write("{}\n".format(values[metric]))

        
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
