#  Write JSON data into a file.
import json

data = {
    "name": "Tanya",
    "age": 21
}
with open("D:\Apexon\BL_Python_Training\Json\data.json","w") as file: 
    json.dump(data,file)
print("Data written successfully")