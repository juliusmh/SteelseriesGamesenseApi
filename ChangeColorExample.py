#IMPORTS
from io import StringIO
import json

#MY PYGAME SENSE MODULE
import PyGameSense

GAME = "PYGS"
COREPROPS = "C:/ProgramData/SteelSeries/SteelSeries Engine 3/coreProps.json"

#HELPER FUNCTIONS
def parse_coreprops(path):
    f = open(path, 'r')
    io = StringIO(unicode(f.read()))
    addr = json.load(io)["address"].split(":")
    return (addr[0], addr[1])

#EXAMPLE CODE
(ip, port) = parse_coreprops(COREPROPS)
gs = PyGameSense.GameSenseBridge(ip,port) #("127.0.0.1", 49157)

if(gs.is_connected):
    gs.unregister_game(GAME) #DONE TO CLEAN UP THE DATABASE
    gs.register_game(GAME , "PythonBridge", 5)

    gs.getEffects().show_rgb_rainbow(GAME, PyGameSense.MouseRival.DEVICE_TYPE, PyGameSense.MouseRival.ZONES)

    #gs.enter_heartbeat_loop(GAME)

    #gs.unregister_game(GAME) #DONE TO CLEAN UP THE DATABASE
