from manpy.simulation.imports import (
    Machine,
    Queue,
    Part,
)
from manpy.simulation.Globals import runSimulation

# define the objects of the model
M1 = Machine("M1", "Machine1", processingTime={"fromList": {"path": "M1_proclist"}})
M2 = Machine("M2", "Machine2", processingTime={"fromList": {"path": "M2_proclist"}})
Q1 = Queue("Q1", "Queue1", capacity=5)
Q2 = Queue("Q2", "Queue2", capacity=2)
entityList = []
numOfParts = 2
for i in range(numOfParts):  # create the WIP in a loop
    Q1PartId = "P" + str(i)
    Q1PartName = "Part" + str(i)
    PQ1 = Part(Q1PartId, Q1PartName, currentStation=Q1)
    entityList.append(PQ1)

# define predecessors and successors for the objects
Q1.defineRouting(predecessorList=[M2], successorList=[M1])
M1.defineRouting(predecessorList=[Q1], successorList=[Q2])
Q2.defineRouting(predecessorList=[M1], successorList=[M2])
M2.defineRouting(predecessorList=[Q2], successorList=[Q1])


def main():

    # add all the objects in a list
    objectList = [Q1, M1, Q2, M2] + entityList
    # set the length of the experiment
    maxSimTime = 100000
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime, numberOfReplications=1)

    print("The exit of each replication is:")
    print(M1.timeLastEntityLeft)
    print(M2.timeLastEntityLeft)


if __name__ == "__main__":
    main()
