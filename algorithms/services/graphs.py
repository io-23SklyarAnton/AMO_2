import random
from typing import List
import matplotlib.pyplot as plt
from math import log, log2

from .algorithms import merge_sort


def build_execution_time_graph(arrays: List[list]):
    n_list = [len(array) for array in arrays]
    arrays_data = [merge_sort(array) for array in arrays]
    sorted_arrays = [array[0] for array in arrays_data]
    execution_times = [array[1] for array in arrays_data]

    # real graph
    plt.plot(n_list, execution_times, marker='o', linestyle='-')

    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання')
    plt.title('Залежність часу виконання від розміру масиву')
    plt.grid(True)
    plt.savefig(r'algorithms/static/img/real_plot.png')
    plt.close()

    # theory graph
    theory_operations = [n * log(n) for n in n_list]

    plt.plot(n_list, theory_operations, marker='o', linestyle='-')

    plt.xlabel('Розмір масиву')
    plt.ylabel('Кількість операцій')
    plt.title('Залежність кількості операцій від розміру масиву')
    plt.grid(True)
    plt.savefig(r'algorithms/static/img/theory_plot.png')
    plt.close()

    return sorted_arrays
