# -*- coding: utf-8 -*-
# CONSTANTS

# DATA STRUCTURES
from events import Event, EVENT_TYPE_ARRIVAL, EVENT_TYPE_END_SERVICE_1, EVENT_TYPE_PREEMPTION
from queue import Queue

TOTAL_CLIENTS = 10000
TRANSIENT_STAGE = 1000

number_clients = 0

listEvents = # inicializacao da heap

server = # inicializa server
queue1 = Queue()
queue2 = Queue()

total_time = 0

while number_clients < TOTAL_CLIENTS:
    event = listEvents.pop() # pega o minimo da lista (proximo evento)
    if event is None:
        event = get_next_arrival(total_time)
    total_time = event.start_time
    log_event(event)
    if event.type == EVENT_TYPE_ARRIVAL:
        new_client = Client()
        queue1.push(new_client)
        listEvents.insert(get_next_arrival(total_time))

        number_clients += 1 
        if number_clients > TRANSIENT_STAGE:
            analytics.add(new_client)
        if server.is_empty():
            server.push(queue1.pop())
            listEvents.insert(Event(total_time + new_client.get_service_time(), {"client": new_client}, EVENT_TYPE_END_SERVICE_1))
        else:
            if server.service_type == 2:
                client_running = server.pop()
                client_running.update_service_time(total_time) 
                listEvents.insert(Event(total_time + new_client.get_service_time(), {"client": new_client}, EVENT_TYPE_END_SERVICE_1))
    elif event.type == EVENT_TYPE_END_SERVICE_1:
        client = event.data.client
        client.end_service_1 = client.start_queue_2 = total_time
        queue2.push(client)
        
        server.pop()
        if queue1.is_empty():
            if queue2.is_empty():
                pass
            else:
                next_client = queue1.pop()
                server.push(next_client)        
                listEvents.insert(Event(total_time + next_client.get_service_time(), {"client": next_client}, EVENT_TYPE_END_SERVICE_2))
        else:
            next_client = queue1.pop()
            server.push(next_client)
            listEvents.insert(Event(total_time + next_client.get_service_time(), {"client": next_client}, EVENT_TYPE_END_SERVICE_1))
    elif event.type == EVENT_TYPE_END_SERVICE_2:
        client = event.data.client
        client.end_service_2 = total_time 
        server.pop()
        if queue1.is_empty():
            if queue2.is_empty():
                pass
            else:
                next_client = queue1.pop()
                server.push(next_client)        
                listEvents.insert(Event(total_time + next_client.get_service_time(), {"client": next_client}, EVENT_TYPE_END_SERVICE_2))
        else:
            next_client = queue1.pop()
            server.push(next_client)
            listEvents.insert(Event(total_time + next_client.get_service_time(), {"client": next_client}, EVENT_TYPE_END_SERVICE_1))

analytics.run()