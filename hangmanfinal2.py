import random
from tkinter import *
from tkinter import messagebox

# Global variables
score = 0
lives = 6
game_over = False
guess_list = ["rose", "table", "charger", "phone", "band", "airpods", "chair","robot","laptop","race","cup","airconditioner","microwave","ganjichurail","husband","mistress","son","leeminho","keifer","aditikhoobsurat"]

# Tkinter setup
root = Tk()
root.geometry('905x700')
root.title('Hangman')
root.config(bg='#e0ffff')

# Load images from folder
image_path = "C:/Users/HP/Desktop/codealpha/hangman/"

# Letter images
letter_images = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in letters:
    try:
        letter_images[letter] = PhotoImage(file=f"{image_path}{letter}.png.png")
    except:
        print(f"Error: Image {letter}.png not found")

# Hangman images
hangman_images = []
for i in range(1, 8):
    try:
        img = PhotoImage(file=f"{image_path}h{i}.png")
        hangman_images.append(img)
    except:
        print(f"Error: Image h{i}.png not found")

# Hangman label
hangman_label = Label(root, bg="#e0ffff", image=hangman_images[0])
hangman_label.place(x=300, y=-50)

# Score label
score_label = Label(root, text=f"SCORE: {score}", bg="#e0ffff", font=("arial", 25))
score_label.place(x=10, y=10)

# Word display variables
display = []
word_labels = []
chosen_word = ""

def new_round():
    """Starts a new round of the game by resetting the word, lives, and dashes."""
    global chosen_word, display, word_labels, lives

    # Reset lives
    lives = 6
    hangman_label.config(image=hangman_images[0])

    # Choose new word
    chosen_word = random.choice(guess_list)
    display = ["_"] * len(chosen_word)

    # Remove old labels
    for lbl in word_labels:
        lbl.destroy()

    word_labels.clear()

    # Calculate center position for dashes
    x_start = (905 - (len(chosen_word) * 60)) // 2  

    # Create new dashes
    for i in range(len(chosen_word)):
        lbl = Label(root, text="_", bg="#e0ffff", font=("arial", 40))
        lbl.place(x=x_start + i * 60, y=450)
        word_labels.append(lbl)

    # Recreate buttons
    create_buttons()

# Function to check guessed letter
def check(letter, button):
    global lives, score
    
    button.destroy()  # Remove button after click
    
    if letter.lower() in chosen_word:
        for i, char in enumerate(chosen_word):
            if char == letter.lower():
                display[i] = letter
                word_labels[i].config(text=letter.upper())
        
        if "_" not in display:
            score += 1
            score_label.config(text=f"SCORE: {score}")
            ask_continue()  # Ask user if they want to continue
    else:
        lives -= 1
        hangman_label.config(image=hangman_images[6 - lives])  # Update hangman image
        
        if lives == 0:
            messagebox.showinfo('Game Over', 'You Lost! Better luck next time.')
            root.destroy()

# Function to ask the user if they want to continue or exit
def ask_continue():
    """Ask the user if they want to continue playing or exit."""
    answer = messagebox.askyesno('You Win!', 'Congratulations! 🎉\nDo you want to continue?')
    if answer:
        new_round()  # Start new round
    else:
        root.destroy()  # Exit game

# Centering calculations for buttons
window_width = 905
button_width = 50  # Approximate button width
gap = 10  # Space between buttons
row1_x_start = (window_width - (13 * (button_width + gap))) // 2  # Center first row
row2_x_start = (window_width - (13 * (button_width + gap))) // 2  # Center second row

# Adjusted button placement
button_data = [
    # First row (A-M)
    ['A', row1_x_start + 0 * (button_width + gap), 550],
    ['B', row1_x_start + 1 * (button_width + gap), 550],
    ['C', row1_x_start + 2 * (button_width + gap), 550],
    ['D', row1_x_start + 3 * (button_width + gap), 550],
    ['E', row1_x_start + 4 * (button_width + gap), 550],
    ['F', row1_x_start + 5 * (button_width + gap), 550],
    ['G', row1_x_start + 6 * (button_width + gap), 550],
    ['H', row1_x_start + 7 * (button_width + gap), 550],
    ['I', row1_x_start + 8 * (button_width + gap), 550],
    ['J', row1_x_start + 9 * (button_width + gap), 550],
    ['K', row1_x_start + 10 * (button_width + gap), 550],
    ['L', row1_x_start + 11 * (button_width + gap), 550],
    ['M', row1_x_start + 12 * (button_width + gap), 550],

    # Second row (N-Z)
    ['N', row2_x_start + 0 * (button_width + gap), 610],
    ['O', row2_x_start + 1 * (button_width + gap), 610],
    ['P', row2_x_start + 2 * (button_width + gap), 610],
    ['Q', row2_x_start + 3 * (button_width + gap), 610],
    ['R', row2_x_start + 4 * (button_width + gap), 610],
    ['S', row2_x_start + 5 * (button_width + gap), 610],
    ['T', row2_x_start + 6 * (button_width + gap), 610],
    ['U', row2_x_start + 7 * (button_width + gap), 610],
    ['V', row2_x_start + 8 * (button_width + gap), 610],
    ['W', row2_x_start + 9 * (button_width + gap), 610],
    ['X', row2_x_start + 10 * (button_width + gap), 610],
    ['Y', row2_x_start + 11 * (button_width + gap), 610],
    ['Z', row2_x_start + 12 * (button_width + gap), 610]
]

# Creating buttons
letter_buttons = {}  # Store buttons to recreate after each round

def create_buttons():
    
    global letter_buttons
    letter_buttons.clear()

    for letter, x, y in button_data:
        btn = Button(root, bd=0, bg="#e0ffff", activebackground="#e0ffff",
                     font=10, image=letter_images.get(letter, None))
        # Binding current values
        btn.config(command=lambda l=letter, b=btn: check(l, b))
        btn.place(x=x, y=y)
        letter_buttons[letter] = btn


# Exit button
def close():
    global game_over
    answer = messagebox.askyesno('Exit', 'Are you sure you want to quit?')
    if answer:
        game_over = True
        root.destroy()

exit_img = PhotoImage(file=f"{image_path}Exit.png")
exit_button = Button(root, bd=0, command=close, bg="#e0ffff", activebackground="#e0ffff", font=10, image=exit_img)
exit_button.place(x=770, y=10)

# Start the first round
new_round()

root.mainloop()
