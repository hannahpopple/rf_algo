#open and read csv files
#chunk data into 2 minute segments
#find avg power, avg time difference, and amnt of hits per chunk
### WILL BREAK if column titles exist in CSV file. Erase first line!

import csv # csv.reader

def chunk(fileName, chunkNum, timeLen = 120000):
    """Returns a subset of given CSV file as a list of sublists
based on timeLen (in ms)"""
    returnList = []
    with open(fileName, 'r') as csvfile:
        dataReader = csv.reader(csvfile, delimiter = ",")
        start = int(next(dataReader)[3])
        for row in dataReader:
            timestamp = int(row[3])
            if (timestamp >= (start + (timeLen * chunkNum))) and (timestamp <= (start + (timeLen * (chunkNum + 1)))):
                returnList.append([int(row[0].replace(",", "")), float(row[1]), row[2], timestamp])
        csvfile.close()
    return returnList

def avgPwr(listName):
    """Returns the average power (index = 1) of a chunk"""
    return sum([subList[1] for subList in listName]) / len(listName)

def avgDiff(listName):
    """Returns the average difference of time (index = 3)
of a chunk"""
    return (listName[-1][3] - listName[0][3]) / (len(listName)- 1)

def getStats(fileName):
    """Returns a list of stats about a CSV file as broken up
by chunks
[Chunk number, Hits, Average power, Average time diff]"""
    chunkStats = [None]
    statList = []
    i = 0
    while len(chunkStats) != 0:
        chunkStats = chunk(fileName, i)
        if len(chunkStats) > 0:
            statList.append([i, len(chunkStats), avgPwr(chunkStats), avgDiff(chunkStats)])
        i += 1
    return statList

def writeStats(infileName, outfileName):
    """Writes outfileName with chunk stats from infileName.
Does NOT check if outfileName already contains data.
WILL overwrite data if not careful."""
    statList = getStats(infileName)
    with open(outfileName, 'w', newline = '') as csvfile:
        dataWriter = csv.writer(csvfile, delimiter = ",")
        for row in statList:
            dataWriter.writerow(row)
        csvfile.close()
        

""" Legacy
### Uncomment and add filenames between '' when files are in the same dir as this file
normalWifi = getStats('Normal Wi-Fi Data v3.csv')
##jammingWifi = getStats('') 
##normalZwave = getStats('')
##jammingZwave = getStats('')
##replayZwave = getStats('')
"""

writeStats('Normal Wi-Fi Data v3.csv', 'Normal Wi-Fi Stats.csv')
