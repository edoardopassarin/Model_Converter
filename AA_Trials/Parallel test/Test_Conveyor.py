from manpy.simulation.imports import Source, Queue, Machine, Exit
from manpy.simulation.TimedConveyor import TimedConveyor
from manpy.simulation.Globals import runSimulation

# define the objects of the model
S = Source("S1", "Source", interArrivalTime={"Fixed": {"mean": 1}}, entity="manpy.Part")
Q1 = Queue("Q1", "Queue", capacity=1000)
M1 = Machine("M1", "Machine", capacity=1, processingTime={"Fixed": {"mean": 4}}, gatherIntArr=True)
C = TimedConveyor("C1", "Conveyor", capacity=1, length=24000.001, speed=100)      # 4 min
Q2 = Queue("Q2", "Queue", capacity=1)
M2 = Machine("M2", "Machine", capacity=1, processingTime={"Fixed": {"mean": 5}})
E = Exit("E1", "Exit", gatherSysTimeEx=True)

# define predecessors and successors for the objects
S.defineRouting(successorList=[Q1])
Q1.defineRouting(predecessorList=[S], successorList=[M1])
M1.defineRouting(predecessorList=[Q1], successorList=[C])
C.defineRouting(predecessorList=[M1], successorList=[Q2])
Q2.defineRouting(predecessorList=[C], successorList=[M2])
M2.defineRouting(predecessorList=[Q2], successorList=[E])
E.defineRouting(predecessorList=[M2])


def main():
    # add all the objects in a list
    objectList = [S, Q1, M1, C, Q2, M2, E]
    # set the length of the experiment
    maxSimTime = 100
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # print the results
    print(("the system produced", E.numOfExits, "parts"))
    print(M1.IntArr)
    print(M1.totalBlockageTime)


if __name__ == "__main__":
    main()
