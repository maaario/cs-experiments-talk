import argparse
import os
import random

from methods import all_methods


def prepare_argparser():
    argparser = argparse.ArgumentParser(description='Argparser for subset sum.')

    # IO paths
    argparser.add_argument('-data', default='data/input_data.txt', help='Input data file.')
    argparser.add_argument('-output', default='output', help='Name of the output folder.')

    # General options
    argparser.add_argument('-seed', default=0, type=int, help='Random seed.')
    argparser.add_argument('-repeat', default=100, type=int, help='Number of the method calls.')

    # Methods and parameters
    argparser.add_argument('-method', default='sol_random', help='Name of solver method.',
                           choices=all_methods.keys())
    argparser.add_argument('-num_repeats', default=10, type=int,
                           help='Parameter of "repeat_random_half" method.')

    return argparser


def read_input(path):
    with open(path, "r") as f:
        input_data = [int(x) for x in f.read().split()]
    return input_data


def evaluate(method, params, repeat, task_input, output_dir):
    answers = []
    for _ in range(repeat):
        answers.append(method(task_input, **params))

    with open(os.path.join(output_dir, "answers.txt"), "w") as answers_file:
        answers_file.write("\n".join(map(str, answers)))

    average = sum(answers) / repeat

    with open(os.path.join(output_dir, "average.txt"), "w") as answers_file:
        answers_file.write("{}\n".format(average))
    print(method.__name__, average)


def run_experiment(args):
    # Prepare params.
    if args.method == "sol_repeat_random_half":
        params = {"num_repeats": args.num_repeats}
    else:
        params = dict()

    # Load inputs.
    input_data = read_input(args.data)

    # Prepare output paths.
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Run evaluate.
    random.seed(args.seed)
    evaluate(
        method=all_methods[args.method],
        params=params,
        repeat=args.repeat,
        task_input=input_data,
        output_dir=args.output,
    )


if __name__ == "__main__":
    argparser = prepare_argparser()
    args = argparser.parse_args()
    run_experiment(args)
