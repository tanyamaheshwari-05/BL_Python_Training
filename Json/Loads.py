# Convert JSON data back into Python dictionary.
import json

json_data='''{
    "name":"Tanya",
    "email" :"abc@gmail.com",
    "1":1
}'''

data= json.loads(json_data)
print("Python dictionary : ",data)