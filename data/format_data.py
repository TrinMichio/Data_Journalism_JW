import json


f1 = open("data/data_cleaned.csv", "r")
lines = f1.readlines()

dictionary ={}

dictionary['years'] = [int(i.replace('\n', '')) for i in lines[0].split(',')[1:]]

for line in lines[1:]:
    vals = line.split('","')
    vals = vals[0].split(',"') + vals[1:]
    area = vals[0].strip('.').strip('\'')
    vals = [int(i.strip('.').strip('\n').strip('\"').replace(',', '')) for i in vals[1:]]
    dictionary[area] = vals
    


f1.close()

#Save the json object to a file
f2 = open("data/data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
