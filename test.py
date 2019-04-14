from environment import Environment
import math

obj = Environment()
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{} \n\n========================================="
    .format(obj.rewardScenario))

obj.changePosition(4)
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))
print("done: \n{}".format(obj.getDone()))        
print("=========================================\n")

obj.actionUp()
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")

    
obj.actionUp()
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")


obj.actionDown()
print("going down")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")


# print(math.floor(obj.position/obj.ratScenario.shape[1]))
# print(obj.ratScenario.shape)

obj.actionDown()
print("going down")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")


obj.actionLeft()
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionLeft()
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionUp()
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionLeft()
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionRight()
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionRight()
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionUp()
print("going up")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionRight()
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario)) 
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionLeft()
print("going left")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



obj.actionRight()
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))   
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")


obj.actionDown()
print("going right")
print("self.position: {}".format(obj.getPosition()))
print("ratScenario:\n{}".format(obj.ratScenario))   
print("rewardScenario:\n{}".format(obj.rewardScenario))
print("reward: \n{}".format(obj.getReward()))   
print("total reward: \n{}".format(obj.getTotalReward()))  
print("done: \n{}".format(obj.getDone()))         
print("=========================================\n")



