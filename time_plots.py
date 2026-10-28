from classes.Environment import Environment
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

SERIOUSNESS = 0.4
AGENTS = 3
CALLED_OUT_GROUP = 1
ITERATIONS = 100
TIMESTEPS = 10
PATH_FILE = "time_plots/"


def make_history_plot(total_helpers, called_out_helpers, baseline_helpers):
    fig, ax = plt.subplots()
    ax.plot(total_helpers, label="total helpers")
    ax.plot(called_out_helpers, label="helpers with assigned responsibilty")
    ax.plot(baseline_helpers, label="total helpers with no one assigned responsibility")
    ax.set_ylabel("average number of helpers")
    ax.set_xlabel("timestep")
    fig.set_figwidth(10)
    fig.set_figheight(6)
    plt.title(f"average number of helpers by timestep over {ITERATIONS} iterations \n with {AGENTS} bystanders when assigning responsibility to {CALLED_OUT_GROUP} bystanders")
    plt.legend()
    plt.show()

def plot():
    called_out_helpers = []
    total_helpers = []
    total_no_helpers = []
    for i in range(TIMESTEPS):
        called_out_helpers.append(0)
        total_helpers.append(0)
        total_no_helpers.append(0)
    for i in range(ITERATIONS):
        env = Environment(n=AGENTS, seriousness=SERIOUSNESS, width=10, height=10, agents_helping=0)
        env.run_for(TIMESTEPS)
        datacollector = env.datacollector.get_model_vars_dataframe()
        helpers = datacollector["num helpers"]
        for idx in range(len(helpers)):
            total_no_helpers[idx] += helpers[idx]
    for i in range(ITERATIONS):
        env = Environment(n=AGENTS, seriousness=SERIOUSNESS, width=10, height=10, agents_helping=CALLED_OUT_GROUP)
        env.run_for(TIMESTEPS)
        datacollector = env.datacollector.get_model_vars_dataframe()
        helpers = datacollector["num helpers"]
        called_out_helpers_one = datacollector["called_out_helpers"]
        for idx in range(len(helpers)):
            total_helpers[idx] += helpers[idx]
            called_out_helpers[idx] += called_out_helpers_one[idx]
    for idx in range(len(called_out_helpers)):
        called_out_helpers[idx] /= ITERATIONS
        total_helpers[idx] /= ITERATIONS
        total_no_helpers[idx] /= ITERATIONS
    print("done")
    print(total_helpers)
    
    make_history_plot(total_helpers, called_out_helpers, total_no_helpers)  


if __name__ == "__main__":
    plot()