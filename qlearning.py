import numpy as np

class Qlearning:
    def __init__(self, env, maxNumEpisodes, stepPerEpisode, epsilonMin, epsilonDecay, alpha, gamma):
        self.env = env
        self.maxNumEpisodes = maxNumEpisodes
        self.stepPerEpisode = stepPerEpisode
        self.maxNumSteps = self.maxNumEpisodes * self.stepPerEpisode
        self.epsilonMin = epsilonMin
        self.epsilonDecay = epsilonDecay 
        self.epsilon = 1
        self.alpha = alpha
        self.gamma = gamma
        self.actionVector = env.getActionVector()
        self.qTable = np.zeros((self.env.getPositionVector().shape[0]+2, self.env.getActionVector().shape[0]))
    
    # selects action according to epsilon-greedy policy
    def getAction(self, obs):
        if self.epsilon > self.epsilonMin:
            self.epsilon -= self.epsilonDecay
        if np.random.random() > self.epsilon:
            return np.argmax(self.qTable[obs,:])
        else:       # Choose a random action
            return np.random.choice([ a for a in range(self.actionVector.shape[0])])

    # calculates Q-table values
    def learn(self, obs, action, reward, nextObs):
        deltaQ = reward + self.gamma*np.max(self.qTable[nextObs]) - self.qTable[obs, action]
        self.qTable[obs, action] = self.qTable[obs,action] + self.alpha*deltaQ




        

