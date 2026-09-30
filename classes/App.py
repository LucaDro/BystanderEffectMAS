import solara
from mesa.visualization import SolaraViz, SpaceRenderer, make_plot_component
from mesa.visualization.components import AgentPortrayalStyle

import Environment


def agent_portrayal(agent):
    portrayal = AgentPortrayalStyle(size=50, color="tab:orange")
    portrayal.update(("color", "tab:blue"), ("size", 100))
    return portrayal

model_params = {
    "n": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "width": 10,
    "height": 10,
}
plot_comp = make_plot_component("encoding", page=1)
@solara.component
def CustomComponent():
    ...
my_model = Environment.Environment(n=50, width=10, height=10)
renderer = (
    SpaceRenderer(model=my_model, backend="altair")
    .setup_agents(agent_portrayal)
    .render()
)





my_model = Environment.Environment(n=50, width=10, height=10)
renderer = (
    SpaceRenderer(model=my_model, backend="matplotlib")
    .setup_agents(agent_portrayal)
    .render()
)

GiniPlot = make_plot_component("Gini")

page = SolaraViz(
    my_model,
    renderer,
    components=[
        GiniPlot,
        plot_comp,
    ],
    model_params=model_params,
    name="Bystander Model",
)
