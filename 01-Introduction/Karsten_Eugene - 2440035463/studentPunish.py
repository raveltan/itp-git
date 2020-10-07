#Made variable for points and punishment
point = 0
punishment = ""

#Made variable containing a list
studentList = []

#Second loop after actions loop break
while True:

    #Inputting student name
    studentName = input("Name of student: ")

    #If student name is blank, breaks and proceeds to results
    if studentName == "":
        print("")
        break

    #First loop to input multiple actions
    while True:

        #Inputting actions of the student
        action = input("What did the student do: ")

        #Point system depending on their actions
        if action == "Late to class":
            point -= 2
        elif action == "No homework submission":
            point -= 4
        elif action == "Vandalized":
            point -= 6
        elif action == "Plagiarized":
            point -= 8
        elif action == "Cheated":
            point -= 10

        #If action is blank, breaks and proceeds to name inout again
        elif action == "":
            print("")
            break

        #If action is invalid, terminate the whole code
        else:
            print("No such action exists")
            quit()

    #punishments depending on the total amount of points of each student
    if point > -2:
        punishment = "Safe"
    elif point >= -6:
        punishment = "Detention"
    elif point > -10:
        punishment = "Suspended"
    elif point <= -10:
        punishment = "Expelled"

    #Adds different names of student and his/her punishment(s) after every loop until it breaks
    studentList.append(studentName + " - " + punishment)

print("Punishments")

#Displays the names and punishments of each students
for i in range(len(studentList)):
    print(studentList[i])
