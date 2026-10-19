
student_data = {
    "id1": {"name": "Felix", "class": "1a", "subject": "math, science"},
    "id2": {"name": "Aditya", "class": "1a", "subject": "english, math, science"},
    "id3": {"name": "Abhinav", "class": "1a", "subject": "math, science"},
    "id4": {"name": "Cassio", "class": "2b", "subject": "spanish,english"}
}
 
print("Student Records:")
print(student_data)

 
print("Details of id1:")
print(student_data.get("id1", "Not Found"))
 

print("Details of id5:")
print(student_data.get("id5", "Not Found"))
 

student_data["id5"] = {
    "name": "Anson",
    "class": "2a",
    "subject": "english,maths"
}
 

print("The student's data after adding id5:")
print(student_data)


student_data["id2"]["subject"] = "english, math, science"
 

print("After updating id2 subject:")
print(student_data)
 

cleaned_data = {}
seen_records = []
 
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
 
student_data = cleaned_data
 

print("After removing duplicate records:")
print(student_data)
 

removed_student = student_data.pop("id2", "Student not found")
 

print("Removed student:", removed_student)

 
print("Total student records left in the student record is:", len(student_data))
 

for student_id, details in student_data.items():
    print(student_id, ":", details)
 