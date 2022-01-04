from datetime import datetime
from KSVE.GLOBAL import *
_LOGLEVEL = [0]
_DEBUG = [0]

def initLog(loglevel, debugmode):
    _LOGLEVEL[0] = loglevel
    _DEBUG[0] = debugmode
    loginfo("KSVE Logger initialized")


def loginfo(msg):
    if _DEBUG[0]:
        if _LOGLEVEL[0] == "INFO":
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"INFO    : {dt_string} : {msg}")

def logwarning(msg):
    if _DEBUG[0]:
        if _LOGLEVEL[0] == "INFO" or _LOGLEVEL[0] == "WARNING":
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"WARNING : {dt_string} : {msg}")

def logerror(msg):
    if _DEBUG[0]:
        if _LOGLEVEL[0] == "INFO" or _LOGLEVEL[0] == "WARNING" or _LOGLEVEL[0] == "ERROR":
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print(f"ERROR   : {dt_string} : {msg}")