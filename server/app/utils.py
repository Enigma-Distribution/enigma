import jwt
import datetime
import requests 
import json
import ipfsApi
import os

def get_object_from_token(token, key):
    try:
        return jwt.decode(token, key, algorithms=['HS256'])
    except jwt.DecodeError as e:
        return None

def get_token_from_object(obj, key, time=None):
    try:
        if time:
            obj['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
            return jwt.encode(obj,key)
        return jwt.encode(obj,key)
    except Exception as e:
        print(e)
        return None

def read_file_content(file_link):
    # Example
    # file_link = "https://ipfs.infura.io/ipfs/QmPWfMrZijFSR5B9Q36Wy1nJ33JdGU6eitjnLETLQjLsAL"
    f = requests.get(file_link)
    return f.text

def put_content_into_file_and_upload(content):
    api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)

    file_name = "result.txt"

    # Write result in file
    f = open(file_name, "w")
    f.write(content)
    f.close()

    # add file to ipfs
    res = api.add(file_name)
    # res => {'Name': 'result.txt', 'Hash': 'QmaySg6fCyneVv8Jdi6ZvPs973qscvZUrutZUEj94KveMe', 'Size': '17'}
    # Accessing file: https://ipfs.infura.io/ipfs/QmaySg6fCyneVv8Jdi6ZvPs973qscvZUrutZUEj94KveMe
    print(res)

    # remove file from local server
    os.remove(file_name)

    return res["Hash"]