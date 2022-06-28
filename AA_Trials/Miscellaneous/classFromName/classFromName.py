from manpy.simulation.Machine import Machine
# import sys
#
# name = 'Machine'
# class_inst = getattr(sys.modules[__name__], name)
# M1 = class_inst("M1", "Machine", capacity=1, processingTime={"Fixed": {"mean": 1}}, gatherIntArr=True)
# print(M1)

dotted_name = 'manpy.Machine'
from zope.dottedname.resolve import resolve
# import logging

# logger = logging.getLogger("manpy.platform")
parts = dotted_name.split(".")  # creates a list with the elements inbetween the dots
# this is added for backwards compatibility
if dotted_name.startswith("manpy"):
    class_name = dotted_name.split(".")[-1]
    new_dotted_name = "manpy.simulation.%s.%s" % (class_name, class_name)
    # logger.info(("Old style name %s used, using %s instead" % (dotted_name, new_dotted_name)))
    dotted_name = new_dotted_name
class_inst = resolve(dotted_name)
M1 = class_inst("M1", "Machine", capacity=1, processingTime={"Fixed": {"mean": 1}}, gatherIntArr=True)
print(M1)
a = {
    'nome': 'Luca',
    'cognome': 'Rossi',
    'indirizzo': {
        'città': 'Milano',
        'via': 'Via Roma',
    }
}
print('end')
