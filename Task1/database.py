import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
# making a client to connect to db
def get_mongo_client():
    try:
        mongo_uri = os.getenv("MONGO_DB_URI")
        client = pymongo.MongoClient(mongo_uri)
    except Exception as e:
        print(f"Some error occured {e}")
        
    return client

# fetching data base collection
def fetch_users(collection):
    # Retrieve documents where isActive is true
    query = {"isActive": True}
    results = collection.find(query)
    
    return results

# Display the results in a formatted way
def display_results(results):
    for result in results:
        print("User ID:", result["_id"])
        print("Username:", result["username"])
        print("Email:", result["email"],"\n")

def close_mongo_client(client):
    client.close()