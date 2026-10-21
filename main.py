from classes.Environment import Environment

def main():
    agent_nr = 1
    env = Environment(n=agent_nr, width=10, height=10)
    env.run_for(5)
    env.extract_data()
    

if __name__ == "__main__":
    main()