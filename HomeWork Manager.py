
#prints homework file as of opening the app
file=open("homework.txt", "r")
current_homework=file.readlines()
print(current_homework)
file.close()
#makes list (NEED DO NOT REMOVE)
assignments=current_homework


# sets assignments to content of file
file1=open("homework.txt", "r")
assignments=file1.readlines()
file1.close()
#choose to add or remove assignment
added = 0
while added == 0:
    add_remove=input("add or remove assignment?: ")
    added = 1
    break
#adds assignment
while add_remove == "add":
    assignment=input("enter assignment and due date. ex: 4 types of government, 12/6/22.: ")
    assignments.append(assignment)
    assignment = ""
    file2=open("homework.txt", "w")
    file2.writelines(assignments)
    file2.close()
    add_again=input("add another assignment?: yes/no")
    if add_again == "yes":
        a=open("homework.txt", "w")
        a.writelines(assignments)
        a.close()
        added = 0
        break
    else:
        added = 0
        break
#removes assignment
else:
    print(current_homework)
    remove=input("To remove please type assignment and due date exactly how seen above. ex: '4 types of government, 12/6/22.': ")
    assignments.remove(remove)
    print(assignments)
    file3=open("homework.txt", "w")
    file3.writelines(assignments)
    file3.close()
    added = 0