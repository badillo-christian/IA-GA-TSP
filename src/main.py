import utils
import random
import argparse
import tsp_ga as ga
from datetime import datetime


def run(args):
    genes = utils.get_genes_from(args.cities_fn)

    if args.verbose:
        print("TSP-GA con {} ciudades".format(len(genes)))

    history = ga.run_ga(genes, args.pop_size, args.n_gen,
                        args.tourn_size, args.mut_rate, args.verbose)

    utils.plot(history['cost'], history['route'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', type=int, default=1)
    parser.add_argument('--pop_size', type=int, default=200, help='Tamaño de población')
    parser.add_argument('--tourn_size', type=int, default=20, help='Tamaño del torneo')
    parser.add_argument('--mut_rate', type=float, default=0.01, help='Rate de mutación ')
    parser.add_argument('--n_gen', type=int, default=500, help='Numero de generaciones')
    parser.add_argument('--cities_fn', type=str, default="../data/ciudades.csv", help='Archivo con las ciudades')

    random.seed(datetime.now().timestamp())
    args = parser.parse_args()

    if args.tourn_size > args.pop_size:
        raise argparse.ArgumentTypeError('El tamaño del torneo no puede ser mas grande que el tamaño de la población.')

    run(args)