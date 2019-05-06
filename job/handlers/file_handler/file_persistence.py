import json
import csv
from bson.json_util import dumps

def save_from_mongodb_to_tsv(collection):
    json_data = json.loads(dumps( 
        collection.find().sort(
            [("message_created_at",pymongo.ASCENDING),
            ("author_created_at",pymongo.ASCENDING)]) 
    ))

    with open('output.tsv', 'w') as output_file:
        dict_writer = csv.DictWriter(
            output_file,
            sorted( json_data[0].keys() ),
            delimiter='\t')
        
        dict_writer.writeheader()
        dict_writer.writerows(json_values)