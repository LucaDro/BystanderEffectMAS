from classes.Environment import Environment
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

SERIOUSNESS = 0.1

CALLED_OUT_GROUP = 1
AGENTS = [n for n in range(1, 21) if n >= CALLED_OUT_GROUP]
ITERATIONS = 1000
PATH_FILE = "plots/"

w = 0.4
x = np.arange(len(AGENTS))

def make_bar_plot(total_helpers, called_out_helpers, num_helpers_baseline):
    fig, ax = plt.subplots()
    ax.bar(x-(w/2), num_helpers_baseline, width = w, label="helpers with no one with assigned responsibility")
    ax.bar(x+(w/2), total_helpers, width=w, label="total helpers")
    ax.bar(x+(w/2), called_out_helpers, width=w, label="helpers with assigned responsibility")
    ax.set_xticks(x)
    ax.set_xticklabels(AGENTS)
    ax.set_xlabel("number of bystanders")
    ax.set_ylabel("number of helpers")
    fig.set_figheight(6)
    fig.set_figwidth(10)
    plt.title(f"average number of helpers at seriousness {SERIOUSNESS} over {ITERATIONS} iterations \n when calling out {CALLED_OUT_GROUP} bystanders")
    plt.legend()
    plt.savefig(PATH_FILE+f"helpers_at_seriousness{SERIOUSNESS}_with_{CALLED_OUT_GROUP}_called_out.png")
    plt.show()

def plot():
    called_out_helpers = []
    total_helpers = []
    total_no_helpers = []
    for i in range(len(AGENTS)):
        called_out_helpers.append(0)
        total_helpers.append(0)
        total_no_helpers.append(0)
    for idx, agent in enumerate(AGENTS):
        for i in range(ITERATIONS):
            env = Environment(n=agent, seriousness=SERIOUSNESS, width=10, height=10, agents_helping=0)
            env.run_for(10)
            total_no_helpers[idx] += env.get_total_helpers()
        for i in range(ITERATIONS):
            env = Environment(n=agent, seriousness=SERIOUSNESS, width=10, height=10, agents_helping=CALLED_OUT_GROUP)
            env.run_for(10)
            called_out_helpers[idx] += env.get_total_called_out_helpers()
            total_helpers[idx] += env.get_total_helpers()
        called_out_helpers[idx] /= ITERATIONS
        total_helpers[idx] /= ITERATIONS
        total_no_helpers[idx] /= ITERATIONS
        print("done")
    print(total_helpers)
    make_bar_plot(total_helpers, called_out_helpers, total_no_helpers)


if __name__ == "__main__":
    plot()