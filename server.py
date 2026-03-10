from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

mongo_password = os.getenv('MONGO_CLUSTER_PASSWORD')
uri = f"mongodb+srv://Marcoco:{mongo_password}@marccluster.dv9yckd.mongodb.net/?appName=MarcCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["casino_server"]
    collection = db["player"]
    document = {"name": "Hans", "credits": 100}

    result = collection.insert_one(document)
except Exception as e:
    print(e)