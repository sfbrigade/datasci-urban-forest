""" Given an existing CSV with the (lat, long) of every tree,
    write the new, "derived" neighborhood to the CSV
"""
from __future__ import print_function
import csv
import time
from LatLong import LatLong

with open('combined_tree_data_with_header.csv', 'r') as f:
    out_file = open('combined_tree_data_with_header_with_neighborhood.csv', 'w')
    out_csv = csv.writer(out_file)
    read_csv = csv.reader(f)
    for row in read_csv:
        longitude = row[16]
        latitude = row[17]
        l = LatLong(latitude=latitude, longitude=longitude)
        try:
            neighborhood = l.get_neighborhood()
        except:
            neighborhood = 'None'
        print("%s, %s, %s" % (latitude, longitude, neighborhood))
        row.append(neighborhood)
        out_csv.writerow(row)

        # Be nice to the API
        time.sleep(0.5)

out_file.close()
