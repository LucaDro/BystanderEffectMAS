from classes.Environment import Environment
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

SERIOUSNESS = 0.4
AGENTS = [1,2,3,4,5,6,7,8]
CALLED_OUT_GROUP = 1
ITERATIONS = 1000
PATH_FILE = "plots/"
NO_CALLED_OUT = [0.7878, 0.3975, 0.0445, 0.0, 0.0, 0.0, 0.0, 0.0]

w = 0.3
x = np.arange(len(AGENTS))

def make_bar_plot(total_helpers, called_out_helpers):
    fig, ax = plt.subplots()
    ax.bar(x-w, NO_CALLED_OUT, width = w, label="helpers with no one called out")
    ax.bar(x, total_helpers, width=w, label="total helpers")
    ax.bar(x+w, called_out_helpers, width=w, label="called out helpers")
    ax.set_xticks(x)
    ax.set_xticklabels(AGENTS)
    ax.set_xlabel("number of bystanders")
    ax.set_ylabel("number of helpers")
    plt.title(f"average number of helpers at seriousness {SERIOUSNESS} over {ITERATIONS} iterations when calling out {CALLED_OUT_GROUP} bystanders")
    plt.legend()
    plt.savefig(PATH_FILE+f"helpers_at_seriousness{SERIOUSNESS}_with_{CALLED_OUT_GROUP}_called_out.png")
    plt.show()

def plot():
    called_out_helpers = []
    total_helpers = []
    for i in range(len(AGENTS)):
        called_out_helpers.append(0)
        total_helpers.append(0)
    for idx, agent in enumerate(AGENTS):
        for i in range(ITERATIONS):
            env = Environment(n=agent, seriousness=SERIOUSNESS, width=10, height=10, agents_helping=CALLED_OUT_GROUP)
            env.run_for(10)
            called_out_helpers[idx] += env.get_total_called_out_helpers()
            total_helpers[idx] += env.get_total_helpers()
        called_out_helpers[idx] /= ITERATIONS
        total_helpers[idx] /= ITERATIONS
        print("done")
    print(total_helpers)
    make_bar_plot(total_helpers, called_out_helpers)


if __name__ == "__main__":
    plot()