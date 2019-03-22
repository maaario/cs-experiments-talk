import os

import matplotlib.pyplot as plt


def plot_comparison(outputs_dir):
    averages = []
    labels = []

    for subdir in sorted(os.listdir(outputs_dir)):
        file_path = os.path.join(outputs_dir, subdir, "average.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                averages.append(float(f.read().strip()))
                labels.append(subdir)

    fig, ax = plt.subplots()
    x = list(range(len(averages)))
    ax.scatter(x, averages)
    plt.yscale("log")
    for i, label in enumerate(labels):
        ax.annotate(label, (x[i], averages[i]))

    plt.savefig(os.path.join(outputs_dir, "comparison,png"))
