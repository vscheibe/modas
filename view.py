""" View of the webview, e.g. colors, styles are defined here """
from agent import BirdAgent
from predator import PredatorAgent


def agent_portrayal(agent):
    """ Define agent portrayal """
    direction = agent.get_direction()
    print(direction)
    color_predator = "red"
    color_bird = "green"

    portrayal = {
        "scale": 0.75,
        "Layer": 0,
    }
    if isinstance(agent, BirdAgent):
        if direction == (0, 1) or direction == (0, 2):
            portrayal["Shape"] = "ArrowheadNORTH.png"
        elif direction == (1, 1) or direction == (1, 2) or direction == (2, 2) or direction == (2, 1):
            portrayal["Shape"] = "ArrowheadNORTHEAST.png"
        elif direction == (1, 0) or direction == (2, 0):
            portrayal["Shape"] = "ArrowheadEAST.png"
        elif direction == (1, -1) or direction == (2, -1) or direction == (2, -2) or direction == (1, -2):
            portrayal["Shape"] = "ArrowheadSOUTHEAST.png"
        elif direction == (0, -1) or direction == (0, -2):
            portrayal["Shape"] = "ArrowheadSOUTH.png"
        elif direction == (-1, -1) or direction == (-2, -2) or direction == (-1, -2) or direction == (-2, -1):
            portrayal["Shape"] = "ArrowheadSOUTHWEST.png"
        elif direction == (-1, 0) or direction == (-2, 0):
            portrayal["Shape"] = "ArrowheadWEST.png"
        elif direction == (-1, 1) or direction == (-2, 2) or direction == (-2, 1) or direction == (-1, 2):
            portrayal["Shape"] = "ArrowheadNORTHWEST.png"


    elif isinstance(agent, PredatorAgent):
        portrayal["Shape"] = "circle"

    return portrayal
