import jsonpickle
import os

import matplotlib.pyplot as plt


def load_experiment_results(exp_dir):
    with open(os.path.join(exp_dir, "config.json"), "r") as config_file:
        config = jsonpickle.decode(config_file.read())

    with open(os.path.join(exp_dir, "metrics.json"), "r") as metrics_file:
        metrics = jsonpickle.decode(metrics_file.read())
        average = metrics["average"]["values"][0]

    return config, average


def plot_comparison(sacred_dir, output_path):
    averages = []
    labels = []

    for exp_dir in sorted(os.listdir(sacred_dir)):
        if exp_dir.startswith("_"):
            continue
        config, average = load_experiment_results(os.path.join(sacred_dir, exp_dir))
        label = "{}_{}".format(config["method"], config["params"].get("num_repeats", ""))
        averages.append(average)
        labels.append(label)

    fig, ax = plt.subplots()
    x = list(range(len(averages)))
    ax.scatter(x, averages)
    plt.yscale("log")
    for i, label in enumerate(labels):
        ax.annotate(label, (x[i], averages[i]))
    plt.savefig(output_path)
