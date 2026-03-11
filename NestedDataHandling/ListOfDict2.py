
# print student whose age>21

students = [
    {"name":"Tanya","age":21},
    {"name":"Rahul","age":22},
    {"name":"Aman","age":23}
]
print([s["name"]for s in students if s["age"]>21])