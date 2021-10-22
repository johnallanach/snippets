"""a simple program to fetch walk scores in Guelph ON"""
import csv
import random
import requests
import time
import urllib

from get_coords import get_coords
from config import WALKSCORE_API


def append_to_csv_file(rows):
    output_file = "/home/pi/Documents/Projects/walkscore/data/guelphwalkscores.csv"
    with open(output_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def get_address_score(input_address):

    address_to_fetch = urllib.quote(input_address)
    try:
        lat, lon = get_coords(address_to_fetch)
        data_url = data_url = 'https://api.walkscore.com/score?format=json&address=' + address_to_fetch + '&lat=' + lat + '&lon=' + lon + '&transit=1&bike=1&wsapikey=' + WALKSCORE_API
        res = requests.get(url=data_url)
        response_data = res.json()

        status = response_data["status"]

        try:   
            walkscore = response_data["walkscore"]
        except: 
            walkscore = 'None'
        try:
            transitscore = response_data["transit"]['score']
        except: 
            transitscore = 'None'
        try: 
            bikescore = response_data["bike"]['score']
        except:
            bikescore = 'None'
    except:
        status = 1
        walkscore = 'None'
        transitscore = 'None'
        bikescore = 'None'

    return walkscore, transitscore, bikescore, status


def main():
    
    #compile list of Guelph addresses
    address_list = []
    file_path = "/home/pi/Documents/Projects/walkscore/data/guelphaddresses.csv"
    with open(file_path) as file:
        addresses = csv.reader(file)
        next(addresses, None)
        for row in addresses: 
            address = row[0]
            address_list.append(address)

    processed_address_list = []

    for i in range(1, len(address_list)):
        address_to_process = random.choice(address_list)
        walkscore, transitscore, bikescore, status = get_address_score(address_to_process)
        if status == 1:
            entry = [address_to_process, walkscore, transitscore, bikescore]
            processed_address_list.append(entry)
            address_list.remove(address_to_process)
            status_update = "i= " + str(i) + ": " + str(address_to_process)
            print(status_update)
            time.sleep(20)     #throttle requests to not exceed 5000 API calls per day
        elif status == 40:
            time.sleep(3600) 
            walkscore, transitscore, bikescore, status = get_address_score(address_to_process)
            entry = [address_to_process, walkscore, transitscore, bikescore]
            processed_address_list.append(entry)
            address_list.remove(address_to_process)
        
        if (100 % i) == 0:
            append_to_csv_file(processed_address_list)


if __name__ == '__main__':
    main()


"""
HTTP Response	    Status Code	    Description
200	                1	            Walk Score successfully returned.
200	                2	            Score is being calculated and is not currently available.
404	                30	            Invalid latitude/longitude.
500 series	        31	            Walk Score API internal error.
200	                40	            Your WSAPIKEY is invalid.
200	                41	            Your daily API quota has been exceeded.
403	                42	            Your IP address has been blocked.
"""
