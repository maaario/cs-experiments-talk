import os
import random

N = 100
MAX = 100000
SEED = 7
DATA_PATH = "data/input_data_M2.txt"

if __name__ == "__main__":
    random.seed(SEED)

    task_input = [random.randint(0, MAX) ** 2 for _ in range(N)]

    data_dir = os.path.dirname(DATA_PATH)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with open(DATA_PATH, "w") as f:
        f.write(" ".join(map(str, task_input)))
