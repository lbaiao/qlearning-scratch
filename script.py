from environment import Environment
from qlearning import Qlearning
import numpy as np

# agent parameters
MAX_NUM_EPISODES = 20000
STEPS_PER_EPISODE = 20 #  This is specific to MountainCar. May change with env
EPSILON_MIN = 0.005
max_num_steps = MAX_NUM_EPISODES * STEPS_PER_EPISODE
EPSILON_DECAY = 1000 * EPSILON_MIN / max_num_steps
ALPHA = 0.05  # Learning rate
GAMMA = 0.98  # Discount factor

# training function
def train(agent, env):
    # best_reward = -float('inf')
    best_reward = 0
    for episode in range(agent.maxNumEpisodes):
        env.reset()
        done = False
        obs =  env.getPosition()
        total_reward = 0.0
        i = 0
        while not done:            
            if i >= agent.maxNumSteps:
                break
            else:
                action = agent.getAction(obs)
                next_obs, reward, done = env.step(action)
                # print('step {}'.format(i))
                i +=1
                # if i > 100:
                #     print("fudeu")
                agent.learn(obs,action,reward,next_obs)
                obs = next_obs
                total_reward += reward
        if total_reward > best_reward:
            best_reward = total_reward
        print("Episode#:{} reward:{} best_reward:{} eps:{}".format(episode,
                                     total_reward, best_reward, agent.epsilon))
    
     # Return the trained policy
    return np.argmax(agent.qTable, axis=1)

# tests the learned policy
def test(agent, env, policy):
    done = False
    obs = env.getPosition()
    total_reward = 0.0
    i = 0
    print("RewardScenario: \n{}".format(env.rewardScenario))
    print("RatScenario: \n{}".format(env.ratScenario))
    print("================================================")
    while not done:
        # if i == 20:
        #     print('fudeu')
        action = policy[obs]
        next_obs, reward, done = env.step(action)
        obs = next_obs
        total_reward += reward
        print("RewardScenario: \n{}".format(env.rewardScenario))
        print("RatScenario: \n{}".format(env.ratScenario))
        print("total reward: {}".format(total_reward))
        print("================================================")
        i+=1
    return total_reward

if __name__ ==  "__main__":
    env = Environment()
    agent = Qlearning(env, MAX_NUM_EPISODES, STEPS_PER_EPISODE, EPSILON_MIN, EPSILON_DECAY, ALPHA, GAMMA)
    learned_policy = train(agent,env)
    env = Environment()
    for i in range(10):
        test(agent, env, learned_policy)
        env.reset()
        print('DONE \n\n')     
    # test(agent, env, learned_policy)    
    print("done")