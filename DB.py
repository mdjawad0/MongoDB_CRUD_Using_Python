import pymongo

class DB:
    # Function for MongoDB Connection 
    def __init__(self, db="SecurityAgency", collection="guards"):
        url = "mongodb+srv://jawad:jawad123@cluster0.zsnblev.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        print("Connection Created..")
    
        self.db = client[db]
        print("DB Selected as", db)
    
        self.collection = self.db[collection]
        print("collection Selected as", collection)
 
    # Insert Operation
    def insert(self, document):
        # Insert the only one Document
        result = self.collection.insert_one(document)
        print("Security Guard Inserted with ID:", result.inserted_id)

    # Retrieve All Operation
    def query(self):
        documents = self.collection.find()
        return documents

    # Delete Operation
    def delete(self, query=None):
        result = self.collection.delete_one(query)
        print("Security Guard Deleted. Count:", result.deleted_count)
 
    # Update Operation
    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collection.update_one(query, update_query)
        print("Security Guard Updated. Count:", result.modified_count)



