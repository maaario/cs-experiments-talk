import matplotlib.pyplot as plt

with open("sol_random.txt", "r") as answers_file:
    sol_random = [int(x) for x in answers_file.read().split("\n")]

with open("sol_random_half.txt", "r") as answers_file:
    sol_random_half = [int(x) for x in answers_file.read().split("\n")]

plt.figure()
plt.hist(sol_random, label="random")
plt.hist(sol_random_half, label="random_half")
plt.legend()
plt.savefig("histogram.png")
