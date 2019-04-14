import numpy
import sys
sys.path.insert(0,'/home/lucas/ai/hardcore')
from environment import Environment

class TestEnvironmentClass:

    def __init__(self):
        self.obj = Environment()

    # testing __init__ method
    @staticmethod
    def testInitMethod():        
        try:
            obj = Environment()        
            if obj.ratScenario == numpy.zeros((2,3),int):
                if obj.buildRewardEnvironment == numpy.matrix([[0,1,2],[3,4,5]]):
                    if obj.ratScenario[0] == 99 and obj.position == 0:                
                        return "__init__: OK"
            else:
                return "__init__: ERROR"            
        except:
            return "__init__: ERROR"

    def testBuildRatScenario(self):
        try:
            if self.obj.buildRatScenario() == numpy.zeros((2,3),int):
                return "buildRatScenario: OK"
            else:
                return "buildRatScenario: ERROR"
        except:
            return "buildRatScenario: ERROR"
