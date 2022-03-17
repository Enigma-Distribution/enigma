import imp
import os
import requests
import os
from python.main import sendHash

phase = os.getenv("PHASE")
step_id = ""
hash = sendHash()
url = 'http://127.0.0.1:5000/worker/submit-result'
params = {"phase" : phase, "step_id": step_id, "result_file_id": hash}
r = requests.post(url, params=params)
