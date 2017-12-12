import matplotlib.pyplot as plt
import numpy as np

metrics_name = ["E[Nq1]", "E[Nq2]", "E[N1]", "E[N2]", "E[T1]", "E[W1]", "E[T2]", "E[W2]", "V[W1]", "V[W2]"]
for metric in metrics_name:
    fig, ax = plt.subplots()
    ax.set_title("Metric: {}".format(metric))    
    ax.set_xlabel('Clients')
    ax.set_ylabel('{}'.format(metric))
    for index in range(5):
        with open("testes/fase_transiente/metrics-{}-{}.txt".format(metric, index)) as o_file:
            lines = o_file.readlines()
            y = [line for line in lines]
            x = np.linspace(0, 100000, 100001)
            ax.plot(x, y, label='Amostra: {}'.format(index))
    leg = ax.legend()
    plt.show()
