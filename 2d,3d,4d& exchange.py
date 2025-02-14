Student_list = {
    221311097 :{
                "Name" : "Nahid",
                "ID" : 97,
                "Semester": 30000
            },
    221311111 :{
                "Name" : "Tonay",
                "ID" : 111,
                "Semester": 30000
            },
    221311114: {
                "Name" : "Md. Nur Alam",
                "ID" : "114",
                "Semester": "8",
                "Time_verse": [
                                [
                                    [
                                        [10,20,30],
                                        [40,50,60,70]
                                    ],
                                    [
                                        [101,202,303],
                                        [404,505,606,707]
                                    ]
                                ],
                                [
                                    [
                                        [1000,2000,3000],
                                        [4000,5000,6000,7000]
                                    ],
                                    [
                                        [1001,2002,3003],
                                        [4004,5005,6006,7007]
                                    ]
                                ]
                            ]
    }
}

#print(Student_list[221311111]["ID"])
#print(Student_list[221311114]["ID"])
print("\nGiven informantion:")
print(Student_list[221311114]["Time_verse"])
Student_list[221311114]["Time_verse"][1][0][0][1] = Student_list[221311114]["ID"]

print("\nAfter update:")
print(Student_list[221311114]["Time_verse"])
print(" ")