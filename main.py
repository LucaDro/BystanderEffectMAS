from classes.Environment import Environment

def main():
    agent_nr = 3
    env = Environment(n=agent_nr, width=10, height=10)
    env.run_for(100)
    env.extract_data()
    

if __name__ == "__main__":
    main()