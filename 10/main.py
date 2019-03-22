import copy
import os

from run_experiment import experiment, SACRED_DIR


if __name__ == "__main__":
    global_settings = dict(
        repeat=10,
        data_path="data/input_data_M2.txt",
    )

    settings = [
        dict(method="sol_random"),

        dict(method="sol_random_half"),

        dict(method="sol_repeat_random_half", params=dict(num_repeats=10)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=100)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=1000)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=10000)),

        dict(method="sol_repeat_random", params=dict(num_repeats=1000)),
        dict(method="sol_repeat_random", params=dict(num_repeats=10000)),

        dict(method="sol_sort_greedy"),

        dict(method="sol_genetic", params=dict(
            pop_size=10, max_epochs=50, random_born=0.2, survive=0.2)),
        dict(method="sol_genetic", params=dict(
            pop_size=100, max_epochs=50, random_born=0.2, survive=0.2)),
    ]

    for setting in settings:
        config = copy.deepcopy(global_settings)
        config.update(setting)
        experiment.run(config_updates=config)
