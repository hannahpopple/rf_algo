#Goal: Import data to be read by the Rolling Window
#Rolling window to gather info
#Create array to store information
#Run collected data through program to determine what kind of data it is
#and whether it is normal or anomalous

class signal(object):                                   #classify signals
    def __init__(self, properties = [0,0,0,0,0]):
        self.timestamp = properties[0]
        self.module = int (properties[1])
        self.pwr = float(properties[2])
        self.loc = properties[3]
        self.freq =float( properties[4])
        if 2401000000 <= self.freq <= 2495000000:
            self.classification = "WiFi"
        elif self.freq == 908420000:
            self.classification = "Z-Wave"
        else:
            self.classification = "Undefined"           #TODO: add RSM and LTE values
                                                        #TODO: add normal/anomalous $

    def __str__(self):
        return str(self.freq) + ", " + str(self.pwr) + ", " + str(self.loc) \
        + ", " + self.classification
    def __repr__(self):
        return str(self.freq) + ", " + str(self.pwr) + ", " + str(self.loc) \
        + ", " + self.classification

rfInfo = []                                             #create rf array
dataPoints = None                                       #create dataPoints variable

import csv
with open('rf_data.csv', 'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ",")
    for row in dataReader:
        rfInfo.append(signal(row))
        
             self.classification = "Undefined"           #TODO: add RSM and LTE values
                                                        #TODO: add normal/anomalous $

    def __str__(self):
        return str(self.freq) + ", " + str(self.pwr) + ", " + str(self.loc) \
        + ", " + self.classification
    def __repr__(self):
        return str(self.freq) + ", " + str(self.pwr) + ", " + str(self.loc) \
        + ", " + self.classification

rfInfo = []                                             #create rf array
dataPoints = None                                       #create dataPoints variable

import csv
with open('rf_data.csv', 'r') as csvfile:
    dataReader = csv.reader(csvfile, delimiter = ",")
    for row in dataReader:
        rfInfo.append(signal(row))

### Legacy
#print("Please enter all necessary data points:(frequency, power, location)")
#while dataPoints != "":
#    dataPoints = input ("").strip()
#    if "," not in dataPoints:
#       if dataPoints != "":
#            print("Use format (frequency, power, location)")
#    elif dataPoints != "":
#        rfInfo.append(signal(list(map(float, dataPoints.split(", ")))))
###

print(rfInfo[0:10])
