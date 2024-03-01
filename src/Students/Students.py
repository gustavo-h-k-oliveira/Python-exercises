import csv

print("-----------------------")
print("| Student information |")
print("-----------------------")

loop = True

while (loop == True):

    try:
        option = int(input("\nDo you wish to read or modify the students list?\nDigit [1] to read, [2] to modify or [3] to end session: "))

        if (option == 1):
            option_read = int(input("\nDo you wish to search for a student or view the entire table?\nDigit [1] to display the full student list or [2] to search for student by name: "))

            try:
                if (option_read == 1):
                    with open("students.csv", newline="") as student_file:
                        reader = csv.reader(student_file, delimiter=' ', quotechar="|")
                        print("\nContent file:\n")
                        for row in reader:
                            for item in row:
                                print(item, end="")
                            print()

                elif (option_read == 2):
                    name_search = str(input("\nEnter student name: "))
                    with open("students.csv", newline="") as student_file:
                        reader = csv.DictReader(student_file)
                        absent_student = True
                        for row in reader:
                            if (row["Name"][0] == "|"):
                                row["Name"] = row["Name"][1:]
                                row[" Grade2"] = row[" Grade2"][:-1]
                            
                            if (name_search == row["Name"]):
                                print(row)
                                first_grade = int(row[" Grade1"].strip())
                                second_grade = int(row[" Grade2"].strip())
                                average_grade = (first_grade + second_grade) / 2
                                print(f"Student {name_search}'s average grade is {average_grade}.")
                                absent_student = False
                                
                        if (absent_student == True):
                            print("\nStudent not found. Please, try again.")

            except ValueError:
                print("\nError: Invalid input. Please enter a valid integer.")

        elif (option == 2):
            with open("students.csv", "a", newline="") as student_file:
                writer = csv.writer(student_file, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
                loop_write = True
                while (loop_write == True):
                    option_write = str(input("\nDo you want to add another student? [y/n]: "))
                    option_write = option_write.strip().lower()

                    if (option_write == "y"):
                        name = str(input("Enter the new student's name: "))
                        age = str(input("Enter the new student's age: "))
                        grade_1 = str(input("Enter the new student's first grade: "))
                        grade_2 = str(input("Enter the new student's second grade: "))

                        writer.writerow([f"{name}, {age}, {grade_1}, {grade_2}"])
                        
                    elif (option_write == "n"):
                        print("Closing the editor...")
                        loop_write = False
                    else:
                        print("\nInvalid command. Please, try again.")
                    

        elif (option == 3):
            loop = False

    except ValueError:
        print("\nError: Invalid input. Please enter a valid integer.")
    
print("\nClosing the session...")
print("See you later! 👋")