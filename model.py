import sys
import math
import itertools
import numpy

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import SingleGrid
from mesa.time import RandomActivation

import agent
import config
import predator


def get_center_of_grid():
    x_pos, y_pos = int((config.GRID_HEIGHT - 1) / 2), int((config.GRID_HEIGHT - 1) / 2)
    return x_pos, y_pos


class FlockingModel(Model):

    def __init__(self,
                 number_agents,
                 width: int,
                 height: int,
                 toroidal: bool,
                 seed=None):
        """ Constructor for Flocking Model
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
        self.datacollector = DataCollector(model_reporters={"Cohesion": "cohesion"})
        # Places Birds in the center as a flock
        first_cells = self.get_starting_cells()
        start_cells = self.random.sample(first_cells, k=number_agents)
        for i in range(number_agents):
            new_agent = agent.BirdAgent(self.next_id(), self)
            x_pos, y_pos = start_cells[i]
            self.add_agent(new_agent, x_pos, y_pos)
        self.add_predator()
        self.cohesion = self.calculate_cohesion()

    def calculate_lower_left_corner(self):
        cells = self.get_starting_cells()
        distance = config.SPAWN_DISTANCE_FROM_SWARM
        pos_x = cells[0][0]
        pos_y = cells[0][1]
        return pos_x - distance, pos_y - distance

    def calculate_cohesion(self):
        distance_array = []
        bird_array = []
        for bird in self.schedule.agents:
            if bird != self and not isinstance(bird, predator.PredatorAgent):
                bird_array.append(bird)
        for a, b in itertools.combinations(bird_array, 2):
            a_x, a_y = a.pos
            b_x, b_y = b.pos
            distance = abs(a_x - b_x) + abs(a_y - b_y)
            distance_array.append(distance)
        mean_distance = numpy.mean(distance_array)
        return mean_distance

    def step(self):
        """ Executes one step of the model """
        self.datacollector.collect(self)
        self.schedule.step()
        self.cohesion = self.calculate_cohesion()
        self.cycle += 1
        self.terminate()
        sys.stdout.write(" %d <-- %d \r" % (config.MAXIMUM_STEPS, self.cycle))
        sys.stdout.flush()

    def terminate(self):
        """ Stops the simulation if the model has reached termination conditions """
        if self.cycle == config.MAXIMUM_STEPS:
            self.running = False
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
        new_predator = predator.PredatorAgent(self.next_id(), self)
        low_x, low_y = self.calculate_lower_left_corner()
        self.add_agent(new_predator, low_x, low_y)

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

    def get_starting_cells(self):
        birds = config.AMOUNT_BIRDS
        cells_in_neighborhood = 0
        i = 0
        while cells_in_neighborhood < birds:
            i = i + 1
            cells_in_neighborhood = ((2 * i) + 1) * ((2 * i) + 1)
        center = get_center_of_grid()
        neighbors = self.grid.get_neighborhood(center, True, True, i + config.INITIAL_FLOCK_DISPERSION)

        return neighbors
