student_record={
    id1:{"name":"Jack","age":"9","class":"2b","subject":"Maths"},
    id2:{"name":"felix","age":"13","class":"1a","subject":"science"},
    id3:{"name":"felix","age":"13","class":"1a","subject":"science"}, 
    }
result={}
seen_keys=[] 

for student_id, details in student_record.items():
    unique_key = (details["name"], details["class"], details["subject"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)
    
