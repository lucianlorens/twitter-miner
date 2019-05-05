
import json
import csv
from bson.json_util import dumps

json_data = json.loads(dumps( 
    col.find().sort(
        [("message_created_at",pymongo.ASCENDING),
         ("author_created_at",pymongo.ASCENDING)]) 
))

with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(
        output_file,
        sorted( json_data[0].keys() ),
        delimiter='\t')
    
    dw.writeheader()
    dw.writerows(json_values)