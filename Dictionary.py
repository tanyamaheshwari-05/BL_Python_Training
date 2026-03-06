 #dictionary are mutable ,unordered and store data in key value pair.
dict = {
    "name" : "Rutvi",
    "age" : 24,
    "cgpa" : 8.9,
    "is_adult" : True,
    "subject": ["Maths", "Science"],
    "marks":(89,90)
}
print(dict) 
print(dict["marks"]) # acess the value by using its key

# Nested dictionary
dict = {
    "name" : "Rutvi",
    "age" : 24,
    "cgpa" : 8.9,
    "is_adult" : True,
    "subject": {
        "chem":89,
        "Math":92
    }
}
print(dict["subject"]["chem"]) # access marks of chemistry.
print(list(dict.keys()))
print(list(dict.values()))
print(list(dict.items()))
print(dict.get("name"))
dict.update({"loc": "Mumbai"})
print(dict)


