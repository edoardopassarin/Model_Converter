# routingFileName = input("Give the path to the routing txt file:\n")     # get the file name
# routingFile = open(routingFileName, "r")            # open the file
# routingContent = routingFile.read()                 # read the content of the file
# routingFile.close()                                 # close the file
# routingList = routingContent.split("\n")
# test = str(int(routingList[1]))
# print("Q" + test)
import json
import manpy.simulation.Globals as Globals


file = open("test_CS.json", "r")
fileread = file.read()
json_data = json.loads(fileread)
nodes = json_data["graph"]["node"]
for (element_id, element) in list(nodes.items()):
    element["id"] = element_id
    wip = element.get("wip", [])
    for entity in wip:
        entityClass = entity.get("_class", None)
        entityType = Globals.getClassFromName(entityClass)
        inputDict = dict(entity)
        inputDict.pop("_class")
        print(entityClass)
        #print(inputDict)
        entity = entityType(**inputDict)
        #print(entity)
