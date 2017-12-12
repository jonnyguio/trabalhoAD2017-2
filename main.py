# -*- coding: utf-8 -*-
# DATA STRUCTURES
import os
import time
import sys
import random
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE1, EVENT_TYPE_END_SERVICE2
from heapq import heappush, heappop
from queue import Queue
from server import Server
from client import Client
from generator import Generator
from copy import deepcopy
from analytics import Analytics


# GLOBAL VARIABLES
TOTAL_ROUNDS = int(sys.argv[3])
TOTAL_CLIENTS = int(sys.argv[1])
TRANSIENT_STAGE = int(sys.argv[2])
SERVICE_1 = 1
SERVICE_2 = 2
try:
    DEBUG = bool(sys.argv[4]) 
except IndexError:
    DEBUG = False


number_clients = 0

listEvents = [] #inicializacao da heap

server = Server()
queue1 = Queue()
queue2 = Queue()
generator = Generator(lamb=0.1, mu=1)
analytics = Analytics(TOTAL_CLIENTS - TRANSIENT_STAGE)

total_time = 0
idle_time = 0

#HELPER FUNCTIONS
def log_event(event):
    print "#############"
    # print "Heap: {}".format([event.get_start_time() for event in listEvents])
    print "Ocorreu um evento de tipo: " + event.get_type()
    print "Tempo atual: " + str(total_time)

def log_system():
    print ""
    print "Fila 1: " + str(queue1.get_params())
    print "Fila 2: " + str(queue2.get_params())
    print "Servidor: " + str(server.get_params())
    print "#############"

def reset_system():
    global server
    global queue1
    global queue2
    global generator
    global total_time

    server = Server()
    queue1 = Queue()
    queue2 = Queue()
    generator = Generator(lamb=0.1, mu=1, seed=time.time()*time.time() % 10e9)
    total_time = 0

def pop_event(listEvents):
    if len(listEvents) == 0:
        return None
    return heappop(listEvents)

def push_event(listEvents, event):
    heappush(listEvents, event)

def push_k_arrival_events(time_in, time_out):
    #enquanto a chegada do usuário for menor que o tempo do fim do serviço, adiciona o evento de chegada
    time_temp = float(time_in)
    while True:
        event_arrival = generator.arrival_event(time_temp)
        push_event(listEvents, event_arrival)
        time_temp = event_arrival.get_start_time()
        if time_temp > time_out:
            break

#método que pega o próximo cliente, coloca no servidor e cria o evento indicando
def set_client_1_on_server():
    global total_time
    global server
    global queue1
    next_client = queue1.pop()
    server.push(next_client)

    event_end_service = generator.end_service_1_event(total_time, next_client)
    push_event(listEvents, event_end_service)

    # falta adicionar todos os eventos de chegadas que devem existir
    # como o time_temp será incrementado, não queremos passar total_time como referência
    # time_in = total_time
    # time_out = event_end_service.get_start_time()
    # push_k_arrival_events(time_in, time_out)

def set_client_2_on_server():   
    global total_time
    global queue2
    global server
    next_client = queue2.pop()
    server.push(next_client)

    event_end_service = generator.end_service_2_event(total_time, next_client)
    push_event(listEvents, event_end_service)

    # falta adicionar todos os eventos de chegadas que devem existir
    # como o time_temp será incrementado, não queremos passar total_time como referência
    # time_in = total_time
    # time_out = event_end_service.get_start_time()
    # push_k_arrival_events(time_in, time_out)


def deal_event(event):
    global queue1
    global queue2
    global server
    global total_time
    global number_clients
    global listEvents

    #caso o evento seja do tipo arrival, temos duas possibilidades, atender o usuário ou colocá-lo na fila
    if event.get_type() == EVENT_TYPE_ARRIVAL and number_clients < TOTAL_CLIENTS:

        #incrementa o número total de pessoas que entraram no sistema
        number_clients += 1 

        #cria o cliente que chegará no tempo marcado no evento
        if number_clients < TRANSIENT_STAGE:
            new_client = Client( total_time, "TRANSIENT")
        else:
            new_client = Client( total_time, "NON-TRANSIENT")
        new_client.set_service_time_1( generator.end_service_time() )
        new_client.set_service_time_2( generator.end_service_time() ) 
            
        if not new_client.is_transient():
            analytics.add_sample_queues(queue1, queue2, server)
            # analytics.add(new_client)
            # Como todo evento de chegada poisson é uma amostragem aleatória, pegamos a quantidade de pessoas na fila para usarmos no cálculo da média.
            # analytics.add_people_on_queue1(queue1.get_len())
            # analytics.add_people_on_queue2(queue2.get_len())
            # analytics.add_service_type(server.service_type())

        event_arrival = generator.arrival_event(total_time)
        push_event(listEvents, event_arrival)

        # print("Tempo de serviço 1: {}".format(new_client.get_service_time_1()))
        # print("Tempo de serviço 2: {}".format(new_client.get_service_time_2()))
        # coloque-o na fila
        queue1.push( new_client )

        # #só vamos considerar para a estatísticas os clientes que chegarem após a fase transiente
        #caso o servidor esteja livre, colocaremos este cliente no servidor e cria os eventos das k chegadas poisson
        if server.is_empty():
            set_client_1_on_server()
        #caso o servidor esteja ocupado, nada acontecerá caso seja o cliente 1, caso seja o cliente 2, ele sofrerá preempção
        elif server.service_type() == SERVICE_2:
            #retira o cliente 2 do servidor
            client_running = server.pop()

            #atualiza o tempo de serviço pelo residual, sempre tem apenas 1 elemento
            event_end_service = filter(lambda event: event.get_type() == EVENT_TYPE_END_SERVICE2, listEvents)[0]
            client_running.set_service_time_2(event_end_service.get_start_time() - total_time)

            #coloque o cliente que estava no servidor no inicio da fila 2
            queue2.pushleft(client_running)

            #remova o evento do serviço do tipo 2 da heap de eventos
            listEvents = filter(lambda event: event.get_type() != EVENT_TYPE_END_SERVICE2, listEvents)

            #move o cliente da fila para o servidor e cria o evento de término do serviço
            set_client_1_on_server()
            
    # caso o evento seja o fim do serviço 1, temos que colocá-lo na fila2, atender o próximo ou ficar ocioso
    # o cliente 1 com certeza estará no servidor
    elif event.get_type() == EVENT_TYPE_END_SERVICE1:
        #vamos tirar o cliente do servidor, colocá-lo na segunda fila e setar o tempo global dele
        client = server.pop()
        client.set_end_service_1( total_time )
        client.set_start_queue_2( total_time )
        queue2.push(client)
        if not client.is_transient():
            analytics.add_sample_end_1(client)

        #caso a fila 1 esteja, vamos atender o próximo da fila 2
        #repare que sempre terá pelo menos uma pessoa na fila 2 nesse momento
        if queue1.is_empty():
            #move o cliente da fila para o servidor e cria o evento de término do serviço
            if not queue2.is_empty():
                set_client_2_on_server()

        #caso a fila 1 tenha alguém, vamos pegar o próximo da fila 1
        else:
            #move o cliente da fila para o servidor e cria o evento de término do serviço
            set_client_1_on_server()

    elif event.get_type() == EVENT_TYPE_END_SERVICE2:
        client = server.pop()
        client.set_end_service_2( total_time )
        if not client.is_transient():
            analytics.add_sample_end_2(client)

        if queue1.is_empty():
            #move o cliente da fila para o servidor e cria o evento de término do serviço
            if not queue2.is_empty():
                set_client_2_on_server()
        else:
            #move o cliente da fila para o servidor e cria o evento de término do serviço
            set_client_1_on_server()
        


def simulate():
    rounds = 0
    global total_time
    global idle_time
    global number_clients
    global analytics

    while rounds < TOTAL_ROUNDS:
        number_clients = 0
        print("round {}:".format(rounds))
        reset_system()

        while number_clients < TOTAL_CLIENTS or len(listEvents) > 0:
            if DEBUG:
                print("number of clients: {}".format(number_clients))
            event = pop_event(listEvents) # pega o minimo da lista (proximo evento)

            # se o sistema estiver ocioso, vamos esperar uma chegada
            if event is None:
                event = generator.arrival_event(total_time)
                idle_time += event.get_start_time() - total_time

            total_time = event.get_start_time()
            if DEBUG:
                log_event(event)
            deal_event(event)
            if DEBUG:
                log_system()
        analytics.run_round()
        analytics.print_last_round()
        rounds += 1
    analytics.run(TOTAL_CLIENTS)
    print(analytics)
    # print(analytics.get_metrics())
    # print(analytics.get_final_metrics())

if __name__ == '__main__':
    simulate()