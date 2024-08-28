import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")
root.configure(bg="lightblue")

# Random number to guess
n = random.randint(1, 100)
guse = 0

# Function to check the user's guess
def check_guess():
    global guse
    guse += 1
    try:
        a = int(entry.get())
        if a > n:
            result_label.config(text="Lower number please:", fg="red")
        elif a < n:
            result_label.config(text="Higher number please:", fg="blue")
        else:
            result_label.config(text="Congratulations! You've guessed the number!", fg="green")
            messagebox.showinfo("Congratulations!", f"You've guessed the number {n} correctly in {guse} attempts!")
            reset_game()
    except ValueError:
        result_label.config(text="Please enter a valid number", fg="orange")

def reset_game():
    global n, guse
    n = random.randint(1, 100)
    guse = 0
    entry.delete(0, tk.END)
    result_label.config(text="Guess the number between 1 and 100", fg="black")

# GUI layout
instructions = tk.Label(root, text="Guess the number between 1 and 100", font=("Arial", 14), bg="lightblue")
instructions.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 14), bg="yellow")
guess_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()






# import random
# n=random.randint(1, 100)
# a=-1
# guse=0
# while(a!=n):
#  guse+=1
#  a=int(input("Guess the number :"))
#  if(a> n):
#     print("Lower number please :")
#  else:
#      print("Higher number please")
# print(f"you have guess the number correctly in  {guse}  attmpt")  