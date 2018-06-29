#open and read csv files
#chunk data into 2 minute segments
#find avg power, avg time difference, and amnt of hits per chunk
### WILL BREAK if column titles exist in CSV file. Erase first line!

import csv # csv.reader
import os
import pandas as pd

def chunk(fileName, chunkNum, timeLen = 120000):
	returnList = []
	with open(fileName, 'r') as csvfile:
		dataReader = list(csv.reader(csvfile, delimiter = ","))
		try:
			start = int(dataReader[0][3].strip())
		except ValueError:
			try:
				start = float(dataReader[0][3].strip())
			except ValueError:
				print("DEBUG: Error in ", fileName, " with value \'", dataReader[0][3], "\'")
		for row in dataReader:
			timestamp = float(row[3].strip())
			if (timestamp >= (start + (timeLen * chunkNum))) and (timestamp <= (start + (timeLen * (chunkNum + 1)))):
				returnList.append([int(row[0].replace(",", "")), float(row[1]), row[2], timestamp])
		csvfile.close()
	return returnList

def avgPwr(listName):
    return sum([subList[1] for subList in listName]) / len(listName)

def avgDiff(listName):
	try:
		return (listName[-1][3] - listName[0][3]) / (len(listName)- 1)
	except:
		return 0

def getStats(fileName):
	chunkStats = [None]
	statList = []
	i, emptyChunks = 0, 0
	while emptyChunks < 25:
		chunkStats = chunk(fileName, i)
		if len(chunkStats) > 0:
			emptyChunks = 0
			statList.append([chunkStats[0][0], len(chunkStats), avgPwr(chunkStats), avgDiff(chunkStats), chunkStats[0][2], chunkStats[0][3]])
		if len(chunkStats) == 0:
			emptyChunks += 1
		i += 1
	return statList

def writeStats(infileName, outfileName):
	statList = getStats(infileName)
	#df = pd.DataFrame(statList)
	#print (df)
	with open(outfileName, 'a') as outfile:
		statWriter = csv.writer(outfile, delimiter=",")
		for list in statList:
			statWriter.writerow(list)
		#for subList in statList:
			#print(subList, file=outfile)
		#df.to_csv(outfile, header=False,index=False)



filelist = os.listdir(os.getcwd())
for file in filelist:
	if file.endswith("WifiNorm.csv"):
		writeStats(file, 'all.csv')
#infile = input("Input filename: ")
#outfile = input("Output filename: ")
#writeStats(infile, outfile)
