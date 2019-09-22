

print("Please Select any one option from below option!!!!")
print("1. Adding Data to file : ")
print("2. Searching the Record : ")
#print("4. Deleting the Reocrd : ")
print("4. Updating the Record: ")

x = int(input("Enter Your Choice :"))

if x == 1:
    from os.path import exists

    if exists("student.csv"):
        f = open("student.csv","a")
    else:
        f = open("student.csv","w")
    while True:
        l = []
        l.append(input("Enter the Student Id :"))
        if not l[0]:
            break
        else:
            l.append(input("Enter The Student Name :"))
            l.append(input("Enter The Student Email Address : "))
            f.write(",".join(l)+"\n")
    f.close()

#============================================================================================================================
elif x == 2:

    f = open("student.csv")
    search = input("Enter The Student Name : ")
    for lines in f:
        l = lines.split(",")
        if search =="" or (search.lower() in l[1].lower() or search.lower() in l[0].lower()):
            print("The Student ID is : %s\n The Name of Student is : %s\n The Email of the student is : %s"%(l[0],l[1],l[2]))
    f.close()

#------------------------------------------------------------------------------------------------------------------------
elif x == 3:
    f = open("student.csv","r")
    search = input("Please Enter Student Name or Student Id for search")
    recs = []
    found = False
    for line in f:
        l = line.split(",")
        if search=="" or (search.lower()==l[1].lower() or search.lower()==l[0].lower()):
            print("Student id is : %s\n Student Name is : %s\n Phone Number is : %s\n Email Address : %s"%(l[0],l[1],l[2],l[3]))
            if input("Are you sure you wanted to update this record ?").lower()=="y":
                s = []
                s.append(input("Enter The Student Id :"))
                s.append(input("Enter The Student Name :"))
                s.append(input("Enter The Student Phone Number :"))
                s.append(input("Enter The Student Email Address :"))
                found = True
            recs.append(s)
        f.close()
        if found:
            f = open("student.csv","w")
            for r in recs:
                f.write(",".join(r).rstrip()+"\n")
            f.close()
            print("File updated Succesfully")
        else:
            print(search,"The Name you entered is not found on the file")


else:
    print("Please Enter the Valid Choice!!!!")