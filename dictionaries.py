# Dictionaries

#Dictionaries use a key/value pairs

#key = a reference to a particular object
#value = data storage mechanism you want to use

# Create a dictionary

student_1 = {
    "name" : "Belal",
    "stream" : "Devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"]
}
#Access data within a dictionary

print(student_1["stream"])
#Access particular parts of the list
print(student_1["completed_lesson_names"][1])

# changing a value in a dictionary

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Removing items from a dictionary

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

#get the value

car = {
    "make": "Ford",
    "model": "Fiesta",
    "colour": "Blue",
    "year": "2011",
}

print(car)
car["condition"] = "Moderate"

print(car)
