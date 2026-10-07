from classes.Environment import Environment

def main():
    agent_nr = 33
    env = Environment(n=agent_nr, width=10, height=10)
    env.step()
    

if __name__ == "__main__":
    main()