import mesa
import random
from mesa.discrete_space import CellAgent


class PartyAgents(CellAgent):
    def __init__(self,
                 model: mesa.Model,
                 cell: tuple[int, int],
                 n_bystanders: int,  # other people except for this agent (if 2 people incl. agent then n_b = 1)
                 seriousness: float,  # 0 <= x <= 1
                 helping_tendency: float = 0.5,  # 0 <= x <= 1; should not stray far from 0.5, normal dist
                 confidence: float = 0.5,  # 0 <= x <= 1
                 judgement_fear: float = 0.5,  # 0 <= x <= 1
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
        self.n_responsibility_group = n_bystanders  # if they get assigned responsibility this is where that shows up
        self.n_helpers = 0  # in the beginning there are no helpers yet

        self.is_helping = False
        self.helping_probability = None

    def assign_responsibility(self, responsibility_group):
        self.n_responsibility_group = responsibility_group

    def perceive_helpers(self, n_helpers):
        self.n_helpers = min(n_helpers, self.n_bystanders)

    def get_helping_probability(self):
        self._update_helping_probability()
        return self.helping_probability

    def get_is_helping(self):
        self._update_helping_status()
        return self.is_helping

    def _update_helping_probability(self):
        """
        Calculates the probability that this agent will help by weighing
        the level of audience inhibition (drive not to help)
        and the perceived cost of non-intervention (drive to help).
        """
        cost_of_non_intervention = self._update_cost_of_non_intervention()
        self.helping_probability = cost_of_non_intervention

    def _update_helping_status(self):
        """Updates whether the agent is helping or not based on the helping probability and the helping threshold."""
        if not self.is_helping:  # we are currently assuming that once an agent helps it doesn't stop again
            if self.helping_probability > random.uniform(0, 1):
                self.is_helping = True

    def _update_feeling_of_responsibility(self):
        n_perceived_bystanders = self.n_responsibility_group
        responsibility_feeling = 1/n_perceived_bystanders  # it could make sense to use a growth curve with limit in here to reflect how at some point more bystanders will not have more of an effect (check studies)
        perceived_responsibility = responsibility_feeling #* (self.helping_tendency + 0.5)
        return perceived_responsibility

    def _update_perceived_seriousness(self):
        # log growth -> no because it has no ceiling -> exponential decay upward: f(n_h) = 1-(1-r)^n_h
        GROWTH_RATE = 0.5  # 0.5 because it does not take a lot of helpers to feel like helping too
        helper_observation = 1 - (1-GROWTH_RATE)**self.n_helpers

        # how much each of the factors contribute to perceived seriousness depends on the confidence
        # high confidence means low consideration of helper_observation and vice versa
        perceived_seriousness = (1-self.confidence) * helper_observation + self.confidence * self.seriousness
        return perceived_seriousness

    def _update_cost_of_non_intervention(self):
        WEIGHT = 0.6
        p_responsibility = self._update_feeling_of_responsibility()
        p_seriousness = self._update_perceived_seriousness()
        cost_of_non_intervention = p_responsibility * WEIGHT + p_seriousness * (1-WEIGHT)
        return cost_of_non_intervention

    def _update_audience_inhibition(self):
        """high audience inhibition -> low score close to 0"""
        # more bystanders = more fear of judgement -> exponential decay
        DECAY_RATE = 0.1
        INITIAL_AMOUNT = 0.5  # if there is no one watching your action would not change
        bystander_fear = INITIAL_AMOUNT * (1-DECAY_RATE)**self.n_bystanders

        # less helpers -> helping more out of norm -> more chance of negative judgement -> more fear
        # ROWTH_RATE = 0.5  # 0.5 because it does not take a lot of helpers to feel like helping too
        # helper_observation = 1 - (1 - GROWTH_RATE) ** self.n_helpers

        # idk man ignore this for now
