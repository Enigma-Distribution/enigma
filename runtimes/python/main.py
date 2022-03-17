from distutils.command.upload import upload
import os
from random import shuffle
from modules.unzipper import unzip
from modules.utils import run_if_setup_file_exists
import ipfsUpload

path_to_zip = os.getenv("PATH_TO_ZIP")
unzip(path_to_zip)
run_if_setup_file_exists()

from client.handler import app

hash = ''

if os.getenv("PHASE") == "ENIGMA.MAP":
    map_data = app.run_mapper()
    hash = ipfsUpload(map_data)


if os.getenv("PHASE") == "ENIGMA.REDUCE":
    reduce_data = app.run_reducer()
    hash = ipfsUpload(reduce_data)


if os.getenv("PHASE") == "ENIGMA.SHUFFLE":
    shuffle_data = app.run_shuffler()
    hash = ipfsUpload(shuffle_data)

def sendHash():
    return hash