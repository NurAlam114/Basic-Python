SectionC = [
    {"ID": "221311082", "Name": "Esha", "CGPA": 3.86, "City": "Rajshahi"},
    {"ID": "221311083", "Name": "Umme Kulsum", "CGPA": 3.92, "City": "Ishwardi"},
    {"ID": "221311084", "Name": "Jasy", "CGPA": 4.00, "City": "Rajshahi"},
    {"ID": "221311085", "Name": "Tamanna", "CGPA": 3.82, "City": "Rajshahi"},
    {"ID": "221311086", "Name": "Ishtiaq", "CGPA": 3.57, "City": "Rajshahi"},
    {"ID": "221311088", "Name": "Mou", "CGPA": 3.60, "City": "Rajshahi"},
    {"ID": "221311089", "Name": "Safwan", "CGPA": 3.43, "City": "Naogaon"},
    {"ID": "221311091", "Name": "Nerisha", "CGPA": 3.33, "City": "Naogaon"},
    {"ID": "221311092", "Name": "MAHMUDUL", "CGPA": 3.22, "City": "Rajshahi"},
    {"ID": "221311094", "Name": "Noman", "CGPA": 3.64, "City": "Rajshahi"},
    {"ID": "221311095", "Name": "Shihab", "CGPA": 2.82, "City": "Rajshahi"},
    {"ID": "221311096", "Name": "Solaiman", "CGPA": 3.10, "City": "Rajshahi"},
    {"ID": "221311097", "Name": "Nahid", "CGPA": 4.00, "City": "Rajshahi"},
    {"ID": "221311099", "Name": "MOUMITA", "CGPA": 3.83, "City": "Charghat"},
    {"ID": "221311100", "Name": "Amlan", "CGPA": 3.89, "City": "Rajshahi"},
    {"ID": "221311102", "Name": "Nurtaz", "CGPA": 3.64, "City": "Rajshahi"},
    {"ID": "221311104", "Name": "Sabbir", "CGPA": 3.89, "City": "Natore"},
    {"ID": "221311106", "Name": "Tina", "CGPA": 3.11, "City": "Rajshahi"},
    {"ID": "221311107", "Name": "Mukul", "CGPA": 3.15, "City": "Chapai Nawabganj"},
    {"ID": "221311109", "Name": "Rohidul", "CGPA": 3.89, "City": "Naogaon"},
    {"ID": "221311110", "Name": "Najmul", "CGPA": 3.56, "City": "Rajshahi"},
    {"ID": "221311111", "Name": "Iftakhar", "CGPA": 3.00, "City": "Chapai Nawabganj"},
    {"ID": "221311113", "Name": "Mahfuj", "CGPA": 3.78, "City": "Chapainawabganj"},
    {"ID": "221311114", "Name": "Md. Nur Alam", "CGPA": 3.82, "City": "Natore"},
    {"ID": "221311115", "Name": "Shahariar", "CGPA": 3.60, "City": "Chapai Nawabganj"},
    {"ID": "221311116", "Name": "SARWAR", "CGPA": 3.35, "City": "Tanore"},
    {"ID": "221311117", "Name": "Rinku", "CGPA": 3.32, "City": "Ishwardi"},
    {"ID": "221311118", "Name": "Mahi", "CGPA": 2.46, "City": "Rajshahi"},
    {"ID": "221311119", "Name": "Sija", "CGPA": 3.76, "City": "Rajshahi"},
    {"ID": "221311120", "Name": "Amimoy", "CGPA": 3.96, "City": "Rajshahi"}
]

print("")
print("section C all ID:")
print([student["ID"] for student in SectionC])


print(" ")
print("section C all Name:")
print([student["Name"] for student in SectionC])

print(" ")
print("section C all CGPA:")
print([student["CGPA"] for student in SectionC])

print(" ")
print("section C all City:")
print([student["City"] for student in SectionC])
print(" ")


if (student["Name"] == "Md. Nur Alam" for student in SectionC):
    print("Yes, Md. Nur Alam exists in this list") 
else:
    print("No, Md. Nur Alam is not in this list")

# found = False
# for student in SectionC:
#     if student["Name"] == "Md. Nur Alam":
#         found = True
#         break

# if found:
#     print("Yes, it is inside in the Section C.")
    
# else:
#     print("No, this is not found")
