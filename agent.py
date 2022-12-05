""" Agent module for the Flocking simulation """
from copy import copy
from enum import Enum, auto
import math

from mesa import Agent

import predator
import config


def init_position(model):
    dir_x = model.random.randint(-config.MAX_VELOCITY_BIRD, config.MAX_VELOCITY_BIRD)
    dir_y = model.random.randint(-config.MAX_VELOCITY_BIRD, config.MAX_VELOCITY_BIRD)
    return dir_x, dir_y


class BirdAgent(Agent):
    """ Class modeling agent with flocking capabilities """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.dir_x, self.dir_y = init_position(model)
        self.direction = (self.dir_x, self.dir_y)
        while self.direction == (0, 0):
            print("reinitializing position")
            self.dir_x, self.dir_y = init_position(model)
            self.direction = (self.dir_x, self.dir_y)


    def get_direction(self):
        return self.direction



    def step(self):
        self.move()
        """ Executes one step of an agent """
        # TODO

    def move(self):
        neighbors = self.model.grid.get_neighborhood(self.pos, True, False, 2)
        free_cells = []
        for neighbor in neighbors:
            x_pos, y_pos = neighbor
            if self.model.grid[x_pos, y_pos] is None:
                free_cells.append(neighbor)
        x_pos, y_pos = self.pos
        move_to = (x_pos + self.dir_x, y_pos + self.dir_y)
        if move_to in free_cells:
            self.model.grid.move_agent(self, move_to)

    def random_movement(self):
        """Moves birds in one direction"""
    def alignment_movement(self):
        """birds align"""
    def cohesion_movement(self):
        """birds align and have cohesion"""
    def avoiding_dispersion_movement(self):
        """birds avoid dispersion and collision*"""
    def fleeing_from_predator(self):
        """Final movement type"""

    def get_id(self):
        """ Get unique ID of the agent """
        return self.unique_id