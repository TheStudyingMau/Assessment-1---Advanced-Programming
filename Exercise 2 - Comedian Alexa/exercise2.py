# Alexa-Tell-Me-A-Joke Program!

from tkinter import * # Imports Tkinter in the Python File
import random, os # Imports the random module and the operating system for me to use.

root = Tk() # Storing the Tkinter module for access in a variable.
root.title('Alexa The Clown') # Sets the title of the application.
root.geometry('600x600') # Sets dimension of the GUI
root.configure(bg="#1B1919") # Allows me to configure the main app's background color.
###############################################

# Frame
f1 = Frame(root, bg="#1B1919")
f1.place(relx=0.5, rely=0.4, anchor=CENTER)

# Textbox
t1 = Text(f1, width="50", height="5",bg='white', state="disabled", wrap='word', font=('Calibri', 15))

# Label
l1 = Label(f1, text="Comedian Alexa", bg="#1B1919", fg="white", font=('Calibri', 35, 'bold'))

# Buttons
b1 = Button(f1, text="Start", relief="flat", bg="#2EA1FF", fg="white", width="18", font=('Calibri', 12, 'bold'), command=lambda: displayGame())
b2 = Button(f1, text="Alexa Tell Me A Joke", relief="flat", bg="#2EA1FF", fg="white", width="18", font=('Calibri', 12, 'bold'), command=lambda: displayGame())
b3 = Button(f1, text="Why?", relief="flat", bg="#2EA1FF", fg="white", width="18", font=('Calibri', 12, 'bold'), command=lambda: thejoke())
b4 = Button(f1, text="Close", relief="flat", bg="#2EA1FF", fg="white", width="18", font=('Calibri', 12, 'bold'), command=lambda: displayMenu())

# Variables
start = [l1, b1]
menu = [t1, b3, b4]
script_dir = os.path.dirname(__file__)  # Finds the folder where exercise3.py lives
image_path = os.path.join(script_dir, 'Assets', 'alexalogo.png') # In the same directory where the script is, it goes through the assets folder and access the png.
file_path = os.path.join(script_dir, 'randomJokes.txt') # Locates the file within the folder and stores it in an accessible variable.

# Functions
def cleardisplay(): # Clears the textbox display.
    t1.config(state="normal") # Unlocks the textbox
    t1.delete("1.0", END) # Deletes what's in the textbox.
    t1.config(state="disabled") # Locks the textbox

def clearElements(): # Clears the element in the frame.
    for item in f1.winfo_children(): # Goes through f1's children or elements.
        item.forget() # Clears the current elements in the frame.

def displayMenu(): # Responsible for displaying the first menu.
    clearElements()
    for item in start: # Goes through start variable that store's the game's start elements.
        item.pack(pady=(25,0)) # Packs the element in the frame.

def displayJoke(): # Responsible for displaying the jokes in the textbox.
    global punchline # Makes punchline variable available globally

    cleardisplay() # Clears the textbox before new content is inserted.    
   
    with open (file_path) as file_handler: # Opens the file through "with open" and assigns it as "file_handler."
        jokes = [joke.rstrip() for joke in file_handler.readlines()] # Using for-loop to take a line in the text and then strips it afterwards stores it in the variable.
        randomjoke = random.choice(jokes) # Using random module, I get to store a random line in a randomjoke variable to be used.
        if "?" in randomjoke: #If the randomjoke has a question mark:
            question, punchline = randomjoke.split('?', 1) #The line that has the question mark is placed in question, and punchline is stored separately.               
    
    t1.config(state="normal") # Unlocks the textbox
    t1.insert(END, f"{question}?\n") # Inserts the joke.
    t1.config(state="disabled") # Locks the textbox

def thejoke():
    global punchline # Gives access to the punchline.

    b3.forget() # Hides the "Why?" button when the punchline is present.
    b4.pack(pady=(10,0)) # Adjusts the close button's position
    b2.pack(pady=(5,0)) # Shows the "Alexa Tell Me A Joke" button to regenerate a joke.

    cleardisplay() # Clears the display before showing the punchline.

    t1.config(state="normal") # Unlocks the textbox
    t1.insert(END, f"{punchline}\n") # Inserts the joke.
    t1.config(state="disabled") # Locks the textbox

def displayGame(): # Responsible for displaying the 'game'.
    
    cleardisplay() # Clears the textbox display.
    displayJoke() # Displays the joke.
    clearElements() # Clears the current elements in the frame.

    for item in menu: # Goes through the menu's variables.
        if item == t1: # If it is the textbox, it is packed normally.
            item.pack() 
        if item == b3: # If it is the first button, it is packed with specific distance from the textbox.
            item.pack(pady=(10,0))
        if item == b4: # If it is the second button, it is packed with slight distance from the other button.
            item.pack(pady=(5,0))
###############################################
displayMenu() # Displays the menu automatically.
root.mainloop()  # Runs the Tkinter GUI