# https://pypi.org/project/ipfs-api/
import ipfsApi
import os

def uploadToIPFS(content):

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
    # os.remove(file_name)

    return res["Hash"]

# uploadToIPFS("Hello this is file content which will be uploaded to ipfs")