from classes.Environment import Environment
import matplotlib.pyplot as plt
import pandas as pd


def read_baseline():
    bl = pd.read_csv("baseline.csv")
    s = 0.8
    bl = bl[bl["seriousness"]==s]
    bl_agg = bl.groupby('n_bystanders')['probability_help'].mean().reset_index()

    for n in bl["n_bystanders"].unique():
        value_count = len(bl[bl["n_bystanders"]==n]["probability_help"])
        print(f"{n}: {value_count}")

    x = bl["n_bystanders"]
    y = bl["probability_help"]
    x_agg = bl_agg["n_bystanders"]
    y_agg = bl_agg["probability_help"]

    fig, ax = plt.subplots()
    ax.plot(x, y, 'x', markeredgewidth=2)
    ax.plot(x_agg, y_agg, linewidth=2.0)
    ax.set(ylim=(0, 1.1))

    plt.show()

def main():
    percentage_helper = [0,0,0,0,0]
    agent_nr_list = [1,2,3,4,5]
    for idx, agent in enumerate(agent_nr_list):
        iterations = 10000
        agent_nr = agent
        seriousness = 0.8

        for i in range(iterations):
            env = Environment(n=agent_nr, seriousness=seriousness, width=10, height=10, )
            env.run_for(2)
            #env.extract_data()
            help = env.someone_helped()
            percentage_helper[idx] += help
        percentage_helper[idx] /= iterations
        print("Percentage of Helpers:", percentage_helper)
    plt.plot(agent_nr_list, percentage_helper)
    plt.axis((agent_nr_list[0]-1, agent_nr_list[-1]+1, 0,1))
    plt.show()

if __name__ == "__main__":
    #main()
    read_baseline()