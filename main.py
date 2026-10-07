from src.environment import PartyEnvironment

def main():
    agent_nr = 33
    env = PartyEnvironment(agent_nr)    
    env.step()
    

if __name__ == "__main__":
    main()