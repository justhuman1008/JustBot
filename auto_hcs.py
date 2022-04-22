from hcskr import asyncSelfCheck
import json

file_path = "hcs_info.json"

with open(file_path, "r", encoding="utf_8") as json_file:
    json_data = json.load(json_file)