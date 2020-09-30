"""This is a fun VIM exercise for me to learn code and vim at the same time"""
print("Add people to your family")

question = input("Do you want to add to your family?: ")
family = {}    
iterator = 0 
index= 0
rows = [1]
x=0
table = [['Age','First Name','Last Name']]

def buildPerson():
    global iterator
    age = input("What is your age: ")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    iterator += 1
    family.update({'Age ' + str(iterator): age})
    family.update({'First Name '+ str(iterator): first_name})
    family.update({'Last Name '+ str(iterator): last_name})
    iterator = int(iterator)
    
def buildtable():
    global index
    while (index < len(family)/3):
        index += 1
        table.append(list([family['Age '+str(index)], family['First Name ' + str(index)], family['Last Name '+ str(index)]]))
        rows.append(index)
        index = int(index)
     

while(question[0]=='y') or ( question[0]=='Y') :
    buildPerson()
    question = input("Do you want to keep adding to your family?: ")
    if (question[0]=='N') or (question[0] == 'n'):
        buildtable()

print("This is your family table!")

for i in range(len(table)):
    print(table[i])
