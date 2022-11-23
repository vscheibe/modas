import sys
import math
from itertools import product

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import SingleGrid
from mesa.time import RandomActivation

import agent
import config
import predator


class FlockingModel(Model):

    def __init__(self,
                 number_agents,
                 width: int,
                 height: int,
                 toroidal: bool,
                 seed=None):
        """ Constructor for EvolModel
            seed=None means seed is chosen from system time
        """
        super().__init__(seed=seed)
        self.width = width
        self.height = height
        self.grid = SingleGrid(width, height, toroidal)
        self.schedule = RandomActivation(self)
        self.running = True
        self.cycle = 0
        self.num_agents = 0
        self.has_predator = False

        """Places Agents randomly"""  # TODO
        coordinates = self.random.sample(
            list(product(range(0, width), range(0, height))), k=number_agents)
        for i in range(number_agents):
            new_agent = agent.BirdAgent(self.next_id(), self)
            x_pos, y_pos = coordinates[i]
            self.add_agent(new_agent, x_pos, y_pos)

    def step(self):
        """ Executes one step of the model """
        self.schedule.step()
        self.cycle += 1
        #self.add_predator TODO
        #self.terminate() TODO
        sys.stdout.write(" %d <-- %d \r" % (config.MAXIMUM_STEPS, self.cycle))
        sys.stdout.flush()

    def terminate(self):
        """ Stops the simulation if the model has reached termination conditions """
        # TODO

    def add_agent(self, new_agent, x_pos, y_pos):
        """ Add an agent to the schedule and to the board"""
        self.schedule.add(new_agent)
        self.grid.place_agent(new_agent, (x_pos, y_pos))
        if isinstance(new_agent, predator.PredatorAgent):
            self.has_predator = True
        else:
            self.num_agents += 1

    def remove_agent(self, target_agent):
        """ Remove agent from schedule, then from board """
        self.schedule.remove(target_agent)
        self.grid.remove_agent(target_agent)
        if isinstance(target_agent, predator.PredatorAgent):
            self.has_predator = False
        else:
            self.num_agents -= 1

    def add_predator(self):
        return None

    def find_empty_cell(self, grid):
        """ Returns (x,y) of a random, empty cell, or (-1,-1) if none was found """
        cell_iter = grid.coord_iter()
        empties = []
        for cell in cell_iter:
            content, x_pos, y_pos = cell
            if content is None:
                empties.append((x_pos, y_pos))
        cell = (-1, -1)
        if len(empties) > 0:
            cell = self.random.choice(empties)
        return cell

    def get_grid(self):
        """ Returns the mesa.SingleGrid held by EvolModel """
        return self.grid
