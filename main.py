# main.py

# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib.pyplot as plt
import collections as clt
from queues.exp_queue import Queue
from servers.exp_server import Server


def run_system(queue, queue2, server, epochs, time=0.0):
    busy = 0.0
    idle = 0.0
    queue_size = list()
    est_busy = 0.0

    for idx in range(epochs):
        if server.is_empty() == True:
            client_time = queue.pop_fcfs()
            if client_time == None:
                queue.add_client()
                client_time = queue.pop_fcfs()
                idle += client_time
                time += client_time
                busy = server.do_service(time)
                time += busy
                est_busy += busy
            else:
                busy = server.do_service(time)
                time += busy
                est_busy += busy
        server.update(time)
        queue.update(time)
        if idx%1 == 0:
            queue_size.append(queue.get_len())

    # plt.plot(range(len(queue_size)), queue_size)
    # plt.show()
    ro = est_busy/time
    return ro


def simulateMM1(number_it=100000, lamb=1.0, mu=1.0):
    queue = Queue(lamb=lamb)
    queue2 = Queue(lamb=lamb)
    server = Server(mu=mu)
    ro = run_system(queue, queue2, server, number_it)
    return ro

def MM1(lamb=1.0, mu=1.0):
    ro = lamb/mu
    X = 1/mu
    Nq = ro/(1-ro)
    W = Nq*lamb
    return dict(zip(
        ["W", "Nq", "X", "ro"],
        [W, Nq, X, ro]
    ))

if __name__ == '__main__':
    lamb = 0.8
    mu = 1.0
    number_it = 100000
    ro = simulateMM1(number_it, lamb)
    params = MM1(lamb, mu)
    print(ro, params["ro"])