from classes.Agent import PartyAgents as AgentClass
import mesa
from mesa.discrete_space import OrthogonalMooreGrid
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def compute_helpers(model):
    n = model.num_agents
    helpers = 0
    helpers += sum([1 if agent.called_out is True else 0 for agent in model.agents])
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
                rng=None):
        super().__init__(rng=rng)
        self.num_agents = n
        self.grid = OrthogonalMooreGrid((width, height), torus=True, random=self.random)
        self.datacollector = mesa.DataCollector(
            model_reporters={"helpers percentage": compute_helpers,
                             "called_out_helpers": compute_called_out_helpers,
                             "non called out helpers": compute_non_called_out_helpers},
            agent_reporters={
                "n_bystanders": "n_bystanders",
                "seriousness": "seriousness",
                "helping_tendency": "helping_tendency",
                "confidence": "confidence",
                "judgement_fear": "judgement_fear",
                "n_responsibility_group": "n_responsibility_group",
                "n_helpers": "n_helpers",
            },
        )
        agents = AgentClass.create_agents(
            self,
            self.num_agents,
            cell=self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
            n_bystanders=self.num_agents-1,
            seriousness=[self.random.random() for _ in range(self.num_agents)],
            helping_tendency=[self.random.random() for _ in range(self.num_agents)],
            confidence=[self.random.random() for _ in range(self.num_agents)],
            judgement_fear=[self.random.random() for _ in range(self.num_agents)],
        )

    def step(self):
        self.datacollector.collect(self)
        helpers = len(self.agents.select(lambda a: a.is_helping == True))
        self.agents.do("perceive_helpers", helpers)
        self.agents.do("decide_take_action")

    def extract_data(self):
        helpers_over_time = self.datacollector.get_model_vars_dataframe()
        g = sns.lineplot(data=helpers_over_time)
        g.set(title="Helpers over time", ylabel="helpers")
        plt.show()
