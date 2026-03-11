# Read JSON data from a file.

import json



with open("D:\Apexon\BL_Python_Training\Json\data.json", "r")as file:
    data= json.load(file)
print("Data from file : ",data)