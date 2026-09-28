import mesa

class PartyAgents(mesa.Agent):
    
    def __init__(self, model):
        super().__init__(model)
        
    def decision(self):
        print(self.unique_id)