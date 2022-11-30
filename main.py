""" The main module, from which the webview is run """
import sys
import pandas as pd

from mesa.batchrunner import batch_run
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

import config  # TODO
from model import FlockingModel
from view import agent_portrayal  # TODO


def visualized_single_run():
    """ Run the webserver and canvas view """
    grid = CanvasGrid(agent_portrayal, config.GRID_WIDTH, config.GRID_HEIGHT, config.GRID_WIDTH * config.VIEW_SCALING,
                      config.GRID_HEIGHT * config.VIEW_SCALING)

    server = ModularServer(FlockingModel,
                           [grid],
                           "Flocking Model",
                           {"number_agents": config.AMOUNT_BIRDS,
                            "width": config.GRID_WIDTH,
                            "height": config.GRID_HEIGHT,
                            "toroidal": config.GRID_TOROIDAL,
                            "seed": config.SEED
                            })

    server.port = 8521
    server.launch()


if __name__ == '__main__':
    visualized_single_run()
