import gymnasium as gym
from gymnasium import spaces

import numpy as np
import random

# A lot of this code very liberally uses the example found here: 
# https://github.com/Farama-Foundation/gym-examples/blob/main/gym_examples/envs/grid_world.py
class connect4Env(gym.Env):
    # Different rendering modes, text returns a ascii form of the game to the console and
    # Pygame uses the pygame library to draw out the game
    metadata = {"render_modes":["text", "pygame"]}

    def __init__(self, render_mode=None):
        # Shape of the board
        # Note that the shape is a rotated version of traditional board, this makes indexing easier
        self.shape=(7, 6)
        # A list of players (red or black)
        self.player_list = ["red", "black"]

        # Observation space, a matrix representation of the board where -1 is the opponent's pieces,
        # 1 is the player's pieces, and 0 represents no piece present on that spcae
        self.observation_space = spaces.Box(low=-1, high=1, shape=self.shape, dtype=int)

        # Action space, each number corresponds to one of the columns to place a piece
        self.action_space = spaces.Discrete(7)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _get_obs(self):
        return self.board
    
    # Might be useful later, if not then delete. Thinking about storing reward info here
    def _get_info(self):
        return self.current_player

    # Resets the environment, seed determines who goes first. Options currently unused but
    # might be implemented later
    def reset(self, seed=None, options=None):
        # Needed to properly seed
        super().reset(seed=seed)
        random.seed(seed)

        # Chooses a player at random to start
        self.current_player = random.choice(self.player_list)

        # Setup a clear board (all 0s)
        self.board = np.zeros(shape=self.shape, dtype=int)

        observation = self._get_obs()
        info = self._get_info()

        return observation, info
    
    # Take the next step forward in the environment, in this case placing a piece
    def step(self, action):
        # Place a piece
        self.placePiece(action)
        return self.board
    
    # Edits the board to place a piece, if a piece can't be placed throws an 
    # out of bounds error currently
    def placePiece(self, column):
        # First need to find first empty space (0) in the column
        placeInd, = np.where(self.board[column] == 0)
        placeInd = placeInd[0] # Originator of out of bounds error, can check placeInd before this step to remove
        # Next, change the board at the first empty space
        self.board[column, placeInd] = 1

    # Renders the game
    def render(self):
        # Rendering in console
        if self.render_mode == None or self.render_mode == "text":
            renderedBoard = np.rot90(self.board, 1)
            return renderedBoard
        # Rendering in pygame
        else:
            return "Uh oh!"

    # Needed for the environment, but no implementation right now
    # If working with pygame, implement stuff here!
    def close(self):
        pass