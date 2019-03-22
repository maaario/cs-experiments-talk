import random

from methods import *

SEED = 7
N = 1000
MAX = 1000
REPEAT = 100


def evaluate(method, task_input, params=dict()):
    answers = []
    for _ in range(REPEAT):
        answers.append(method(task_input, **params))

    with open(method.__name__ + ".txt", "w") as answers_file:
        answers_file.write("\n".join(map(str, answers)))

    print(method.__name__, sum(answers) / REPEAT)
    # print(method.__name__, sum(answers) / REPEAT, min(answers))


if __name__ == "__main__":
    random.seed(SEED)
    task_input = [random.randint(0, MAX) for _ in range(N)]
    evaluate(sol_random, task_input)
    evaluate(sol_random_half, task_input)
    evaluate(sol_repeat_random_half, task_input, {"num_repeats": 10})
    evaluate(sol_sort_greedy, task_input)
