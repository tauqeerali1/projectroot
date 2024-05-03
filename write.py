import csv
import json
from models import NearEarthObject, CloseApproach
from helpers import datetime_to_str

def write_to_csv(results, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous'])
        writer.writeheader()
        for approach in results:
            neo = approach.neo
            writer.writerow({
                'datetime_utc': datetime_to_str(approach.time),
                'distance_au': approach.distance,
                'velocity_km_s': approach.velocity,
                'designation': neo.designation,
                'name': neo.name if neo.name else "",
                'diameter_km': neo.diameter if neo.diameter else float('nan'),
                'potentially_hazardous': "True" if neo.hazardous else "False"
            })

def write_to_json(results, filename):
    output_data = []
    for approach in results:
        neo = approach.neo
        output_data.append({
            'datetime_utc': datetime_to_str(approach.time),
            'distance_au': approach.distance,
            'velocity_km_s': approach.velocity,
            'neo': {
                'designation': neo.designation,
                'name': neo.name if neo.name else "",
                'diameter_km': neo.diameter if neo.diameter else float('nan'),
                'potentially_hazardous': bool(neo.hazardous)
            }
        })
    with open(filename, 'w') as jsonfile:
        json.dump(output_data, jsonfile)
