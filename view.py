""" View of the webview, e.g. colors, styles are defined here """
from agent import BirdAgent
from predator import PredatorAgent

def agent_portrayal(agent):
    """ Define agent portrayal """
    h_x, h_y = agent.get_direction_unit_vector()
    color_predator = "red"
    color_bird = "green"

    if isinstance(agent, BirdAgent):
        portrayal = {
            "Shape": "arrowHead",
            "Color": color_bird,
            "Filled": "true",
            "Layer": 0,
            "scale": 0.5,
            "heading_x": h_x,
            "heading_y": h_y
        }
    elif isinstance(agent, PredatorAgent):
        portrayal = {
            "Shape": "arrowHead",
            "Color": color_predator,
            "Filled": "true",
            "Layer": 0,
            "scale": 0.5,
            "heading_x": h_x,
            "heading_y": h_y
        }

    return portrayal