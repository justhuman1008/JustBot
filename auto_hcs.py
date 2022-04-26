import json
from hcskr import selfcheck

from setting import hcs_path

json_object = json.load(open(hcs_path,encoding="utf_8"))
for k, v in json_object.items():
    if v[0]['Auto_check'] == "O":
        Nickname = v[0]['Nickname']
        Name = v[0]['Name']
        Birthday = v[0]['Birthday']
        Area = v[0]['Area']
        School = v[0]['School']
        School_lv = v[0]['School_lv']
        Password = v[0]['Password']
        hcskr_result = selfcheck(Name, Birthday, Area, School, School_lv, Password)