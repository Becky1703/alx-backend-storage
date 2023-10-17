#!/usr/bin/env python3
"""Script analyses Nginx log"""
import pymongo


def print_nginx_request_logs(nginx_collection):
    """Function prints stats about Nginx requet logs"""
# MongoDB connection details
mongo_uri = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
db_name = "logs"
collection_name = "nginx"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Get the total number of documents
total_logs = collection.count_documents({})

# Count documents with specific methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}
for method in methods:
    count = collection.count_documents({"method": method})
    method_counts[method] = count

# Count documents with specific method and path
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"    method {method}: {count}")
print(status_check_count, "status check")

# Close the MongoDB connection
client.close()
