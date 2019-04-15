import numpy
import math

class Environment:
    # constructor
    def __init__(self):
        # properties: 
            # position
            # ratScenario
            # rewardScenario
            # totalReward
            # reward
            # done
            # actionVector
        
        self.actionVector = numpy.array([0,1,2,3])
        self.positionVector = numpy.array([0,1,2,3,4,5])
        self.totalReward = 0
        self.reward = 0
        self.done = False
        self.buildRatScenario()
        self.buildRewardEnvironment()        
        self.start()        
    
    # builds a matrix that represents the rat position
    def buildRatScenario(self):
        env = numpy.zeros((2,3),int)
        self.ratScenario = env

    # builds a matrix that represents the rewards positions
    def buildRewardEnvironment(self):
        env = numpy.matrix([[0,1,0],[3,4,5]])
        self.rewardScenario = env

    # positions the rat into the environment, at the first position
    def start(self):
        self.ratScenario[0,0] = 99
        self.position = 0

    # changes the rat's position, according to position argument
    # 0 <= position <= 5        
    def updateRatRewardMatrix(self, position):        
        scenarioColumns = self.ratScenario.shape[1]
        self.ratScenario = numpy.zeros((2,3),int)
        self.ratScenario[math.floor(position/scenarioColumns), position % scenarioColumns] = 99
        self.rewardScenario[math.floor(position/scenarioColumns), position % scenarioColumns] = 0

    # moves the rat upwards, except when it is at scenario's upper edges
    def actionUp(self):
        if self.position/self.ratScenario.shape[1] >= 1:
            self.position -= self.ratScenario.shape[1]
            self.setReward()
            self.updateRatRewardMatrix(self.position)             
        else:
            self.setReward()

    # moves the rat upwards, except when it is at scenario's lower edges
    def actionDown(self):
        if self.position/self.ratScenario.shape[1] < self.ratScenario.shape[0]-1:
            self.position += self.ratScenario.shape[1]
            self.setReward()
            self.updateRatRewardMatrix(self.position)
        else: 
            self.setReward()

    # @staticmethod
    # def actionLeft(self):
    #     if self.ratScenario[:,0].all != numpy.zeros(self.ratScenario.shape[0] ,dtype=int).all:
    #         self.position -= 1
    #         self.updateRatRewardMatrix(self.position)

    # moves the rat upwards, except when it is at scenario's left edges
    def actionLeft(self):
        if self.position != 0 and self.position != 3:
            self.position -= 1
            self.setReward()
            self.updateRatRewardMatrix(self.position)
        else: 
            self.setReward()

    # moves the rat upwards, except when it is at scenario's right edges
    def actionRight(self):
        if self.position !=2 and self.position != 5:
            self.position += 1
            self.setReward()
            self.updateRatRewardMatrix(self.position)
        else:
            self.setReward()
    
    # sets the reward according to the rewardScenario matrix status
    def setReward(self):
        scenarioColumns = self.rewardScenario.shape[1]
        state = self.rewardScenario[math.floor(self.position/scenarioColumns), self.position % scenarioColumns]
        if state == 0:
            reward = -1
            # reward = 0
        elif state == 1:
            reward = 1
        elif state == 3:
            reward = 2
        elif state == 4:
            # reward = -100
            reward = -10
            self.done = True
        elif state == 5:
            reward = 10
            self.done = True
        self.reward = reward
        self.totalReward += reward    

    # makes the environment perform a step
    def step(self, action):
        if action == 0:
            self.actionUp()
        elif action == 1:
            self.actionDown()
        elif action == 2:
            self.actionLeft()
        elif action == 3:
            self.actionRight()
        return self.position, self.reward, self.done
    
    # resets some of the environment attributes
    def reset(self):
        self.totalReward = 0
        self.reward = 0
        self.done = False
        self.buildRatScenario()
        self.buildRewardEnvironment()        
        self.start()        

    # returns a vector with the environment's action representations
    def getActionVector(self):
        return self.actionVector

    # returns the accumulated totalReward
    def getTotalReward(self):
        return self.totalReward
    
    # returns the most recent reward    
    def getReward(self):
        return self.reward

    # returns the done status
    def getDone(self):
        return self.done
    
    # returns the rat's actual position
    def getPosition(self):
        return self.position
    
    # returns the environment's position vector
    def getPositionVector(self):
        return self.positionVector
    
        

        


        


        
    