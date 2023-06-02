import csv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputFile', '-if', required=True, help='Input file of cancellations. In CSV format.')
parser.add_argument('--month', '-m', required=True, help='Month to check for cancellations.')

args = parser.parse_args()
file = args.inputFile
month = args.month

def processMonth(file, month):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        eventIDs = []
        users = []
        outputs = {}

        #Parse CSV and add to lists
        for row in reader:
            #Gets cancellations in a given month
            search = re.search(f'\d+\/0{month}', row['Cancel Date']) or re.search(f'\d+\/{month}', row['Cancel Date'])
            if search:
                #Adds Event ID and Username to separate lists
                eventIDs.append(row['Event ID'])
                users.append(row['Username'])

        #Merge event ID and users lists to one dictionary
        for k, v in zip(users, eventIDs):
            outputs.setdefault(k, []).append(v)

        #Get counts of cancellations per user and sorts
        count = [(key, len(value)) for key, value in outputs.items()]
        count.sort(key= lambda x: x[1], reverse=True)
    
    #Append results to CSV
    #with open('export.csv', 'a') as a:
        #write = csv.writer(a)

   #write.writerows(count)

    print(f'Number of unique users: {len(outputs.keys())}')
    print(count)

processMonth(file, month)
    
