import random

import numpy as np
from sacred import Experiment
from sacred.observers import FileStorageObserver
from tqdm import tqdm

from methods import all_methods

SACRED_DIR = "sacred"
experiment = Experiment()
experiment.observers.append(FileStorageObserver.create(SACRED_DIR))


@experiment.config
def config():
    data_path = 'data/input_data.txt'

    repeat = 100

    method = 'sol_random'
    params = dict()


def read_input(path):
    with open(path, "r") as f:
        input_data = [int(x) for x in f.read().split()]
    return input_data


def evaluate(method, params, repeat, task_input, _run):
    answers = []
    for _ in tqdm(range(repeat)):
        answer = method(task_input, **params)
        answers.append(answer)
        _run.log_scalar("answer", answer)

    average = np.mean(answers)
    _run.log_scalar("average", average)
    print(method.__name__, np.min(answers), average, np.std(answers))


@experiment.automain
def run_experiment(data_path, repeat, method, params, _seed, _run):
    input_data = read_input(data_path)
    random.seed(_seed)
    evaluate(
        method=all_methods[method],
        params=params,
        repeat=repeat,
        task_input=input_data,
        _run=_run,
    )
