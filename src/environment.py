import mesa
from src.agent import PartyAgents

class PartyEnvironment(mesa.Model):
    
    def __init__(self, n, seed):
        super().__init__(rng=seed)
        self.num_agents = n
        
        PartyAgents.create_agents(model=self, n=self.num_agents)