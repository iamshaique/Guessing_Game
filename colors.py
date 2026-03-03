import tkinter as tk
from tkinter import messagebox
import random

# Extended list of colors with hex codes
colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "orange": "#FFA500",
    "purple": "#800080",
    "pink": "#FFC0CB",
    "brown": "#A52A2A",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "lime": "#00FF00",
    "navy": "#000080",
    "teal": "#008080",
    "maroon": "#800000",
    "olive": "#808000",
    "coral": "#FF7F50",
    "gold": "#FFD700",
    "salmon": "#FA8072",
    "violet": "#EE82EE",
    "indigo": "#4B0082"
}

class ColorGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Color Guessing Game with Hints")
        self.attempts = 0
        self.max_attempts = 5
        self.color_name, self.color_hex = random.choice(list(colors.items()))

        self.label = tk.Label(master, text="Guess the color!", font=("Arial", 18))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(master, width=200, height=200, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=10)
        self.color_block = self.canvas.create_rectangle(10, 10, 190, 190, fill=self.color_hex)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.entry.focus()

        self.submit_btn = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        self.hint_label = tk.Label(master, text=f"You have {self.max_attempts} attempts.", font=("Arial", 12))
        self.hint_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().strip().lower()
        self.attempts += 1

        if guess == self.color_name:
            messagebox.showinfo("Correct!", f"🎉 You guessed it right! The color was {self.color_name.capitalize()}.")
            self.reset_game()
        else:
            if self.attempts < self.max_attempts:
                attempts_left = self.max_attempts - self.attempts
                hint = self.get_hint()
                self.hint_label.config(text=f"Wrong! Hint: {hint} | Attempts left: {attempts_left}")
            else:
                messagebox.showinfo("Game Over", f"Out of attempts! The correct color was {self.color_name.capitalize()}.")
                self.reset_game()

        self.entry.delete(0, tk.END)

    def get_hint(self):
        # Provide hints based on attempt number
        if self.attempts == 1:
            # First letter hint
            return f"Starts with '{self.color_name[0].upper()}'"
        elif self.attempts == 2:
            # Length of color name
            return f"Contains {len(self.color_name)} letters"
        elif self.attempts == 3:
            # Last letter hint
            return f"Ends with '{self.color_name[-1].upper()}'"
        elif self.attempts == 4:
            # Reveal first two letters
            if len(self.color_name) > 1:
                return f"Starts with '{self.color_name[:2].capitalize()}'"
            else:
                return f"Starts with '{self.color_name[0].upper()}'"
        else:
            return ""

    def reset_game(self):
        self.attempts = 0
        self.color_name, self.color_hex = random.choice(list(colors.items()))
        self.canvas.itemconfig(self.color_block, fill=self.color_hex)
        self.hint_label.config(text=f"You have {self.max_attempts} attempts.")
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x400")
    game = ColorGuessingGame(root)
    root.mainloop()