import sys
import json
import os


os.environ["ENIGMA_FAE"] =  sys.argv[1]
os.environ["PHASE"] = sys.argv[2]
os.environ["STEP_ID"] = sys.argv[3]
os.environ["API_URL"] = sys.argv[4]
os.environ["AUTH_TOKEN"] = sys.argv[5]

from client.handler import app

if os.getenv("PHASE") == "map":
    app.run_mapper()

if os.getenv("PHASE") == "reduce":
    app.run_reducer()

if os.getenv("PHASE") == "shuffle":
    app.run_shuffler()
