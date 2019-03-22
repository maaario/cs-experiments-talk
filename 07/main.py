import os

from run_experiment import prepare_argparser, run_experiment
from visualize import plot_comparison


if __name__ == "__main__":
    # Default settings.
    argparser = prepare_argparser()
    args = argparser.parse_args()

    # Override setting to make only 10 repeat runs.
    args.repeat = 10
    output_dir = args.output

    # Method name, num_repeats, output_folder.
    settings = [
        ["sol_random",              0,     "random"],
        ["sol_random_half",         0,     "random_half"],
        ["sol_repeat_random_half",  10,    "repeat_random_half_10"],
        ["sol_repeat_random_half",  100,   "repeat_random_half_100"],
        ["sol_repeat_random_half",  1000,  "repeat_random_half_1000"],
        ["sol_repeat_random_half",  10000, "repeat_random_half_10000"],
        ["sol_sort_greedy",         0,     "sort_greedy"],
    ]

    # Run multiple experiments.
    for setting in settings:
        args.method = setting[0]
        args.num_repeats = setting[1]

        output_path = os.path.join(output_dir, setting[2])
        if os.path.exists(output_path):
            print("Don't run experiment {}, because experiment folder already exists.".format(
                output_path))
        else:
            args.output = output_path
            run_experiment(args)

    # Visualize.
    plot_comparison(output_dir)
