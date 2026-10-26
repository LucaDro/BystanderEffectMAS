from classes.Environment import Environment
import matplotlib.pyplot as plt

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
    main()