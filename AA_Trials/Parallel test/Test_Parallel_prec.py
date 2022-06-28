# Want to try the precedents when we have a parallel system, since if we have multiple parts blocked in a parallel it is
# not clear which parts goes first in the following machine/buffer when it becomes available.

from manpy.simulation.imports import Queue, Machine, Exit, Part
from manpy.simulation.Globals import runSimulation

# define the objects of the model
MP1 = Machine("MP1", "ParMachine", capacity=1, processingTime={"Fixed": {"mean": 1}})
MP2 = Machine("MP2", "ParMachine", capacity=1, processingTime={"Fixed": {"mean": 2}})
MP3 = Machine("MP2", "ParMachine", capacity=1, processingTime={"Fixed": {"mean": 3}})
Q2 = Queue("Q2", "Queue", capacity=1)
M2 = Machine("M2", "Machine", capacity=1, processingTime={"Fixed": {"mean": 10}})
E = Exit("E1", "Exit", gatherSysTimeEx=True)

P1 = Part("P1", "Part1", currentStation=MP1)
P2 = Part("P2", "Part2", currentStation=MP2)
P3 = Part("P3", "Part3", currentStation=MP3)
P4 = Part("P4", "Part4", currentStation=Q2)
P5 = Part("P5", "Part5", currentStation=M2)

# define predecessors and successors for the objects
MP1.defineRouting(successorList=[Q2])
MP2.defineRouting(successorList=[Q2])
MP3.defineRouting(successorList=[Q2])
Q2.defineRouting(predecessorList=[MP1, MP2, MP3], successorList=[M2])
M2.defineRouting(predecessorList=[Q2], successorList=[E])
E.defineRouting(predecessorList=[M2])


def main():
    # add all the objects in a list
    objectList = [MP1, MP2, MP3, Q2, M2, E, P1, P2, P3, P4, P5]
    # set the length of the experiment
    maxSimTime = float("inf")
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # print the results
    print(E.numOfExits)
    print(E.SysTime_E)


if __name__ == "__main__":
    main()
