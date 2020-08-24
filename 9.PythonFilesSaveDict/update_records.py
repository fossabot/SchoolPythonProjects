import ast
from pprint import pprint

with open('marks.dat') as read_file:
    student_dict = ast.literal_eval(read_file.read())

print("Current State: ")
pprint(student_dict)

choice = input("Do you wish to update records?[YES/NO]")
if choice in ['Y', 'y', 'Yes', 'yes', 'yEs', 'yeS', 'YEs', 'yES', 'YES']:
    print("Modifying Records")
    no_of_iterations = int(input("Enter the no of record to be entered:"))

    for i in range(no_of_iterations):
        print("Current Iter: ", i)
        roll_num = input("Enter Roll Number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        student_dict[roll_num] = {'Name':name, 'Marks':marks}

    with open("marks.dat", "w") as write_file:
        write_file.write(str(student_dict))
else:
    print("OK. Exiting.")