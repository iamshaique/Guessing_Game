import tkinter as tk
from tkinter import messagebox
import random

# List of fruits
fruits = ["apple", "banana", "orange", "grape", "mango",
          "pineapple", "strawberry", "blueberry", "kiwi", "watermelon"]

class FruitGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Fruit Guessing Game")

        self.fruit = random.choice(fruits)
        self.attempt = 0
        self.max_attempts = 4

        # Instructions Label
        self.label = tk.Label(master, text="Guess one fruit from the list below:",
                              font=("Arial", 14))
        self.label.pack(pady=10)

        # Display fruit list
        self.fruits_label = tk.Label(master, text=", ".join(fruits), font=("Arial", 12))
        self.fruits_label.pack(pady=5)

        # Entry box for user guess
        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Submit button
        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        # Hint label
        self.hint_label = tk.Label(master, text="", font=("Arial", 12), fg="blue")
        self.hint_label.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        self.attempt += 1

        if guess == self.fruit:
            messagebox.showinfo("Result", "🎉 You Won! 🎉")
            self.reset_game()
            return
        else:
            if self.attempt == 1:
                self.hint_label.config(text=f"Hint 1: The fruit contains {len(self.fruit)} characters.")
            elif self.attempt == 2:
                hint = "*" * (len(self.fruit) - 1) + self.fruit[-1]
                self.hint_label.config(text=f"Hint 2: {hint}")
            elif self.attempt == 3:
                hint = self.fruit[0] + "*" * (len(self.fruit) - 1)
                self.hint_label.config(text=f"Hint 3: {hint}")
            else:
                messagebox.showinfo("Result", f"All attempts lost! The fruit was: {self.fruit}")
                self.reset_game()

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.fruit = random.choice(fruits)
        self.attempt = 0
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = FruitGuessingGame(root)
    root.mainloop()