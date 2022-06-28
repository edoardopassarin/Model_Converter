from manpy.simulation.imports import Source, Queue, Machine, Exit       # We are imporing the ManPy objects
from manpy.simulation.Globals import runSimulation          # We are importing the globals.runsimulation method

# define the objects of the model
S = Source(
    "S1", "Source", interArrivalTime={"Exp": {"mean": 0.5}}, entity="manpy.Part"
)
Q = Queue("Q1", "Queue", capacity=10)
M1 = Machine("M1", "Machine", processingTime={"Exp": {"mean": 0.25}})
M2 = Machine("M2", "Machine", processingTime={"Exp": {"mean": 0.25}})
E = Exit("E1", "Exit")

# define predecessors and successors for the objects
S.defineRouting(successorList=[M1])
M1.defineRouting(predecessorList=[S], successorList=[Q])
Q.defineRouting(predecessorList=[M1], successorList=[M2])
M2.defineRouting(predecessorList=[Q], successorList=[E])
E.defineRouting(predecessorList=[M2])


def main(test=0):           # We define the main function, which is the program to be run
    # add all the objects in a list
    objectList = [S, M1, Q, M2, E]
    # set the length of the experiment
    maxSimTime = 1440.0     # Minutes
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # calculate metrics
    working_ratio_M1 = (M1.totalWorkingTime / maxSimTime) * 100
    working_ratio_M2 = (M2.totalWorkingTime / maxSimTime) * 100

    # return results for the test
    if test:
        return {"parts": E.numOfExits, "working_ratio of M1": working_ratio_M1, "working_ratio of M2": working_ratio_M2}

    # print the results
    print(("the system produced", E.numOfExits, "parts"))
    print(("the total working ratio of Machine 1 is", working_ratio_M1, "%"))
    print(("the total working ratio of Machine 2 is", working_ratio_M2, "%"))


if __name__ == "__main__":      # This line is used to execute the main function which runs the program
    main()
