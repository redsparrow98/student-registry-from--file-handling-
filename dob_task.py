# Please read the README.txt for information on the program

#=====================         Code       =========================

# Opens the DOB file as file reads all lines and stores in to variable content
with open("./Input Code Files/Task file/DOB.txt", "r", encoding= "utf_8") as file:
    content = file.readlines()

    # Creates list comprehension to split the first 2 words in the content and
    # creates a names_list full of nested list containing first and last names
    names_list = [line.split()[:2] for line in content]

    # Creates list comprehension to split the last 3 words in the content and
    # creates a birthdays_list full of nested lists containing birthdays
    birthdays_list = [line.split()[2:] for line in content]

    # Creates variables containing an empty space and new line to use in the joining
    empty_space = " "
    new_line = "\n"

    # Every inner list in the names_list is joint to each other with an empty space
    # and a new line after each inner list
    #its saved in to a names variable as a string of all names
    names = new_line.join(empty_space.join(inner_list) for inner_list in names_list)

    # Every inner list in the birthdays_list is joint to each other with an empty space
    # and a new line after each inner list
    # its saved in to a names variable as a string of all names    
    birthday = new_line.join(empty_space.join(inner_list) for inner_list in birthdays_list)

# Variables for start and end of bold text
start = "\033[1m"
end = "\033[0;0m"

# Prints the names and birthdays in bold
# prints out the names and birthdays strings
print(f"{start}Names{end}\n{names}")
print("\n\n")
print(f"{start}Birthdays{end}\n{birthday}")
