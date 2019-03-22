from random import randint, shuffle

N = 1000
MAX = 1000

task_input = [randint(0, MAX) for _ in range(N)]


def sol_random(numbers):
    total = sum(numbers)

    selected = sum([x for x in numbers if randint(0, 1) == 1])

    not_selected = total - selected
    return abs(selected - not_selected)


def sol_random_half(numbers):
    total = sum(numbers)

    half = len(numbers) // 2
    shuffle(numbers)
    selected = sum(numbers[:half])

    not_selected = total - selected
    return abs(selected - not_selected)


if __name__ == "__main__":
    print(sol_random(task_input))
    print(sol_random_half(task_input))
