from classes.Agent import PartyAgents as AgentClass
import mesa
from mesa.discrete_space import OrthogonalMooreGrid


def compute_gini(model):
    ...


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
            model_reporters={"Gini": compute_gini},
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
        AgentClass.create_agents(
            self,
            self.num_agents,
            cell=self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
            n_bystanders=[self.random.randint(1, 5) for _ in range(self.num_agents)],
            seriousness=[self.random.random() for _ in range(self.num_agents)],
            helping_tendency=[self.random.random() for _ in range(self.num_agents)],
            confidence=[self.random.random() for _ in range(self.num_agents)],
            judgement_fear=[self.random.random() for _ in range(self.num_agents)],
        )

    def step(self):
        self.datacollector.collect(self)


