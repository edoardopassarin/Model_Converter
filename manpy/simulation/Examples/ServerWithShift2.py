from manpy.simulation.imports import Machine, Source, Exit, Part, ShiftScheduler
from manpy.simulation.Globals import runSimulation

# define the objects of the model
S = Source(
    "S1", "Source", interArrivalTime={"Fixed": {"mean": 0.5}}, entity="manpy.Part"
)
M = Machine("M1", "Machine", processingTime={"Fixed": {"mean": 3}})
E = Exit("E1", "Exit")

# create a repeated shift pattern
shiftPattern = []
i = 0
while i < 100:
    shiftPattern.append([i, i + 5])
    i += 10
print(shiftPattern)

# create the shift
SS = ShiftScheduler(victim=M, shiftPattern=shiftPattern)

# define predecessors and successors for the objects
S.defineRouting(successorList=[M])
M.defineRouting(predecessorList=[S], successorList=[E])
E.defineRouting(predecessorList=[M])


def main(test=0):

    # add all the objects in a list
    objectList = [S, M, E, SS]
    # set the length of the experiment
    maxSimTime = 100.0
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # calculate metrics
    working_ratio = (M.totalWorkingTime / maxSimTime) * 100
    off_shift_ratio = (M.totalOffShiftTime / maxSimTime) * 100

    # return results for the test
    if test:
        return {"parts": E.numOfExits, "working_ratio": working_ratio}

    # print the results
    print(("the system produced", E.numOfExits, "parts"))
    print(("the total working ratio of the Machine is", working_ratio, "%"))
    print(("the total off-shift ratio of the Machine is", off_shift_ratio, "%"))


if __name__ == "__main__":
    main()
