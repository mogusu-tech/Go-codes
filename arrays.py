courses = ["MIT","Cybersecurity","Datascience"]
print(courses)
#Accessing an element in array
print(courses[1])

#Looping through an element
for course in courses:
    print("Course is",course)

#Adding a new element
courses.append("Web development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)