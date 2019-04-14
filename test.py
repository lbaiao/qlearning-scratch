from environment import Environment
import math

obj = Environment()
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))

obj.changePosition(4)
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionUp(obj)
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
    
obj.actionUp(obj)
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionDown(obj)
print("going down")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

# print(math.floor(obj.position/obj.ratScenario.shape[1]))
# print(obj.ratScenario.shape)

obj.actionDown(obj)
print("going down")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionLeft(obj)
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionLeft(obj)
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
    
obj.actionUp(obj)
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionLeft(obj)
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionRight(obj)
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionRight(obj)
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionUp(obj)
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionRight(obj)
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario)) 

obj.actionLeft(obj)
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))

obj.actionRight(obj)
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))   


