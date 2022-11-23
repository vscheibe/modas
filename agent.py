""" Agent module for the Flocking simulation """
from copy import copy
from enum import Enum, auto
import math

from mesa import Agent

import predator
import config

class BirdAgent(Agent):
    """ Class modeling agent with evolutionary capabilities """

    class Compass(Enum):
        """ Compass enum used for directional logic """
        NORTH = auto()
        WEST = auto()
        SOUTH = auto()
        EAST = auto()
        # TODO

    def __init__(self, unique_id, model):
        """ Once max_age is reached, agent automatically dies """
        super().__init__(unique_id, model)
        self.direction = model.random.choice(list(self.Compass))
        # TODO

    def step(self):
        """ Executes one step of an agent """
        # TODO

    def turn(self):
        """ Action: Turn to face a direction """
        # TODO

    def move_forward(self):
        """ Action: Move 1 cell in current direction """
        # TODO

    def get_direction_unit_vector(self):
        """ Movement helper method
            Calculates the movement vector of an agent
        """
        # TODO Add 4 more vectors

        x_pos_add = 0
        y_pos_add = 0
        match self.direction:
            case self.Compass.NORTH:
                x_pos_add = -1
            case self.Compass.SOUTH:
                x_pos_add = 1
            case self.Compass.WEST:
                y_pos_add = -1
            case self.Compass.EAST:
                y_pos_add = 1
        return x_pos_add, y_pos_add

    def get_id(self):
        """ Get unique ID of the agent """
        return self.unique_id