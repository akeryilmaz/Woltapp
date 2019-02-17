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

def ReadPickupTimes(location_id, date):
    '''reads csv file for a given location_id and given date.
    Input: location_id: Integer. location_id of a restaurant
            date: String. query date
    Output: List of tuple of integers. (hour, pickup_time)'''
    pickup_times = []
    with open("pickup_times.csv", 'r') as csvFile:
        line_count = 0
        reader = csv.reader(csvFile)
        for row in reader:
            if line_count != 0:
                if location_id == int(row[0]) and date == row[1].split("T")[0]:
                    pickup_times.append((int(row[1].split("T")[1].split(":")[0]), int(row[2])))
            line_count += 1
    return pickup_times

def FindMedian(pickup_times, hour_range):
    '''finds median for given pickup times and hour range
    Input: pickup_times: List of tuple of integers. (hour, pickup_time)
           hour_range: Tuple of ıntegers. (lower bound, upper bound)
    Output: Float. Median OR None if no pickup time exist'''
    pickups = []
    count = 0
    for pickup_time in pickup_times:
        # append only if order is in the given range
        if pickup_time[0] >= hour_range[0] and pickup_time[0] < hour_range[1]:
            pickups.append(pickup_time[1])
            count += 1
    if pickups == []:
        return None
    # Sort the pickup times to find median
    pickups.sort()
    # If there are even number of elements, median is the average of two elements in the middle
    if count % 2 == 0:
        return (pickups[int(count/2)] + pickups[int(count/2)-1])/2
    # If there are odd number of elements, median is the element in the middle
    else:
        return float(pickups[int(count/2)])

if __name__ == "__main__":
    arguments = sys.argv
    location_ids = ReadLocation(arguments[1])
    hour_range = (int(arguments[3].split("-")[0]), int(arguments[3].split("-")[1]))
    date = (arguments[2])
    print("location_id , median")
    for location_id in location_ids:
        pickup_times = ReadPickupTimes(location_id, date)
        median = FindMedian(pickup_times, hour_range)
        print (location_id, ",", median)