import matplotlib.pyplot as plt
import tsp_ga as ga
import pandas as pd
from random import sample
from mpl_toolkits.basemap import Basemap


def get_genes_from(fn, sample_n=0):
    df = pd.read_csv(fn)
    genes = [ga.Gene(row['city'], row['latitude'], row['longitude'])
             for _, row in df.iterrows()]

    return genes if sample_n <= 0 else sample(genes, sample_n)


def plot(costs, individual, save_to=None):
    plt.figure(1)
    plt.subplot(121)
    plot_ga_convergence(costs)

    plt.subplot(122)
    plot_route(individual)

    if save_to is not None:
        plt.savefig(save_to)
        plt.close()
    else:
        plt.show()

def plot_ga_convergence(costs):
    x = range(len(costs))
    plt.title("Convergencia GA")
    plt.xlabel('# Generación')
    plt.ylabel('costo en  (KM)')
    plt.text(x[len(x) // 2], costs[0], 'costo minimo: {} KM'.format(costs[-1]), ha='center', va='center')
    plt.plot(x, costs, '-')


def plot_route(individual):
    plt.axis('off')
    plt.title("Ruta mas corta")
    
    for i in range(0, len(individual.genes)):
        x, y = individual.genes[i].lng, individual.genes[i].lat
        plt.plot(x, y, 'ok',  markersize=5)
        if i == len(individual.genes) - 1:
            x2, y2 = individual.genes[0].lng, individual.genes[0].lat
        else:
            x2, y2 = individual.genes[i+1].lng, individual.genes[i+1].lat

        plt.plot([x, x2], [y, y2], c='g')

        
    for i in range(0, len(individual.genes)):
        xx, yy = individual.genes[i].lng, individual.genes[i].lat
        ciudad = individual.genes[i].name
        plt.text(xx, yy, ciudad, fontsize=8)