import numpy as np

from manpy.simulation.imports import (
    Machine,
    Source,
    Exit,
    Queue,
)
from manpy.simulation.Globals import runSimulation

# define the objects of the model
S = Source(
    "S1", "Source", interArrivalTime={"Exp": {"mean": 3.2}}, entity="manpy.Part"
)
M1 = Machine("M1", "Machine1", processingTime={"Exp": {"mean": 2.5}})
M2 = Machine("M2", "Machine2", processingTime={"Exp": {"mean": 2.6}})
M3 = Machine("M3", "Machine3", processingTime={"Exp": {"mean": 2.7}})
Q1 = Queue("Q1", "Queue1", capacity=float('inf'))
Q2 = Queue("Q2", "Queue2", capacity=5)
Q3 = Queue("Q3", "Queue3", capacity=5)
E = Exit("E1", "Exit")

# define predecessors and successors for the objects S>Q1>M1>Q2>M2>E
S.defineRouting(successorList=[Q1])
Q1.defineRouting(predecessorList=[S], successorList=[M1])
M1.defineRouting(predecessorList=[Q1], successorList=[Q2])
Q2.defineRouting(predecessorList=[M1], successorList=[M2])
M2.defineRouting(predecessorList=[Q2], successorList=[Q3])
Q3.defineRouting(predecessorList=[M2], successorList=[M3])
M3.defineRouting(predecessorList=[Q3], successorList=[E])
E.defineRouting(predecessorList=[M3])


def main():

    # add all the objects in a list
    objectList = [S, Q1, M1, Q2, M2, Q3, M3, E]
    # set the length of the experiment
    maxSimTime = 10080.0
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime, numberOfReplications=1)

    print("The exit of each replication is:")
    print(E.Exits)                        # E.Exits is a list
    NumberInSink = np.array(E.Exits)        # Convert E.Exits into an array
    Throughput = NumberInSink/maxSimTime    # Calculate the throughput for each replication
    print(Throughput)
    print(M3.completedJobs)


if __name__ == "__main__":
    main()
