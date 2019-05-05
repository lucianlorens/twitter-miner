
import json
import csv
from bson.json_util import dumps

def save_from_mongodb_to_tsv(self, collection):
    json_data = json.loads(dumps( 
        collection.find().sort(
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
    print('File saved')