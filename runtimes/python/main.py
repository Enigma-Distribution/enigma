from distutils.command.upload import upload
import os
from random import shuffle
from modules.unzipper import unzip
from modules.utils import run_if_setup_file_exists
import ipfsUpload
import requests


path_to_zip = os.getenv("PATH_TO_ZIP")
unzip(path_to_zip)
run_if_setup_file_exists()

from client.handler import app

hash = ''

if os.getenv("PHASE") == "ENIGMA.MAP":
    map_data = app.run_mapper()
    print('map_data', map_data)
    hash = ipfsUpload(map_data)


if os.getenv("PHASE") == "ENIGMA.REDUCE":
    reduce_data = app.run_reducer()
    print('reduce_data', reduce_data)
    hash = ipfsUpload(reduce_data)


if os.getenv("PHASE") == "ENIGMA.SHUFFLE":
    shuffle_data = app.run_shuffler()
    print('shuffle_data', shuffle_data)
    hash = ipfsUpload(shuffle_data)

phase = os.getenv("PHASE")
step_id = os.getenv("STEP")
url = os.getenv("SERVER_URL") + "/worker/submit-result"
params = {"phase" : phase, "step_id": step_id, "result_file_id": hash}
r = requests.post(url, params=params)