# -*- coding: utf-8 -*-
# CONSTANTS

# DATA STRUCTURES
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE_1, EVENT_TYPE_PREEMPTION
from heapq import heappush, heappop
from queue import Queue
from generator import Generator
from copy import deepcopy

TOTAL_ROUNDS = 10
TOTAL_CLIENTS = 10000
TRANSIENT_STAGE = 1000

number_clients = 0

listEvents = [] #inicializacao da heap

server = # inicializa server
queue1 = Queue()
queue2 = Queue()
generator = Generator()

total_time = 0
idle_time = 0

def create_client(time1=None, time=None):


def pop_event(listEvents):
    if len(listEvents) == 0:
        return None
    return heappop(listEvents)

def push_event(listEvents, event):
    heappush(listEvents, event)

def push_k_arrival_events(time_in, time_out):
    time_temp = deepcopy(time_in)
    event_arrival = generator.arrival_event(time_temp)
    push_event(listEvents, event_arrival)

    #enquanto a chegada do usuário for menor que o tempo do fim do serviço, adiciona o evento de chegada
    while(event_arrival <= event_end_service_1):
        time_temp = event_arrival.start_time
        event_arrival = generator.arrival_event(time_temp)
        push_event(listEvents, event_arrival)

def deal_event(event):
    #caso o evento seja do tipo arrival, temos duas possibilidades, atender o usuário ou colocá-lo na fila
    if event.type == EVENT_TYPE_ARRIVAL:

        #cria o cliente que chegará no tempo marcado no evento
        new_client = Client(total_time)
        new_client.set_service_time_1( generator.end_service_1_time() )
        new_client.set_service_time_2( generator.end_service_2_time() )
        #coloque-o na fila
        queue.push(new_client)
        #incrementa o número total de pessoas que entraram no sistema
        number_clients += 1 

        #só vamos considerar para a estatísticas os clientes que chegarem após a fase transiente
        if number_clients > TRANSIENT_STAGE:
            analytics.add(new_client)

        #caso o servidor esteja livre, colocaremos este cliente no servidor
        if server.is_empty():
            #move o cliente da fila para o servidor
            client = queue1.pop()
            server.push(client)

            #cria o evento que diz quando o serviço irá terminar
            event_end_service_1 = generator.end_service_1_event(total_time, client)
            push_event(listEvents, event_end_service_1)

            # falta adicionar todos os eventos de chegadas que devem existir
            # como o time_temp será incrementado, não queremos passar total_time como referência
            time_in = total_time
            time_out = event_end_service_1.start_time
            push_k_arrival_events(time_in, time_out)

        #caso o servidor esteja ocupado, nada acontecerá caso seja o cliente 1, caso seja o cliente 2, ele sofrerá preempção
        else:
            if server.service_type == 2:
                #retira o cliente 2 do servidor
                client_running = server.pop()

                #atualiza o tempo de serviço pelo residual
                event = filter(lambda event: event.n_type == EVENT_TYPE_PREEMPTION, listEvents)
                client_running.set_service_time_2(event.start_time - total_time)

                #remova o evento do serviço do tipo 2 da heap de eventos
                listEvents = filter(lambda event: event.n_type != EVENT_TYPE_PREEMPTION, listEvents)

                #coloque o cliente 1 no servidor
                server.push(queue1.pop())

                #cria o evento que diz quando o serviço irá terminar
                event_end_service_1 = generator.end_service_1_event(total_time, client)
                push_event(listEvents, event_end_service_1)

    # Falta refatorar a partir daqui: -----------------------------------------------------------------------------------------
    elif event.type == EVENT_TYPE_END_SERVICE_1:
            client = event.data.client
            client.set_end_service_1(total_time)
            client.set_start_queue_2(total_time)
            queue2.push(client)
            
            server.pop()
            if queue1.is_empty():
                if queue2.is_empty():
                    pass
                else:
                    next_client = queue2.pop()
                    server.push(next_client)        
                    listEvents.insert(Event(total_time + next_client.get_service_time_2(), {"client": next_client}, EVENT_TYPE_END_SERVICE_2))
            else:
                next_client = queue1.pop()
                server.push(next_client)
                listEvents.insert(Event(total_time + next_client.get_service_time_1(), {"client": next_client}, EVENT_TYPE_END_SERVICE_1))
        elif event.type == EVENT_TYPE_END_SERVICE_2:
            client = event.data.client
            client.set_end_service_2(total_time) 
            server.pop()
            if queue1.is_empty():
                if queue2.is_empty():
                    pass
                else:
                    next_client = queue2.pop()
                    server.push(next_client)        
                    listEvents.insert(Event(total_time + next_client.get_service_time_2(), {"client": next_client}, EVENT_TYPE_END_SERVICE_2))
            else:
                next_client = queue1.pop()
                server.push(next_client)
                listEvents.insert(Event(total_time + next_client.get_service_time_1(), {"client": next_client}, EVENT_TYPE_END_SERVICE_1))
        



while rounds < TOTAL_ROUNDS:
    while number_clients < TOTAL_CLIENTS:
        event = pop_event(listEvents) # pega o minimo da lista (proximo evento)

        # se o sistema estiver ocioso, vamos esperar uma chegada
        if event is None:
            event = generator.arrival_event(total_time)
            idle_time += event.start_time - total_time

        total_time = event.start_time

        deal_event(event, total_time)

    analytics.run_round()
analytics.run()