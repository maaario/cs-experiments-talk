import matplotlib.pyplot as plt

from methods import all_methods

# Read results
results = dict()
for method_name, method in all_methods.items():
    with open(method_name + ".txt", "r") as answers_file:
        results[method_name] = [int(x) for x in answers_file.read().split("\n")]

# Plot
plt.figure()
for method in all_methods:
    method_name = method.__name__
    plt.hist(results[method_name], label=method_name)

# plt.xscale("log")
plt.legend()
plt.savefig("histogram.png")
