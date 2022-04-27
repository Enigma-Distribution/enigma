import sys
from distutils.command.upload import upload
# from modules.unzipper import unzip
# from modules.utils import run_if_setup_file_exists
import ipfsUpload
import requests

from client.handler import app

hash = ''

if sys.argv[2] == "map":
    map_data = app.run_mapper()
    print('map_data', map_data)
    hash = ipfsUpload(map_data)


if sys.argv[2] == "reduce":
    reduce_data = app.run_reducer()
    print('reduce_data', reduce_data)
    hash = ipfsUpload(reduce_data)


if sys.argv[2] == "shuffle":
    shuffle_data = app.run_shuffler()
    print('shuffle_data', shuffle_data)
    hash = ipfsUpload(shuffle_data)

phase = sys.argv[2]
step_id = sys.argv[3]
url = "{}/worker/submit-result".format(sys.argv[4])
params = {"phase" : phase, "step_id": step_id, "result_file_id": hash}
r = requests.post(url, params=params)