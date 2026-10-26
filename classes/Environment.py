from classes.Agent import PartyAgents as AgentClass
import mesa
from mesa.discrete_space import OrthogonalMooreGrid
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def compute_helpers(model):
    n = model.num_agents
    helpers = 0
    helpers += sum(1 for agent in model.bystanders if agent.is_helping is True)
    print(helpers)
    helpers_percentage = helpers/n
    return helpers_percentage

def compute_called_out_helpers(model):
    """Computes the amount of people in the called out group that are helpers"""
    pass

def compute_non_called_out_helpers(model):
    """Computes the amount of people in the non called out group that are helpers"""
    pass


class Environment(mesa.Model):

    def __init__(self,
                *,
                n,
                width,
                height,
                agents_helping: int = 0,
                rng=None):
        super().__init__(rng=rng)
        self.num_agents = n
        self.agents_helping = agents_helping
        self.grid = OrthogonalMooreGrid((width, height), torus=True, random=self.random)
        self.datacollector = mesa.DataCollector(
            model_reporters={"helpers percentage": compute_helpers,
                             "called_out_helpers": compute_called_out_helpers,
                             "non called out helpers": compute_non_called_out_helpers},
            agenttype_reporters={
                AgentClass: {
                    "n_bystanders": "n_bystanders",
                    "seriousness": "seriousness",
                    "helping_tendency": "helping_tendency",
                    "confidence": "confidence",
                    "judgement_fear": "judgement_fear",
                    "n_responsibility_group": "n_responsibility_group",
                    "n_helpers": "n_helpers",
                },
            },
        )
        self.bystanders = AgentClass.create_agents(
            self,
            self.num_agents,
            cell=self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
            n_bystanders=self.num_agents,
            seriousness=1,
            helping_tendency=[np.random.normal(0.5, 0.25) for _ in range(self.num_agents)],
            confidence=[np.random.normal(0.5, 0.25) for _ in range(self.num_agents)],
            judgement_fear=[np.random.normal(0.5, 0.25) for _ in range(self.num_agents)],
        )

        self.schedule_event(self.call_for_help, at=0.0)
        print("this is it")
        print(np.random.normal(0.5, 1))

    def call_for_help(self):
        selected_agents = self.random.sample(
            list(self.bystanders),
            k=self.agents_helping,
        )
        for agent in selected_agents:
            agent.is_helping = True

    def step(self):
        self.datacollector.collect(self)
        helpers = len(self.bystanders.select(lambda a: a.is_helping == True))
        self.bystanders.do("perceive_helpers", helpers)
        self.bystanders.do("decide_take_action")

    def extract_data(self):
        self.helpers_over_time = self.datacollector.get_model_vars_dataframe()
        g = sns.lineplot(data=self.helpers_over_time)
        g.set(title="Helpers over time", ylabel="helpers")
        plt.show()

    def get_total_helpers(self):
        return len(self.bystanders.select(lambda a: a.is_helping == True))
