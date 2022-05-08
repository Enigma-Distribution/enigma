import os
from enigpy.ipfsUpload import uploadToIPFS as ipfsUpload
import json
import requests
# import json

# def json_data():
#     with open('/runtime/data.json') as json_file:
#         data = json.load(json_file)
#         return data


def process_post_result(ipfs_hash_of_file):
    url = "{}/worker/submit-result".format(os.getenv('API_URL'))
    params = {"phase" : os.getenv('PHASE'), "step_id": os.getenv('STEP_ID'), "result_file_id": ipfs_hash_of_file}
    requests.post(url, params=params)

class EnigmaMapper:
    def __init__(self):
        self.return_array_of_tuples = []

    def map(self):
        raise NotImplementedError

    def get_normalise_file_ref(self):
        string = ""
        for each in self.return_array_of_tuples:
            string += str(each[0]) + ", " + str(each[1]) + " ,"
        string = string[:-2]
        hash = ipfsUpload(string)
        return hash

    def run(self):
        self.map()
        print("request to mapper")
        process_post_result(self.get_normalise_file_ref())


class EnigmaReducer:
    def __init__(self):
        self.return_dict = dict()
    
    def get_normalise_file_ref(self):
        return ipfsUpload(json.dumps(self.return_dict))

    def reduce(self):
        raise NotImplementedError

    def run(self):
        self.reduce()
        print("request to reducer")
        process_post_result(self.get_normalise_file_ref())


class EnigmaShuffler:
    def __init__(self):
        self.return_dict = dict()

    def get_normalise_file_ref(self):
        return ipfsUpload(json.dumps(self.return_dict))

    def create_key(self, key):
        if not key in self.return_dict:
            self.return_dict[key] = []

    def update_to_array_via_key(self, key, value):
        if not key in self.return_dict:
            self.create_key(key)
            self.update_to_array_via_key(key, value)
            return
        self.return_dict[key].append(value)
        
    def shuffle(self):
        raise NotImplementedError
    
    def run(self):
        self.shuffle()
        print("request to shuffler")
        process_post_result(self.get_normalise_file_ref())


class EnigmaApp:
    def __init__(self):
        pass

    def set_mapper_class(self, cls):
        if(issubclass(cls, EnigmaMapper)):
            self.mapper = cls()
            return

    def set_reducer_class(self, cls):
        if(issubclass(cls, EnigmaReducer)):
            self.reducer = cls()
            return

    def set_shuffler_class(self, cls):
        if(issubclass(cls, EnigmaShuffler)):
            self.shuffler = cls()
            return

    def run_mapper(self):
        self.mapper.run()
    
    def run_reducer(self):
        self.reducer.run()

    def run_shuffler(self):
        self.shuffler.run()