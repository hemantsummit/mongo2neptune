import json
import csv

# load the JSON data
with open('data.json') as json_file:
    data = json.load(json_file)

data_file = []

for x in data:
    appNum = x["requestData"]["applicationNumber"]

    for y in x["requestData"]["entities"]:
        valNeed = y
        valNeed["applicationNumber"] = appNum
        data_file.append(valNeed)

data = data_file

def flatten_json(nested_json):
    """
        Flatten the json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

# create a new CSV file
with open('data.csv', 'w', newline='') as csv_file:
    fieldnames = list(flatten_json(data[0]).keys())
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        flat_row = flatten_json(row)
        writer.writerow(flat_row)
