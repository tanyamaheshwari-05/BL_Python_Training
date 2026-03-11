#  Convert a Python dictionary into JSON format.

import json

data={
    "name":"Tanya",
    "email":"abc@gmail.com",
    1:1
}
json_data= json.dumps(data)
print(json_data)