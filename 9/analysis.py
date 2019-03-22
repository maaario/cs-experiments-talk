import jsonpickle
import os

import matplotlib.pyplot as plt
import pandas as pd


def load_experiment_results(exp_dir):
    with open(os.path.join(exp_dir, "config.json"), "r") as config_file:
        config = jsonpickle.decode(config_file.read())

    with open(os.path.join(exp_dir, "run.json"), "r") as run_file:
        run = jsonpickle.decode(run_file.read())

    with open(os.path.join(exp_dir, "metrics.json"), "r") as metrics_file:
        metrics = jsonpickle.decode(metrics_file.read())

    return config, run, metrics


def process_exp_results_to_df(exp_results):
    records = []

    for config, run, metrics in exp_results:
        record = dict(
            status = run.get("status", ""),
            method = config["method"],
            repeat = config["repeat"],
            average = metrics["average"]["values"][0],
            min = min(metrics["answer"]["values"]),
        )
        record.update(config["params"])
        records.append(record)

    return pd.DataFrame.from_records(records)
