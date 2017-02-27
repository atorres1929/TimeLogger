import os
def checkTime(log):
    with open(log) as file:
        lines = file.readlines()
        last = lines[-1]
        file.seek(0)
        totalTime = 0
        latestSession = 0
        for line in file:
            splice = line.split("::")
            if ("not running" in splice[0] and last != line):
                latestSession = 0
                continue
            else:
                latestSession += 1
                totalTime += 1
    return [totalTime, latestSession]
    
if __name__ == "__main__":
    dir = input("Enter the directory containing log files: ")
    #EDIT THIS PATH TO CHANGE WHERE LOGS ARE READ FROM
    for file in os.listdir(dir):
        if (file.endswith(".log")):
            result = checkTime(os.path.join(dir, file))
            time = result[0]
            latest = result[1]
            splice = file.split("-")
            print(splice[0]+" Total Time in Minutes: " + str(time))
            print(splice[0]+" Total Time in Hours: "+str(int(time/60))+":"+(str(int(time%60))))
            print(splice[0]+" Latest session: " + str(int(latest/60))+":"+(str(int(latest%60))))
	
