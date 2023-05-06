import json
from pathlib import Path



def getdata(key):
    json_file_path = Path(__file__).parent.parent.joinpath("resources").joinpath("config.json")
    with open(json_file_path, 'r') as datafile:
        testdata = json.load(datafile)
        return testdata[key]

# Utility().getdata()