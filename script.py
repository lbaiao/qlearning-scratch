from environment import Environment
from qlearning import Qlearning

MAX_NUM_EPISODES = 50000
STEPS_PER_EPISODE = 200 #  This is specific to MountainCar. May change with env
EPSILON_MIN = 0.005
max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE
EPSILON_DECAY = 500 * EPSILON_MIN / max_num_steps
ALPHA = 0.05  # Learning rate
GAMMA = 0.98  # Discount factor

env = Environment()
q = Qlearning(env, MAX_NUM_EPISODES, STEPS_PER_EPISODE, EPSILON_MIN, EPSILON_DECAY, ALPHA, GAMMA)
