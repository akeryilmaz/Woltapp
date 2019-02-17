import sys
import csv

def ReadLocation(location):
    '''reads csv file for a given location.
    Input: String. name of the location(also the name of the csv file) 
    Output: List of integers. location_id's of restaurants.'''
    path = location + ".csv"
    location_ids = []
    with open(path, 'r') as csvFile:
        line_count = 0
        reader = csv.reader(csvFile)
        for row in reader:
            if line_count != 0:
                location_ids.append(int(row[0]))
            line_count += 1
    return location_ids

def ReadPickupTimes(location_id):
    '''reads csv file for a given location_id.
    Input: Integer. location_id of a restaurant
    Output: List of tuple of integers. (hour, pickup_time) location_id's of restaurants.'''
    pickup_times = []
    with open("pickup_times.csv", 'r') as csvFile:
        line_count = 0
        reader = csv.reader(csvFile)
        for row in reader:
            if line_count != 0:
                if location_id == row[0]:
                    pickup_times.append((int(row[1]), int(row[2])))
            line_count += 1
    return pickup_times

def FindMedian():

if __name__ == "__main__":
    arguments = sys.argv
    location_ids = ReadLocation(arguments[0])
    for location_id in location_ids:
        pickup_times = ReadPickupTimes(location_id)
        # TODO: Calculate median
