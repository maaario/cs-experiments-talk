import os
import random

N = 1000
MAX = 1000
SEED = 7
DATA_PATH = "data/input_data.txt"

if __name__ == "__main__":
    random.seed(SEED)

    task_input = [random.randint(0, MAX) for _ in range(N)]

    data_dir = os.path.dirname(DATA_PATH)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with open(DATA_PATH, "w") as f:
        f.write(" ".join(map(str, task_input)))
