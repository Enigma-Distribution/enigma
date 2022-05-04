import os
import sys

from client.handler import app

os.environ["ENIGMA_FAE"] =  sys.argv[1]
os.environ["PHASE"] = sys.argv[2]
os.environ["STEP_ID"] = sys.argv[3]
os.environ["API_URL"] = "{}/worker/submit-result".format(sys.argv[4])

if sys.argv[2] == "map":
    app.run_mapper()

if sys.argv[2] == "reduce":
    app.run_reducer()

if sys.argv[2] == "shuffle":
    app.run_shuffler()
