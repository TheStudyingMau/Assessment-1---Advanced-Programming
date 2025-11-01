from tkinter import * # Imports Tkinter in the Python File
from tkinter import ttk # Imports TTk submodule in Python File.
import os # Imports the Operating System for me to access file directories.

root = Tk() # Storing the Tkinter module for access in a variable.
root.title('Student Manager') # Sets the title of the application.
root.geometry('700x600') # Sets dimension of the GUI
root.configure(bg="#E1E1E1") # Allows me to configure the main app's background color.

##################################

# Variable, Dictionaries, & Lists

amount = 0 # Stores the amount of students in the data.
script_dir = os.path.dirname(__file__)  # Finds the folder where exercise3.py lives
file_path = os.path.join(script_dir, 'studentMarks.txt') # Constructs a path to the file I want to use and stores in a variable for use.

students = {} # The list that stores student data.
comparelist = {} # Stores dictionaries of students and their scores for comparison.
studentlist = [] # Stores the names of students used for the Combobox.


# Tkinter GUi

f1 = Frame(root, bg="#E1E1E1", highlightbackground="black", highlightthickness=1) # Frame that contains the label and textbox display.
f1.place(relx=0.5, rely=0.4, anchor=CENTER)

f2 = Frame(root, bg="#E1E1E1", highlightbackground="black", highlightthickness=1) # Frame that contains the combobox and buttons.
f2.place(relx=0.5, rely=0.65, anchor=CENTER)

Label(f1, text="Student Manager", fg="black", bg="#E1E1E1", font=('Courier', 15, 'bold')).pack(pady=5)   # Label for title. (decided to combine its position into one line)

t1 = Text(f1, width="60", height="10",bg='white', state="disabled", wrap='word', font=('Courier', 10)) # Textbox for display.
t1.pack(padx=10, pady=10)

c1 = ttk.Combobox(f2, state="readonly", font=('Courier', 10), width="42") # This is responsible for the combobox for selecting a student. It is currently limited to "read only."
c1.set('Select') # This is the default text present when nothing is selected.
c1.grid(row=0, column=0, columnspan=2) # Using .grid allows me to be able to put the combobox next to the button.

b1 = Button(f2, text="View Record", bg="#ACACAC", font=('Arial', 12), command=lambda: viewinfo()) # Button that's responsible to view the student based on the combobox's value.
b1.grid(row=0, column=2, sticky="EW") # This positions the button next to the combobox.

b2 = Button(f2, text="View All Records", bg="#ACACAC", font=('Arial', 12), command=lambda: displayall())
b2.grid(row=1, column=0, sticky="EW") 

b3 = Button(f2, text="Show Highest Mark", bg="#ACACAC", font=('Arial', 12), command=lambda: greater())
b3.grid(row=1, column=1, sticky="EW") 

b3 = Button(f2, text="Show Lowest Mark", bg="#ACACAC", font=('Arial', 12), command=lambda: lesser())
b3.grid(row=1, column=2, sticky="EW") 

# Functions

def cleardisplay(): # Clears the textbox's display.
    t1.config(state="normal") # Unlocks the textbox
    t1.delete("1.0", END) # Deletes what's in the textbox.
    t1.config(state="disabled") # Locks the textbox

def assess(val1, val2): # Assess the students score and grades it.
    marks = val1 + int(val2) # Combines the marks
    percent = (marks / 160) * 100  # Divides the marks by the total marks and multiply it by 100 will get us our average score for our student.
    percent = round(percent, 2) # Rounds the percent we have into 2 decimal places and stores it back. 
    
    # Grading System
    if percent >= 70: # If it is equal or greater than 70, it's an "A"
        grade = "A"
    elif percent >= 60 and percent <= 70: # If it is greater than 60 but less than 70, it's a "B"
        grade = "B"
    elif percent >= 50 and percent <= 60: # If it is greater than 50 but less than 60, it's a "C"
        grade = "C"
    elif percent >= 40 and percent <= 50: # If it is greater than 40 but less than 50, it's a "D"
        grade = "D"
    elif percent <= 40: # If it is equal or less than 40, it's a hard "F"
        grade = "F"

    return percent, grade

def scoresort(val1): # Sorts the score from data.
    scores = [int(score) for score in val1] # Using a short form of for-loop, turns each score into integer and stores it back to the list. Converting all strings into integers.
    total = sum(scores) # This will allow us to find the sum of the scores and store it in an accessible variable to call out.
    return total # Returns the variable for use

def displayall(): # Responsible for displaying info to the textbox.
    averperc = [] # Variable to contain all percentages to find the average percentage.
    cleardisplay() # Clears textbox display.

    for student in studentlist: # Goes through the names listed for combobox.

        averperc.append(comparelist[student][1]) # Adds the percentage of the person in the averperc list to find the average percentage of all percentages.

        t1.config(state="normal") # Unlocks the textbox
        # Inserts the necessary text:
        t1.insert(END, f"\nStudent Name: {student}\nStudent Number: {students[student][0]}\nCoursework Total: {comparelist[student][0]}\nExam Mark: {students[student][-1]}\nOverall Percentage: {comparelist[student][1]}%\nGrade: {comparelist[student][-1]}\n") 
    
    average = sum(averperc) / len(averperc) # Divides the sum of all the percentages by the amount of them to find the average.
    average = round(average, 2) # Rounds the average percentage to 2 decimal places.
    t1.insert(END, f"\n\nStudent Amount: {amount}\nAverage Percentage Mark: {average}%") # Student amount and average percentage mark is then displayed.
    t1.config(state="disabled") # Locks the textbox
    
def viewinfo(): # Responsible for viewing information
    select = c1.get() # Gets the value of the combobox when selected.
    cleardisplay() # Makes way for new display

    try: # If there is value in the combobox, it executes to display the info
        t1.config(state="normal") # Unlocks the textbox
        t1.insert(END, f"\nStudent Name: {select}\nStudent Number: {students[select][0]}\nCoursework Total: {comparelist[select][0]}\nExam Mark: {students[select][-1]}\nOverall Percentage: {comparelist[select][1]}%\nGrade: {comparelist[select][-1]}\n") 
        t1.config(state="disabled") # Locks the textbox
    except: # If there is no value, it returns nothing
        return None

def assign(): # Responsible for sorting lines from the textfile and assigning data to accessible variables.
    global amount # Gives global access to amount.

    with open(file_path) as file_handler: # Opens the .txt file for me to access.
        global comparelist # Gives global access to comparelist

        lines = file_handler.readlines() # Stores each line into a list of lines.
        count = 0 # Counter for the for-loop iterations
        data = [] # Data is a list variable

        for line in lines: # Goes through each line stored in the list
            line = line.rstrip() # Removes \t and \n to get the raw text and redefines the line with that raw text.

            if count == 0: # If it is the first iteration,
                amount = int(line) # Stores the first data in the text file in the variable assigned
            else:
               data = line.split(',', 5) # divides the lines and stores it in the list
               scores = data[2:5] # From index 2 to 5, the student's scores are grouped.
               students[data[1]] = [data[0], scores, data[-1]] # Stores all the information as a dictionary

               total = scoresort(scores) # The returned data from scoresort() functions is stored as the total score from the scores. 
               percent, grade = assess(total, data[-1]) # The percentage and grade is supplied by the returning values of the assess() function.
               comparelist[data[1]] = [total, percent, grade] # Creates a dictonary within comparelist that consists the name of the student and their percentage of their score.

               studentlist.append(data[1]) # Adds the names of the students into a list.

            count += 1 # Adds count after first iteration passes.   

        c1.config(values=studentlist)

def greater(): # Finds the greater value from the comparelist.
    topstudent = max(comparelist, key=lambda name: comparelist[name][1]) 
    # Max() function helps me goes through the given list (comparelist) and find the maximum value (the highest value).
    # "Key=" narrows down and defines how to compare the elements (which is using their percentage)
    # "lambda" as a mini function takes "name" as input to use to go through the comparelist.
    # "comparelist[name][1]" accesses the percentage value. (used as a basis of comparison)

    cleardisplay() # Clears the textbox display to make way for new display.
    t1.config(state="normal") # Unlocks the textbox
    t1.insert(END, f"\nStudent Name: {topstudent}\nStudent Number: {students[topstudent][0]}\nCoursework Total: {comparelist[topstudent][0]}\nExam Mark: {students[topstudent][-1]}\nOverall Percentage: {comparelist[topstudent][1]}%\nGrade: {comparelist[topstudent][-1]}\n") 
    t1.config(state="disabled") # Locks the textbox

def lesser(): # Finds the lesser value from the comparelist.
    botstudent = min(comparelist, key=lambda name: comparelist[name][1]) #key=lambda helps me tell the function to compare based on the selected value via index.
    # Similar to Max(), min() finds the lesser value from the list.    

    cleardisplay() # Clears the textbox display to make way for new display.
    t1.config(state="normal") # Unlocks the textbox
    t1.insert(END, f"\nStudent Name: {botstudent}\nStudent Number: {students[botstudent][0]}\nCoursework Total: {comparelist[botstudent][0]}\nExam Mark: {students[botstudent][-1]}\nOverall Percentage: {comparelist[botstudent][1]}%\nGrade: {comparelist[botstudent][-1]}\n") 
    t1.config(state="disabled") # Locks the textbox

##################################

assign() # Assigns data before GUI starts
root.mainloop() # Runs the Tkinter GUI