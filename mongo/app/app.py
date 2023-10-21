from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

#Connecting to mongodb 
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_default_database()
#Connecting to collection called "mongo" inside this db
collection = db.get_collection("mongo")

#Creating an endpoint that will be creating key-value pairs based on data from post request body
@app.route('/create', methods=['POST'])
def create_key_value():
    data = request.get_json()
    #Getting the key and value from the post request body
    key = data.get('key')
    value = data.get('value')
    #Inserting this key value pair into our collection
    collection.insert_one({'key': key, 'value': value})
    return jsonify({'message': 'Key-Value pair created successfully'})

#Creating an endpoint, that will be updating a value for indicated key
@app.route('/update/<key>', methods=['PUT'])
def update_key_value(key):
    data = request.get_json()
    #Getting the new value from the put request body
    new_value = data.get('value')
    #Updating the key with this value inside our collection
    collection.update_one({'key': key}, {'$set': {'value': new_value}})
    return jsonify({'message': 'Key-Value pair updated successfully'})

#This endpoint will be getting a key and return the its value in response
@app.route('/read/<key>', methods=['GET'])
def read_key_value(key):
    result = collection.find_one({'key': key})
    #We return the info about this key if we find it in our collection
    if result:
        return jsonify({'key': result['key'], 'value': result['value']})
    else:
        return jsonify({'message': 'Key not found'})

#Running the app on port 8080

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
