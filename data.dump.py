import pymongo 
import pandas as pd
import json

#Provide the mongodb localhost url to connect python to mongodb 
clients = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"

if __name__ == '__main__' :
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and coloumns: {df.shape}")

    #Convert dataframe into json so that we can dump these records in mongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())      # T = transform 
    print(json_record[0])

    #insert converted json record to mongo 
    clients[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

