import random


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


def sol_repeat_random_half(numbers, num_repeats):
    min_answer = sum(numbers)

    for _ in range(num_repeats):
        min_answer = min(min_answer, sol_random_half(numbers))

    return min_answer


def sol_sort_greedy(numbers):
    total = sum(numbers)

    sorted_numbers = sorted(numbers)

    min_answer = total
    selected = 0
    not_selected = total
    for number in sorted_numbers:
        selected += number
        not_selected -= number
        answer = abs(selected - not_selected)
        min_answer = min(min_answer, answer)

    return min_answer


all_methods = [
    sol_random,
    sol_random_half,
    sol_repeat_random_half,
    sol_sort_greedy,
]
