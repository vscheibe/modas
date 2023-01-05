""" The main module, from which the webview is run """
import sys
import pandas as pd

from mesa.batchrunner import batch_run
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

import config
from model import FlockingModel
from view import agent_portrayal


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


def b_run():
    """ Runs a parameter sweeping batch run """
    params = {"number_agents": config.AMOUNT_BIRDS,
              "width": config.GRID_WIDTH,
              "height": config.GRID_HEIGHT,
              "toroidal": config.GRID_TOROIDAL,
              "seed": config.SEED
              }

    results = batch_run(
        FlockingModel,
        parameters=params,
        iterations=config.ITERATIONS,
        max_steps=config.MAXIMUM_STEPS,
        number_processes=config.NUMBER_PROCESSES,
        data_collection_period=config.DATA_COLLECTION_PERIOD,
        display_progress=False,
    )
    results_df = pd.DataFrame(results)
    results_df.to_csv('output\\results.csv')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-brun':
            b_run()
        elif sys.argv[1] == '-vrun':
            visualized_single_run()
        else:
            print("Please specify the execution mode.")
            print("Use argument -brun for batch execution or -vrun for a single run with visualization.")
    else:
        print("Please specify the execution mode.")
        print("Use argument -brun for batch execution or -vrun for a single run with visualization.")
