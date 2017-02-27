import subprocess
from datetime import datetime
import time
import os

class TimeLogger(object):

    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    
    #Change this variable to log whatever you want logged
    #Process names need to be the name of the process found in Task Manager -> Details
    #Or you can find it in Task Manager -> Processes -> Right Click Application -> Properties
    #e.g. "Google Chrome" will not work, "chrome" will
    #Remember to separate items in the array by commas
    APPS_TO_LOG = ["chrome"] #"chrome" is an example
    
    #Edit this to change where logs are stored
    PATH_TO_LOGS = "C:\\Python Time Logger\\" 
    
    #Amount of time between checks
    TIME_INTERVAL = 60

    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    
    """ Gets the processes currently running and puts them into a byte string array.
    :return Byte String array with all processes running
    """
    def listRunningApps(self):
        cmd = "WMIC PROCESS GET CAPTION"
        proc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
        processes = []
        for line in proc.stdout:
            line = line.decode(encoding = "UTF-8")
            process = line.split(".")[0]
            processes.append(process)
        processes = sorted(set(processes), key=str.lower)
        proc.kill()
        return processes
        
    """ Logs every minute that the apps are open 
    :param apps: An array that contains the apps that are to be logged
    """
    def logTime(self):
        while True:
            runningApps = TimeLogger.listRunningApps(self) 
            for app in TimeLogger.APPS_TO_LOG:
                appOpen = app in runningApps
                try:
                    file = open(TimeLogger.PATH_TO_LOGS + app + ".log", "a+")
                except OSError:
                    break   #Some stupid thing dealing with how process names are collected
                            #Ignoring it is the easiest solution
                    
                date = datetime.now()
                log = ""
                if (appOpen):
                    log += app+" running :: "+str(date.year)+"-"+str(date.month)+"-"+str(date.day)+"::"+str(date.hour)+":"+str(date.minute)+"\n"
                    print(log)
                    file.write(log)
                    file.close()
                elif not appOpen:
                    log += app+" is not running :: "+str(date.year)+"-"+str(date.month)+"-"+str(date.day)+"::"+str(date.hour)+":"+str(date.minute)+"\n"
                    print(log)
                    file.write(log)
                    file.close()
                    
            time.sleep(TimeLogger.TIME_INTERVAL)

if __name__ == "__main__":
    if not os.path.isdir(TimeLogger.PATH_TO_LOGS):
        os.mkdir(TimeLogger.PATH_TO_LOGS)
    TimeLogger().logTime()
