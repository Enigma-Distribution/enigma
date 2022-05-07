import sys
import json
import os

from client.handler import app


# os.environ["ENIGMA_FAE"] =  sys.argv[1]
# os.environ["PHASE"] = sys.argv[2]
# os.environ["STEP_ID"] = sys.argv[3]
# os.environ["API_URL"] = sys.argv[4]

def json_data(filename='data.json'):
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data
        

def append_and_write(taskName, taskData):
    data = json_data(filename='data.json')
    data[taskName] = taskData 
    json_object = json.dumps(data, indent = 1)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)


append_and_write("ENIGMA_FAE", sys.argv[1])
append_and_write("PHASE", sys.argv[2])
append_and_write("STEP_ID", sys.argv[3])
append_and_write("API_URL", sys.argv[4])

if sys.argv[2] == "map":
    app.run_mapper()

if sys.argv[2] == "reduce":
    app.run_reducer()

if sys.argv[2] == "shuffle":
    app.run_shuffler()
