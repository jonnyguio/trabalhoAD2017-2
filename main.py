# -*- coding: utf-8 -*-
# CONSTANTS

# DATA STRUCTURES
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE_1, EVENT_TYPE_END_SERVICE_2
from heapq import heappush, heappop
from queue import Queue
from generator import Generator
from copy import deepcopy


# GLOBAL VARIABLES
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

#HELPER FUNCTIONS
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

#método que pega o próximo cliente, coloca no servidor e cria o evento indicando
def set_client_on_server(queue, server):
    next_client = queue.pop()
    server.push(next_client)

    event_end_service_1 = generator.end_service_1_event(total_time, next_client)
    push_event(listEvents, event_end_service_1)

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
            #move o cliente da fila para o servidor e cria o evento de término do serviço
            set_client_on_server(queue1, server)

            # falta adicionar todos os eventos de chegadas que devem existir
            # como o time_temp será incrementado, não queremos passar total_time como referência
            time_in = total_time
            time_out = event_end_service_1.start_time
            push_k_arrival_events(time_in, time_out)

        #caso o servidor esteja ocupado, nada acontecerá caso seja o cliente 1, caso seja o cliente 2, ele sofrerá preempção
        elif server.service_type == 2:
            #retira o cliente 2 do servidor
            client_running = server.pop()

            #atualiza o tempo de serviço pelo residual
            event = filter(lambda event: event.n_type == EVENT_TYPE_END_SERVICE_2, listEvents)
            client_running.set_service_time_2(event.start_time - total_time)

            #coloque o cliente que estava no servidor no inicio da fila 2
            queue2.pushleft(client_running)

            #remova o evento do serviço do tipo 2 da heap de eventos
            listEvents = filter(lambda event: event.n_type != EVENT_TYPE_END_SERVICE_2, listEvents)

            #adiciona um novo evento de chegada 
            
            ---------------------------------------------------------------------------------
            ---------------------------------------------------------------------------------

            #move o cliente da fila para o servidor e cria o evento de término do serviço
            set_client_on_server(queue1, server)

    # caso o evento seja o fim do serviço 1, temos que colocá-lo na fila2, atender o próximo ou ficar ocioso
    # o cliente 1 com certeza estará no servidor
    elif event.type == EVENT_TYPE_END_SERVICE_1:
            #vamos tirar o cliente do servidor, colocá-lo na segunda fila e setar o tempo global dele
            client = server.pop()
            client.set_end_service_1(total_time)
            client.set_start_queue_2(total_time)
            queue2.push(client)

            #caso a fila 1 esteja, vamos atender o próximo da fila 2
            #repare que sempre terá pelo menos uma pessoa na fila 2 nesse momento
            if queue1.is_empty():
                #move o cliente da fila para o servidor e cria o evento de término do serviço
                set_client_on_server(queue2, server)     

            #caso a fila 1 tenha alguém, vamos pegar o próximo da fila 1
            else:
                #move o cliente da fila para o servidor e cria o evento de término do serviço
                set_client_on_server(queue1, server)

        elif event.type == EVENT_TYPE_END_SERVICE_2:
            client = server.pop()
            client.set_end_service_2(total_time)

            if queue1.is_empty() and not queue2.is_empty():
                #move o cliente da fila para o servidor e cria o evento de término do serviço
                set_client_on_server(queue2, server)
            else:
                #move o cliente da fila para o servidor e cria o evento de término do serviço
                set_client_on_server(queue1, server)
        



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