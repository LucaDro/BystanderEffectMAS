from classes.Environment import Environment
import matplotlib.pyplot as plt
import pandas as pd


def read_baseline(s):
    bl = pd.read_csv("baseline.csv")
    bl = bl[bl["seriousness"]==s]
    bl_agg = bl.groupby('n_bystanders')['probability_help'].mean().reset_index()

    x = bl["n_bystanders"]
    y = bl["probability_help"]
    x_agg = bl_agg["n_bystanders"]
    y_agg = bl_agg["probability_help"]

    return x, y, x_agg, y_agg


def plot_stuff(s, agent_nr_list, percentage_helper, with_helper = None):
    bx, by, bx_agg, by_agg = read_baseline(s)
    fig, ax = plt.subplots()
    ax.plot(bx, by, 'x', markeredgewidth=2)
    ax.plot(bx_agg, by_agg, linewidth=2.0, label="baseline")
    ax.plot(agent_nr_list, percentage_helper, label="model")
    if with_helper is not None:
        ax.plot(agent_nr_list, with_helper)
    ax.set_xlabel("number of bystanders")
    ax.set_ylabel(f"probability at seriousness {s}")
    ax.set(ylim=(0, 1.1))
    plt.legend()
    plt.axis((agent_nr_list[0]-1, agent_nr_list[-1]+1, 0,1))
    plt.show()


def main():
    seriousness_list = [0.3, 0.4, 0.6, 0.8, 0.9]
    for seriousness in seriousness_list:
        percentage_helper = [0,0,0,0,0]
        percentage_helper_with_help = [0,0,0,0,0]
        agent_nr_list = [1,2,3,4,5]
        for idx, agent in enumerate(agent_nr_list):
            iterations = 1
            agent_nr = agent

            for i in range(iterations):
                env = Environment(n=agent_nr, seriousness=seriousness, width=10, height=10, agents_helping=1)
                # env.call_for_help(1)
                env.run_for(5)
                #env.extract_data()
                help = env.someone_helped()
                percentage_helper[idx] += help
            percentage_helper[idx] /= iterations
            print("Percentage of Helpers:", percentage_helper)
            # for i in range(iterations):
            #     env = Environment(n=agent_nr+1, seriousness=seriousness, width=10, height=10, )
            #     # env.call_for_help(1)
            #     env.run_for(5)
            #     #env.extract_data()
            #     help = env.someone_helped(1)
            #     percentage_helper_with_help[idx] += help
            # percentage_helper_with_help[idx] /= iterations
            # print("Percentage of Helpers with help:", percentage_helper_with_help)

        plot_stuff(seriousness, agent_nr_list, percentage_helper, percentage_helper_with_help)

def main_with_helper():
    seriousness_list = [0.3, 0.4, 0.6, 0.8, 0.9]
    for seriousness in seriousness_list[-2:]:
        percentage_helper = [0,0,0,0,0]
        agent_nr_list = [1,2,3,4,5]
        for idx, agent in enumerate(agent_nr_list):
            iterations = 1000
            agent_nr = agent

            for i in range(iterations):
                env = Environment(n=agent_nr+1, seriousness=seriousness, width=10, height=10, )
                # env.call_for_help(1)
                env.run_for(5)
                #env.extract_data()
                help = env.someone_helped(1)
                percentage_helper[idx] += help
            percentage_helper[idx] /= iterations
            print("Percentage of Helpers:", percentage_helper)
        plot_stuff(seriousness, agent_nr_list, percentage_helper)

if __name__ == "__main__":
    main()