import random

import numpy as np


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


def sol_repeat_random(numbers, num_repeats):
    min_answer = sum(numbers)

    for _ in range(num_repeats):
        min_answer = min(min_answer, sol_random(numbers))

    return min_answer


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


def sol_genetic(numbers, pop_size=100, max_epochs=50, random_born=0.2, survive=0.2):
    n = len(numbers)
    numbers = np.array(numbers)
    total = numbers.sum()

    def score(solution):
        selected = numbers[solution == 1].sum()
        not_selected = total - selected
        return abs(selected - not_selected)

    def score_from_sum(selected):
        not_selected = total - selected
        return abs(selected - not_selected)

    def mutate_random_flips(solution, fraction=0.1):
        mask = np.random.rand(n) < fraction
        return (solution + mask) % 2

    def mutate_if_better(solution, index, cur_sum):
        if solution[index] == 0:
            if score_from_sum(cur_sum + numbers[index]) < score_from_sum(cur_sum):
                solution[index] = 1
                return numbers[index]
        else:
            if score_from_sum(cur_sum - numbers[index]) < score_from_sum(cur_sum):
                solution[index] = 0
                return -numbers[index]
        return 0

    def mutate_all_if_better(solution, shuffle=True):
        new_solution = np.copy(solution)
        cur_sum = numbers[solution == 1].sum()
        order = np.arange(n)
        if shuffle:
            np.random.shuffle(order)

        for i in order:
            cur_sum += mutate_if_better(new_solution, i, cur_sum)

        return new_solution

    def mutate_greedy_small(solution):
        fraction = np.random.rand()

        to_greedy = numbers.argsort()[:int(fraction * n)]
        new_solution = np.copy(solution)
        new_solution[to_greedy] = 2
        cur_sum = numbers[new_solution == 1].sum()
        other_sum = numbers[new_solution == 0].sum()

        for index in to_greedy[::-1]:
            if cur_sum < other_sum:
                cur_sum += numbers[index]
                new_solution[index] = 1
            else:
                other_sum += numbers[index]
                new_solution[index] = 0

        return new_solution

    mutations = [mutate_random_flips, mutate_all_if_better, mutate_greedy_small]

    def mutate(solution):
        m = mutations[np.random.randint(len(mutations))]
        return m(solution)

    def crossover(s1, s2):
        new_solution = np.random.randint(0, 2, n)
        equals = s1 == s2
        new_solution[equals] = s1[equals]
        return new_solution

    population = np.random.randint(0, 2, size=(pop_size, n))
    num_random_born = int(random_born * pop_size)
    num_survive = int(survive * pop_size)
    num_mutants = pop_size - num_random_born - num_survive

    for epoch in range(max_epochs):
        fitness = np.apply_along_axis(score, 1, population)
        order = np.argsort(fitness)

        to_mutate = np.random.randint(0, pop_size, num_mutants)
        mutants = np.apply_along_axis(mutate, 1, population[to_mutate, :])
        for i, j in np.random.randint(0, num_mutants, size=(num_mutants // 2, 2)):
            mutants[i, :] = crossover(mutants[i, :], mutants[j, :])
        survivors = population[order[:num_survive], :]
        newborns = np.random.randint(0, 2, size=(num_random_born, n))

        population = np.vstack((mutants, survivors, newborns))

    return np.apply_along_axis(score, 1, population).min()


all_methods = {
    "sol_random": sol_random,
    "sol_random_half": sol_random_half,
    "sol_repeat_random": sol_repeat_random,
    "sol_repeat_random_half": sol_repeat_random_half,
    "sol_sort_greedy": sol_sort_greedy,
    "sol_genetic": sol_genetic,
}
