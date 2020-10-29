from speaker import Speaker
from services import ServiceClass


sp = Speaker()
args = sp.dialog()
service = ServiceClass(args[0], args[1])
final = service.logic()
if final != None:
    print(final)
