from database import *

def main():
    try:
        # Get MongoDB client
        client = get_mongo_client()
        
        # Access the database and collection
        database = client["cosmetic"]
        collection = database.users
        # Fetch and display users
        results = fetch_users(collection)
        display_results(results)

    finally:
        close_mongo_client(client)

if __name__ == "__main__":
    main()