from classes.Environment import Environment

def main():
    percentage_1_helper = 0
    iterations = 10000
    agent_nr = 1
    seriousness = 0.8

    for i in range(iterations):
        env = Environment(n=agent_nr, seriousness=seriousness, width=10, height=10, )
        env.run_for(2)
        #env.extract_data()
        help = env.someone_helped()
        percentage_1_helper += help/iterations

    print("Percentage of Helpers:", percentage_1_helper)
    

if __name__ == "__main__":
    main()