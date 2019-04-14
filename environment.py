import numpy
import math

class Environment:
    # constructor
    def __init__(self):
        # properties: 
            # position
            # ratScenario
            # rewardScenario
            # zeroMatrix
        
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
        env = numpy.matrix([[0,1,2],[3,4,5]])
        self.rewardScenario = env
        pass

    # positions the rat into the environment, at the first position
    def start(self):
        self.ratScenario[0,0] = 99
        self.position = 0
    
    # returns the rat's actual position
    def getPosition(self):
        return self.position

    # changes the rat's position, according to position argument
    def changePosition(self, position):
        # 0 <= position <= 5        
        self.position = position
        scenarioColumns = self.ratScenario.shape[1]
        self.ratScenario = numpy.zeros((2,3),int)
        self.ratScenario[math.floor(position/scenarioColumns), position % scenarioColumns] = 99

    # moves the rat upwards, except when it is at scenario's upper edges
    @staticmethod
    def actionUp(self):
        if math.floor(self.position/self.ratScenario.shape[1])>0:
            self.position -= self.ratScenario.shape[1]          
            self.changePosition(self.position) 

    @staticmethod
    def actionDown(self):
        if math.ceil(self.position/self.ratScenario.shape[1])<self.ratScenario.shape[0]:
            self.position += self.ratScenario.shape[1]
            self.changePosition(self.position)

    # @staticmethod
    # def actionLeft(self):
    #     if self.ratScenario[:,0].all != numpy.zeros(self.ratScenario.shape[0] ,dtype=int).all:
    #         self.position -= 1
    #         self.changePosition(self.position)

    @staticmethod
    def actionLeft(self):
        if self.position != 0 and self.position != 3:
            self.position -= 1
            self.changePosition(self.position)
    
    @staticmethod
    def actionRight(self):
        if self.position !=2 and self.position != 5:
            self.position += 1
            self.changePosition(self.position)
    
#TODO: implement the change rewardScenario mechanism into the actions


        


        
    