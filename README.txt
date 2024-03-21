========================    DOB_TASK    ========================
"""I downloaded the input code files in the same folder
   where my dob_task.py is to simulate how the dropbox files would
   look. the instructions were not clear where we should save DOB.txt
   if there was any requirement on that"""


The program opens and reads the given file DOB.txt as a file

the file is read using the readlines() method which stores each
line in the given file as an item in the list named content

The program uses list comprehension to iterate trough the contents list
and slices each item in it which is a string.
it slices the first 2 words and creates nested lists containing name and
last name as a nested list in the new list named names

The program uses the same method to create the birthdays_list but this
time it slices the last 3 words of the item in the content list

the program creates variables 
empty_space = " "
new_line = "\n"

After this the program joins the nested lists in the names_list in to a
variable names it enters every new nested list as a new line to create one
string that contains all the names

It uses the same method for the birthdays

finally it prints out the names with the bold NAMES column name
leaving 2 new lines between
prints out birthdays with the bold BIRTHDAYS column name

========================    STUDENT REGISTER    ========================

prints out the name of the venue that the registry is for

requests a user input for the number of students registering and saves
in variable no_students

opens a file named reg_form.txt in write mode if the file doesn't exist
it will create one 

runs a for loop using the no_students as the range for how many times to run
the loop
in the loop it requests a second input for the user ID and saves it under user_id
variable
it then writes the user_id on the file and adds a dotted line after it for signature
as well as a new line mark so the next id would go under new line

========== 
finally i chose to add a confirmation for the user so they would know the entries
were successful

after all the IDs have been entered it opens reg_form.txt again but in read mode
to get the contents of It saving it under reg_students

lastly it prints out the confirmation message and all the students that just registered