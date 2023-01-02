""" View of the webview, e.g. colors, styles are defined here """
from agent import BirdAgent
from predator import PredatorAgent


def agent_portrayal(agent):
    """ Define agent portrayal """
    portrayal = {
        "scale": 0.75,
        "Layer": 0,
    }

    if isinstance(agent, BirdAgent):

        direction = agent.get_direction()
        if direction == (0, 1) or direction == (0, 2):
            portrayal["Shape"] = "img/ArrowheadNORTH.png"
        elif direction == (1, 1) or direction == (1, 2) or direction == (2, 2) or direction == (2, 1):
            portrayal["Shape"] = "img/ArrowheadNORTHEAST.png"
        elif direction == (1, 0) or direction == (2, 0):
            portrayal["Shape"] = "img/ArrowheadEAST.png"
        elif direction == (1, -1) or direction == (2, -1) or direction == (2, -2) or direction == (1, -2):
            portrayal["Shape"] = "img/ArrowheadSOUTHEAST.png"
        elif direction == (0, -1) or direction == (0, -2):
            portrayal["Shape"] = "img/ArrowheadSOUTH.png"
        elif direction == (-1, -1) or direction == (-2, -2) or direction == (-1, -2) or direction == (-2, -1):
            portrayal["Shape"] = "img/ArrowheadSOUTHWEST.png"
        elif direction == (-1, 0) or direction == (-2, 0):
            portrayal["Shape"] = "img/ArrowheadWEST.png"
        elif direction == (-1, 1) or direction == (-2, 2) or direction == (-2, 1) or direction == (-1, 2):
            portrayal["Shape"] = "img/ArrowheadNORTHWEST.png"


    elif isinstance(agent, PredatorAgent):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "red"
        portrayal["Filled"] = "true"
        portrayal["r"] = 0.75

    return portrayal


