import mesa

class PartyAgents(mesa.Agent):
    def __init__(self,
                 model: mesa.Model,
                 n_bystanders: int,
                 seriousness: float,
                 helping_tendency: float = 0.5,
                 confidence: float = 0.5,
                 judgement_fear: float = 0.5,
                 helping_threshold: float = 0.75,
                 ):
        super().__init__(model)  # this is what they did in the tutorial

        self.n_bystanders = n_bystanders
        self.seriousness = seriousness

        # these are optional and can be used to create variance in the population
        # at 0.5 they should have no effect
        self.helping_tendency = helping_tendency
        self.confidence = confidence
        self.judgement_fear = judgement_fear

        # this is a threshold we can set to determine at which probability an agent is helping
        self.helping_threshold = helping_threshold

        # stuff that gets updated throughout
        self.n_responsibility_group = n_bystanders  # if they get assigned responsibility this is where that shows up
        self.n_helpers = 0  # in the beginning there are no helpers yet

        self.is_helping = False
        self.helping_probability = None

    def assign_responsibility(self, responsibility_group):
        self.n_responsibility_group = responsibility_group

    def perceive_helpers(self, n_helpers):
        self.n_helpers = n_helpers

    def get_helping_probability(self):
        self.__update_helping_probability()
        return self.helping_probability

    def get_is_helping(self):
        self.__update_helping_status()
        return self.is_helping

    def __update_helping_probability(self):
        """
        Calculates the probability that this agent will help by weighing
        the level of audience inhibition (drive not to help)
        and the perceived cost of non-intervention (drive to help).
        """
        pass

    def __update_helping_status(self):
        """Updates whether the agent is helping or not based on the helping probability and the helping threshold."""
        if not self.is_helping:  # we are currently assuming that once an agent helps it doesn't stop again
            if self.helping_probability >= self.helping_threshold:
                self.is_helping = True

    def __update_feeling_of_responsibility(self):
        n_perceived_bystanders = self.n_responsibility_group
        responsibility = 1/n_perceived_bystanders  # it could make sense to use a growth curve in here to reflect how at some point more bystanders will not have more of an effect (check studies)
        # inlcude helping tendency
        return responsibility

    def __update_perceived_seriousness(self):
        pass

    def __update_cost_of_non_intervention(self):
        pass

    def __update_audience_inhibition(self):
        pass
