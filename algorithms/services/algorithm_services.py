import random
from typing import List

from django.forms import Form
import re
from algorithms.services.algorithms import merge_sort
from algorithms.services.file_handlers import get_string_from_file, get_num_from_file
from algorithms.services.graphs import build_execution_time_graph


def generate_lists_and_sort(form: Form) -> List[list]:
    data = form.cleaned_data
    n_lists = data['lists_num']
    if data.get('file'):
        n_lists = get_num_from_file(data.get('file'))
    lists = [[random.randint(-1000, 1000) for _ in range(10 * n ** 2)] for n in range(1, n_lists * 2, 2)]
    sorted_arrays = build_execution_time_graph(lists)
    return sorted_arrays


def get_sort_list_and_time(form: Form) -> List[list]:
    data = form.cleaned_data
    string = data['elements']
    if data.get('file'):
        string = get_string_from_file(data.get('file'))
    cleaned_string = re.findall('\d+', string)
    array = list(map(int, cleaned_string))

    return merge_sort(array)
