import tkinter as tk
from tkinter import messagebox
import random

class MathPuzzleGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Math Puzzle Game")
        master.geometry("500x400")
        master.configure(bg="#f0f8ff")  # Light blue background

        self.score = 0
        self.attempts = 0
        self.max_attempts = 3

        # Title
        self.title_label = tk.Label(master, text="🎯 Math Puzzle Challenge", font=("Comic Sans MS", 22, "bold"), bg="#f0f8ff", fg="#333399")
        self.title_label.pack(pady=10)

        # Score Frame
        self.score_frame = tk.Frame(master, bg="#dcdcdc", bd=2, relief="ridge")
        self.score_frame.pack(pady=10)
        self.score_label = tk.Label(self.score_frame, text=f"Score: {self.score}", font=("Arial", 16), bg="#dcdcdc")
        self.score_label.pack(padx=10, pady=5)

        # Puzzle Frame
        self.puzzle_frame = tk.Frame(master, bg="#ffffff", bd=3, relief="groove")
        self.puzzle_frame.pack(pady=15)
        self.puzzle_label = tk.Label(self.puzzle_frame, text="", font=("Arial", 24, "bold"), bg="#ffffff")
        self.puzzle_label.pack(padx=20, pady=20)

        # Entry Frame
        self.entry_frame = tk.Frame(master, bg="#f0f8ff")
        self.entry_frame.pack(pady=10)
        self.entry = tk.Entry(self.entry_frame, font=("Arial", 16), width=10, justify="center")
        self.entry.pack(side="left", padx=10)
        self.submit_btn = tk.Button(self.entry_frame, text="Submit", font=("Arial", 14, "bold"), bg="#333399", fg="white", command=self.check_answer)
        self.submit_btn.pack(side="left", padx=5)

        # Hint label
        self.hint_label = tk.Label(master, text=f"You have {self.max_attempts} attempts", font=("Arial", 12), bg="#f0f8ff", fg="green")
        self.hint_label.pack(pady=10)

        self.new_puzzle()

    def new_puzzle(self):
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)
        self.operator = random.choice(["+", "-", "*"])
        if self.operator == "+":
            self.answer = self.a + self.b
        elif self.operator == "-":
            self.answer = self.a - self.b
        else:
            self.answer = self.a * self.b

        self.puzzle_label.config(text=f"{self.a} {self.operator} {self.b} = ?")
        self.attempts = 0
        self.hint_label.config(text=f"You have {self.max_attempts} attempts")
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_answer(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            self.entry.delete(0, tk.END)
            return

        self.attempts += 1

        if guess == self.answer:
            self.score += 1
            messagebox.showinfo("🎉 Correct!", f"Well done! Your score is now {self.score}")
            self.update_score()
            self.new_puzzle()
        else:
            if self.attempts < self.max_attempts:
                attempts_left = self.max_attempts - self.attempts
                hint = self.get_hint(guess)
                self.hint_label.config(text=f"Wrong! Hint: {hint} | Attempts left: {attempts_left}")
            else:
                messagebox.showinfo("Game Over", f"Out of attempts! The correct answer was {self.answer}")
                self.new_puzzle()

        self.entry.delete(0, tk.END)

    def get_hint(self, guess):
        # Provide hints based on the guess
        if guess < self.answer:
            return "Try a higher number"
        else:
            return "Try a lower number"

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = MathPuzzleGame(root)
    root.mainloop()