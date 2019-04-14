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
        self.q = np.zeros((self.env.getActionVector().shape[0], self.env.getPositionVector().shape[0]))
        
    def getAction(self):
        if self.epsilon > self.epsilonMin:
            self.epsilon -= self.epsilonDecay
        if np.random.random() > self.epsilon:
            # return numpy.argmax(self.Q[])
            pass

