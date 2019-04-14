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
        
        self.totalReward = 0
        self.reward = 0
        self.done = False
        self.buildRatScenario()
        self.buildRewardEnvironment()        
        self.start()        
        pass
    
    # builds a matrix that represents the rat position
    def buildRatScenario(self):
        env = numpy.zeros((2,3),int)
        self.ratScenario = env
        pass

    # builds a matrix that represents the rewards positions
    def buildRewardEnvironment(self):
        env = numpy.matrix([[0,1,0],[3,4,5]])
        self.rewardScenario = env
        pass

    # positions the rat into the environment, at the first position
    def start(self):
        self.ratScenario[0,0] = 99
        self.position = 0

    # changes the rat's position, according to position argument
    # 0 <= position <= 5        
    def changePosition(self, position):        
        self.position = position
        scenarioColumns = self.ratScenario.shape[1]
        self.setReward()
        self.ratScenario = numpy.zeros((2,3),int)
        self.ratScenario[math.floor(position/scenarioColumns), position % scenarioColumns] = 99
        self.rewardScenario[math.floor(position/scenarioColumns), position % scenarioColumns] = 0

    # moves the rat upwards, except when it is at scenario's upper edges
    def actionUp(self):
        if math.floor(self.position/self.ratScenario.shape[1])>0:
            self.position -= self.ratScenario.shape[1]          
            self.changePosition(self.position) 

    # moves the rat upwards, except when it is at scenario's lower edges
    def actionDown(self):
        if math.ceil(self.position/self.ratScenario.shape[1])<self.ratScenario.shape[0]:
            self.position += self.ratScenario.shape[1]
            self.changePosition(self.position)

    # @staticmethod
    # def actionLeft(self):
    #     if self.ratScenario[:,0].all != numpy.zeros(self.ratScenario.shape[0] ,dtype=int).all:
    #         self.position -= 1
    #         self.changePosition(self.position)

    # moves the rat upwards, except when it is at scenario's left edges
    def actionLeft(self):
        if self.position != 0 and self.position != 3:
            self.position -= 1
            self.changePosition(self.position)
    
    # moves the rat upwards, except when it is at scenario's right edges
    def actionRight(self):
        if self.position !=2 and self.position != 5:
            self.position += 1
            self.changePosition(self.position)
    
    # sets the reward according to the rewardScenario matrix status
    def setReward(self):
        scenarioColumns = self.rewardScenario.shape[1]
        state = self.rewardScenario[math.floor(self.position/scenarioColumns), self.position % scenarioColumns]
        if state == 0:
            reward = -1
        elif state == 1:
            reward = 1
        elif state == 3:
            reward = 2
        elif state == 4:
            reward = -100
            self.done = True
        elif state == 5:
            reward = 10
            self.done = True
        self.reward = reward
        self.totalReward += reward        

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
    
        

        


        


        
    