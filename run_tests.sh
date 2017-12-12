#!/bin/sh

# teste com lambda 0.1
# time python main.py -l 0.1 -m 1 -c 100000 -t 10000 -r 50 > ./testes/exponenciais/clientes100000-transiente10000-rounds50-lambda01.txt
# time python main.py -l 0.1 -m 1 -c 10000 -t 1000 -r 3100 > ./testes/exponenciais/clientes10000-transiente1000-rounds3100-lambda01.txt
time python main.py -l 0.1 -m 1 -c 200 -t 50 -r 3100 > ./testes/exponenciais/clientes200-transiente50-rounds3100-lambda01.txt

# teste com lambda 0.2
# time python main.py -l 0.2 -m 1 -c 100000 -t 10000 -r 50 > ./testes/exponenciais/clientes100000-transiente10000-rounds50-lambda02.txt
# time python main.py -l 0.2 -m 1 -c 10000 -t 1000 -r 3100 > ./testes/exponenciais/clientes10000-transiente1000-rounds3100-lambda02.txt
time python main.py -l 0.2 -m 1 -c 200 -t 50 -r 3100 > ./testes/exponenciais/clientes200-transiente50-rounds3100-lambda02.txt


# teste com lambda 0.3
# time python main.py -l 0.3 -m 1 -c 100000 -t 10000 -r 50 > ./testes/exponenciais/clientes100000-transiente10000-rounds50-lambda03.txt
# time python main.py -l 0.3 -m 1 -c 10000 -t 1000 -r 3100 > ./testes/exponenciais/clientes10000-transiente1000-rounds3100-lambda03.txt
time python main.py -l 0.3 -m 1 -c 200 -t 50 -r 3100 > ./testes/exponenciais/clientes200-transiente50-rounds3100-lambda03.txt

# teste com lambda 0.4
# time python main.py -l 0.4 -m 1 -c 100000 -t 10000 -r 50 > ./testes/exponenciais/clientes100000-transiente10000-rounds50-lambda04.txt
# time python main.py -l 0.4 -m 1 -c 10000 -t 1000 -r 3100 > ./testes/exponenciais/clientes10000-transiente1000-rounds3100-lambda04.txt
time python main.py -l 0.4 -m 1 -c 200 -t 50 -r 3100 > ./testes/exponenciais/clientes200-transiente50-rounds3100-lambda04.txt

# teste com lambda 0.45
# time python main.py -l 0.45 -m 1 -c 100000 -t 10000 -r 50 > ./testes/exponenciais/clientes100000-transiente10000-rounds50-lambda045.txt
# time python main.py -l 0.45 -m 1 -c 10000 -t 1000 -r 3100 > ./testes/exponenciais/clientes10000-transiente1000-rounds3100-lambda045.txt
time python main.py -l 0.45 -m 1 -c 200 -t 50 -r 3100 > ./testes/exponenciais/clientes200-transiente50-rounds3100-lambda045.txt