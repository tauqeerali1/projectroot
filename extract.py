import csv
import json
from models import NearEarthObject, CloseApproach

def load_neos(neo_csv_path):
    neos = []
    with open(neo_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            designation = row['pdes']
            name = row['name'] if row['name'] != '' else None
            diameter = float(row['diameter']) if row['diameter'] != '' else None
            hazardous = True if row['pha'] == 'Y' else False
            neo = NearEarthObject(designation, name, diameter, hazardous)
            neos.append(neo)
    return neos

def load_approaches(cad_json_path):
    approaches = []
    with open(cad_json_path) as jsonfile:
        data = json.load(jsonfile)
        for record in data['data']:
            time = record[3]
            distance = float(record[4])
            velocity = float(record[7])
            designation = record[5]
            neo = NearEarthObject(designation, "", None, None)
            approach = CloseApproach(time, distance, velocity, neo)
            approaches.append(approach)
    return approaches
