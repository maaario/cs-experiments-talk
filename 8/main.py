import copy
import os

from run_experiment import experiment, SACRED_DIR
from visualize import plot_comparison


if __name__ == "__main__":
    global_settings = dict(
        repeat=10,
    )

    settings = [
        dict(method="sol_random"),
        dict(method="sol_random_half"),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=10)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=100)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=1000)),
        dict(method="sol_repeat_random_half", params=dict(num_repeats=10000)),
        dict(method="sol_sort_greedy"),
    ]

    for setting in settings:
        config = copy.deepcopy(global_settings)
        config.update(setting)
        experiment.run(config_updates=config)

    plot_comparison(SACRED_DIR, "comparison.png")
