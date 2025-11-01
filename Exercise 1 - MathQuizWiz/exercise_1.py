# MathQuizWiz Tkinter + Python Game

# Imports
from tkinter import * # Import Tkinter in Python File
import random # Imports access to Python's random module.

# Tkinter
root = Tk() # Storing the GUI in an accessible variable
root.title("Math Quiz") # Sets title for the GUI
root.geometry('600x600') # Sets dimension of the GUI
root.configure(bg="#242424") # Configures to set the background color of the GUI.

################################

# Frames
f1 = Frame(root, bg='#242424') # This frame will hold all the elements.
f1.place(relx=0.5, rely=0.5, anchor=CENTER) # The frame is positioned in a way it is centered in the app's screen.

# Labels

l1 = Label(f1, text="MathQuizWiz", bg="#242424", fg="white", font=("Helvetica", 45, 'bold')) # Title of the quiz game.
l2 = Label(f1, text="Choose your difficulty:", bg="#242424", fg="white", font=("Helvetica", 12, 'bold')) # Text to label the diffculty menu screen.

# Textbox

t1 = Text(f1, width="10", height="1", bg="white", font=("Helvetica", 12, 'bold'), state="disabled" ) # Score Textbox
t2 = Text(f1, width="50", height="5", bg="white", font=("Helvetica", 15, 'bold'), state="disabled" ) # Display Textbox

# Entry

e1 = Entry(f1, width="25", bg="white", font=("Helvetica", 10, 'bold')) # Input Textbox
e1.bind("<Return>", lambda event: submit()) # This helps me submit the text when enter key is clicked.

# Buttons

b1 = Button(f1, text="Easy", relief="flat", bg="#723E78", fg="white", width="25", font=('Helvetica', 12, 'bold'), command=lambda: displayProblem(1)) # Easy Button 
b2 = Button(f1, text="Moderate", relief="flat", bg="#723E78", fg="white", width="25", font=('Helvetica', 12, 'bold'), command=lambda: displayProblem(2)) # Moderate Button
b3 = Button(f1, text="Hard", relief="flat", bg="#723E78", fg="white", width="25", font=('Helvetica', 12, 'bold'), command=lambda: displayProblem(4)) # Hard Button
b4 = Button(f1, text="Play Again", relief="flat", bg="#723E78", fg="white", width="25", font=('Helvetica', 12, 'bold'), command=lambda: displayProblem(None)) # Play Again
b5 = Button(f1, text="Back", relief="flat", bg="#723E78", fg="white", width="25", font=('Helvetica', 12, 'bold'), command=lambda: displayMenu()) # Back Button

################################

# Variables

tries = 0 # Tracks the amount of wrong tries.
wronggate = None # Variable that determines if the user got it wrong the first try
iterations = 1 # Stores the amount of iterations passed
score = 0 # Stores the score of the user.
questions = 10 # Stores the amount of questions should the program display. 
menu = [l1, l2, b1, b2, b3] # Stores all Tkinter elements for menu
quiz = [t1, t2, e1, b5] # Stores all Tkinter elements for the quiz
dig = 0 # Sets the number of digits.
gate = False # This gate allows me to manipulate when to clear the frame.
result = True

################################

# Custom Functions

def cleardisplay(): # Clears the textboxes display.
    # For the display box
    t2.config(state="normal") # Unlocks the textbox
    t2.delete("1.0", END) # Deletes what's in the textbox.
    t2.config(state="disabled") # Locks the textbox

    # For the score display box
    t1.config(state="normal") # Unlocks the textbox
    t1.delete("1.0", END) # Deletes what's in the textbox.
    t1.config(state="disabled") # Locks the textbox

def clearFrame(): # Clears current elements within the frame.
    for item in f1.winfo_children(): # .winfo_chilren on my frame allows me to access all children widgets within the parent frame through a for-loop
        item.pack_forget() # Using a for-loop, I can forget each widget to make way for the new UI display.

def submit(): # Responsible for passing the input to a variable
    global result, userinput, equa, iterations, score, tries, wronggate # Gives global access to result, userinput, the equation, iterations, score, tries and the wrong gate.
    userinput =  e1.get().strip() # Strips the line in the textbox and gets the value to store in a variable
    
    # Compute for checking
    equa = equa.strip('=') # Removes the equal sign to be able to calculate.
    cleardisplay() # Clears the display to make way for new display.
    result = isCorrect(equa) # This function runs to check if the answer is correct, then returns a value for confirmation. Whatever the result, it is stored in a variable.

    if result == True: # If the results are correct
        iterations += 1 # Adds 1 to the iteration variable.

        if wronggate == True: # If the user got it wrong once.
            score += 5 # Score is capped to 5 points.
            wronggate = False # Then the wrong variable is reset.
        else:
            score += 10 # If the user got it right first attempt, 10+ score is added.

        correct = "Correct!" # Stores the message in the variable.
        t2.config(state="normal") # Unlocks the textbox
        t2.insert(END, correct + "\n") # Inserts the necessary text to inform your input is invalid.
        t2.config(state="disabled") # Locks the textbox
        e1.delete(0,END) # Deletes the entry till the end for fresh new inputs if you're right.
        
    if result == False: # If the results are wrong
        tries += 1 # Tracks the amount of wrong tries.
        wronggate = True # Wronggate is set true to inform that the user got the answer wrong in their first attempt.

        if tries > 1: # If the amount of wrong tries are over 1 time, the program continues.
            iterations += 1 # Adds 1 to the iteration variable.

        wrong = "Wrong!" # Stores the message in the variable.
        t2.config(state="normal") # Unlocks the textbox
        t2.insert(END, wrong + "\n") # Inserts the necessary text to inform your input is invalid.
        t2.config(state="disabled") # Locks the textbox
            
    if result == None: # If the input is not computable.
        result = ""

    root.after(2000, lambda: displayProblem(dig)) # This helps me display the problem always every time the user submits. ".after" helps me schedule a function after a delay.

# Required Functions

def displayMenu(): # Runs the menu of the GUI
    global gate # Acquires access to gate.

    gate = True # Gate is set true when menu is present.

    cleardisplay() # Clears the textbox's display.
    clearFrame() # Clears all current elements within the frame
    for item in menu: # For-loop goes through the list of elements in "menu."
        if item == l2: # If it's l2, it's packed differently.
            item.pack(pady=15)
        else: # Otherwise, it assumes all to be buttons and are packed the same.
            item.pack(pady=(0,5))

def randomInt(dig): # Determines the values used in each question.
    global x, y # Allows global access to x and y variables
    x = random.randrange(10**(dig-1), 10**dig) # A random digit is assigned to x, its digits are determined by the difficulty.
    y = random.randrange(10**(dig-1), 10**dig) # A random digit is assigned to y, its digits are determined by the difficulty.

def decideOperation(): # Decides what kind of equation will it display.
    global x, y, equa # Acquires access to x, y and gives equa global access.
    symb = random.choice(['+', '-']) # Randomly chooses an item in the list and stores it in symb. This helps randomizes equations.
    equa = str(x) + symb + str(y) + "=" # Turns the expression into a string for display and evaluation. "equa" holds the equation.
    return equa

def displayProblem(num): # Displays the problem, receives the answers.
    global gate, result, dig, equa, iterations, score, tries # Acquire access to the gate, result, dig, equation, score, and tries (dig = number of digits) 

    if num == None: # If the argument is None,
        b4.forget() # It signals a play again and hides the play again button to start the game again.
    else: 
        dig = num # Assigns a new amount of digits

    if result == True and iterations <= questions : # If the answer is correct and have not completed all the questions, this condition will reconstruct a new equation.
        randomInt(dig) # Determines the values used in each question, and assigns a number of digit to the digit variable within the function.
        equa = decideOperation() # Decides what kind of equation will it display.

    if tries > 1 and iterations <= questions: # If the answer is wrong and have not completed all the questions, this condition will reconstruct a new equation.
        randomInt(dig) # Determines the values used in each question, and assigns a number of digit to the digit variable within the function.
        equa = decideOperation() # Decides what kind of equation will it display.
        tries = 0 # Tries are then reset.

    if iterations > questions: # If iterations has met with the questions limit.
        equa = f"You have completed the quiz!" # Equa is assigned with information to the user that they completed the quiz.
        e1.forget() # Removes the entry button

    cleardisplay() # Clears the display to make way for new equations.
    
    # Inserts the equation to the textbox.
    t2.config(state="normal") # Unlocks the textbox
    t1.config(state="normal") # Unlocks the textbox

    if iterations > questions: # If iterations has met with the questions limit
        t2.insert(END, equa + "\n") # Inserts the necessary text without the number labels.
        t1.delete("1.0", END) # Deletes the score display
        b4.pack(pady=(0,15)) # Packs a button and reveals it in the frame.

        displayResults() # Displays the results in the main screen through this function.
        
        score = 0 # Score is then reset back to 0.
        iterations = 1 # Resets the iterations back to 0
    else: # Otherwise,
        t2.insert(END, f"{iterations}. {equa}\n") # Inserts the necessary text with the number labels.
        t1.insert(END, f"Score: {score}")

    t1.config(state="disabled")  # Locks the textbox
    t2.config(state="disabled") # Locks the textbox

    # UI
    if gate == True: # If menu was present, gate is true which opens a path to clear the frame and display the game quiz.
        clearFrame() # Clears all current elements within the frame

        for item in quiz: # For-loop to go through the Tkinter element stored in the list "quiz."
            item.pack(pady=(0,15)) # Packs it up with a specific attribute.

        gate = False # Gate is then closed. So as long as menu isn't displayed again, frame won't be cleared and this function can be called multiple times.          

def isCorrect(var): # Checks if the user's answer is correct or wrong.
    global userinput # Acquires access to equa and userinput. (the equation)

    answ = eval(var) # Evaluates the string equation to return an answer
    try:
        answ = int(answ) # It is then converted into an integer for comparison.
        answ2 = int(userinput) # Turns the userinput into an integer and stores it in a variable for comparison.
        return answ == answ2 # If the user's answer is correct, it returns True. Otherwise, it returns False.
        
    except:
        error = "Please enter a valid number."
        t2.config(state="normal") # Unlocks the textbox
        t2.insert(END, error + "\n") # Inserts the necessary text to inform your input is invalid.
        t2.config(state="disabled") # Locks the textbox
        return None # It returns nothing as as boolean.

def displayResults(): # This displays the total score of the Quiz per difficulty.
    global score # Acquires access to score.
    rating = ""
    print(score)
    
    if score < 60:
        rating = "F"
    elif score > 60 and score <= 70:
        rating = "D"
    elif score > 70 and score <= 80:
        rating = "C"
    elif score > 80 and score <= 90:
        rating = "B"
    elif score > 90 and  score <= 100:
        rating = "A"


    t2.insert(END, f"Total Score is: {score}.\nRating: {rating}")

##################################

# System
displayMenu() # Runs the menu of the GUI
root.mainloop() # Runs the Tkinter GUI