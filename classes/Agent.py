import mesa

class Agent(mesa.Agent):
    def __init__(self,
                 model: mesa.Model,
                 n_bystanders: int,
                 seriousness: float,
                 helping_tendency: float = 0.5,
                 confidence: float = 0.5,
                 judgement_fear: float = 0.5,
                 ):
        super().__init__(model)  # this is what they did in the tutorial

        self.n_bystanders = n_bystanders
        self.seriousness = seriousness

        # these are optional and can be used to create variance in the population
        # at 0.5 they should have no effect
        self.helping_tendency = helping_tendency
        self.confidence = confidence
        self.judgement_fear = judgement_fear

        # stuff that gets updated throughout
        self.responsibility_group = None  # if they get assigned responsibility this is where that shows up
        self.n_helpers = 0  # in the beginning there are no helpers yet

    def assign_responsibility(self, responsibility_group):
        self.responsibility_group = responsibility_group

    def perceive_helpers(self, n_helpers):
        self.n_helpers = n_helpers

    def update_feeling_of_responsibility(self):
        pass

    def update_perceived_seriousness(self):
        pass

    def update_cost_of_non_intervention(self):
        pass

    def update_audience_inhibition(self):
        pass

    def get_helping_probability(self):
        pass

