import random

SEED = 7
N = 1000
MAX = 1000
REPEAT = 10


def sol_random(numbers):
    total = sum(numbers)

    selected = sum([x for x in numbers if random.randint(0, 1) == 1])

    not_selected = total - selected
    return abs(selected - not_selected)


def sol_random_half(numbers):
    total = sum(numbers)

    half = len(numbers) // 2
    random.shuffle(numbers)
    selected = sum(numbers[:half])

    not_selected = total - selected
    return abs(selected - not_selected)


def evaluate(method, task_input):
    answers = []
    for _ in range(REPEAT):
        answers.append(method(task_input))
    print(method.__name__, sum(answers) / REPEAT)


if __name__ == "__main__":
    random.seed(SEED)
    task_input = [random.randint(0, MAX) for _ in range(N)]
    evaluate(sol_random, task_input)
    evaluate(sol_random_half, task_input)
