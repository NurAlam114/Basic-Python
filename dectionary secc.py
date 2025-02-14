student_list = {
    221311082: {
        "Name": "Esha",
        "ID": 221311082, 
        "CGPA": 3.86, 
        "Address": "Rajshahi"
        },
    221311083: {
        "Name": "Umme Kulsum",
        "ID": 221311083,
        "CGPA": 3.92, 
        "Address": "Ishwardi"
        },
    221311084: {
        "Name": "Jasy",
        "ID": 221311084, 
        "CGPA": 4.00, 
        "Address": "Rajshahi"
        },
    221311085: {
        "Name": "Tamanna",
        "ID": 221311085, 
        "CGPA": 3.82,
        "Address": "Rajshahi"
        },
    221311086: {
        "Name": "Ishtiaq",
        "ID": 221311086, 
        "CGPA": 3.57, 
        "Address": "Rajshahi"
        },
    221311088: {
        "Name": "Mou", 
        "ID": 221311088, 
        "CGPA": 3.60,
        "Address": "Rajshahi"
        },
    221311089: {
        "Name": "Safwan",
        "ID": 221311089,
        "CGPA": 3.43,
        "Address": "Naogaon"
        },
    221311091: {
        "Name": "Nerisha",
        "ID": 221311091,
        "CGPA": 3.33, 
        "Address": "Naogaon"
        },
    221311092: {
        "Name": "MAHMUDUL",
        "ID": 221311092, 
        "CGPA": 3.22, 
        "Address": "Rajshahi"
        },
    221311094: {
        "Name": "Noman",
        "ID": 221311094, 
        "CGPA": 3.64,
        "Address": "Rajshahi"
        },
    221311095: {
        "Name": "Shihab",
        "ID": 221311095,
        "CGPA": 2.82,
        "Address": "Rajshahi"
        },
    221311096: {
        "Name": "Solaiman",
        "ID": 221311096,
        "CGPA": 3.10, "Address": 
        "Rajshahi"
        },
    221311097: {
        "Name": "Nahid",
        "ID": 221311097, 
        "CGPA": 4.00,
        "Address": "Rajshahi"
        },
    221311099: {
        "Name": "MOUMITA",
        "ID": 221311099,
        "CGPA": 3.83, 
        "Address": "Charghat"
        },
    221311100: {
        "Name": "Amlan",
        "ID": 221311100,
        "CGPA": 3.89,
        "Address": "Rajshahi"
        },
    221311102: {
        "Name": "Nurtaz",
        "ID": 221311102,
        "CGPA": 3.64,
        "Address": "Rajshahi"
        },
    221311104: {
        "Name": "Sabbir",
        "ID": 221311104,
        "CGPA": 3.89,
        "Address": "Natore"
        },
    221311106: {
        "Name": "Tina", 
        "ID": 221311106,
        "CGPA": 3.11,
        "Address": "Rajshahi"
        },
    221311107: {
        "Name": "Mukul",
        "ID": 221311107,
        "CGPA": 3.15,
        "Address": "Chapai Nawabganj"
        },
    221311109: {
        "Name": "Rohidul",
        "ID": 221311109,
        "CGPA": 3.89,
        "Address": "Naogaon"
        },
    221311110: {
        "Name": "Najmul",
        "ID": 221311110,
        "CGPA": 3.56,
        "Address": "Rajshahi"
        },
    221311111: {
        "Name": "Iftakhar",
        "ID": 221311111,
        "CGPA": 3.00, 
        "Address": "Chapai Nawabganj"
        },
    221311113: {
        "Name": "Mahfuj",
        "ID": 221311113,
        "CGPA": 3.78,
        "Address": "Chapainawabganj"
        },
    221311114: {
        "Name": "Md. Nur Alam",
        "ID": 221311114,
        "CGPA": 3.82, 
        "Address": "Natore"
        },
    221311115: {
        "Name": "Shahariar", 
        "ID": 221311115,
        "CGPA": 3.60,
        "Address": "Chapai Nawabganj"
        },
    221311116: {
        "Name": "SARWAR",
        "ID": 221311116, 
        "CGPA": 3.35,
        "Address": "Rajshahi"
        },
    221311117: {
        "Name": "Rinku",
        "ID": 221311117,
        "CGPA": 3.32, 
        "Address": "Ishwardi"
         },
    221311118: {
        "Name": "Mahi",
        "ID": 221311118,
         "CGPA": 2.46,
        "Address": "Rajshahi"
        },
    221311119: {
        "Name": "Sija", 
        "ID": 221311119,
        "CGPA": 3.76,
        "Address": "Rajshahi"
        },
    221311120: {
        "Name": "Amimoy",
        "ID": 221311120,
        "CGPA": 3.96,
        "Address": "Rajshahi"
        }
}

student_name=[student_list[student]["Name"]for student in student_list]  
print(student_name)

student_ID=[student_list[student]["ID"]for student in student_list]  
print(student_ID) 

student_CGPA=[student_list[student]["CGPA"]for student in student_list]  
print(student_CGPA) 

student_Address=[student_list[student]["Address"]for student in student_list] 
print(student_Address)

if student_name: 
    print("Yes,Shihab exists in this list") 
else: 
    print("No,Shihab is not exits in this list ")