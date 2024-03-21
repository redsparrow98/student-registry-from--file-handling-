# Please read the README.txt for information on the program

#=====================   Final code    =====================

# Prints out what venue the registration is for
print("The venue registry form for: The Great Hall Room\n")

# Requests input for number of students registering
no_students = int(input("How many students are registering?: "))

# Opens a reg_form.txt as file
# this file that doesn't exist which creates the file once the program runs
with open("reg_form.txt", "w", encoding= "utf-8") as file:

    # Uses a for loop and range that is the first user input for no_students
    for student in range(no_students):

        # Requests a second input for user ID and keeps asking for every
        # Iteration until end of loop
        student_id = input("Whats the student ID?: ")

        # Writes the student_id input in the file and add the line for signing
        # ends with a new line so each entry will be written in a new line
        file.write(student_id +"\t_________________\n")

# opens the file again but in read mode to get all the contents of the file
with open("reg_form.txt", "r", encoding= "utf-8") as file:
    reg_students = file.read()


# lets the user know the registry was successful and prints out the registered students
print("\nThat all the students registered, thank you.")
print(f"\n{reg_students}")
