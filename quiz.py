import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = (
            "When did the first World War start?",
            "Which is the oldest civilization in the world?",
            "Who is called the Napoleon of Iran?",
            "Which is the last dynasty in China?",
            "Who is the first president of the United States?",
            "In which year was John F. Kennedy assassinated?"
        )

        self.options = (
            ("A. 1914", "B. 1913", "C. 1912", "D. 1911"),
            ("A. Mesopotamia", "B. Greece", "C. Egypt", "D. Indus Valley Civilization"),
            ("A. Genghis Khan", "B. Hannibal Barca", "C. Nader Shah", "D. Kublai Khan"),
            ("A. Shang Dynasty", "B. Zhou Dynasty", "C. Xia Dynasty", "D. Qing Dynasty"),
            ("A. James Monroe", "B. George Washington", "C. Thomas Jefferson", "D. John Adams"),
            ("A. 1962", "B. 1963", "C. 1763", "D. 1762")
        )

        self.answers = ("A", "A", "C", "D", "B", "B")
        self.guesses = []
        self.score = 0
        self.question_number = 0
        self.correct_option_index = None  # Index of the correct answer

        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 10), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=10)

        self.update_question()

    def update_question(self):
        if self.question_number < len(self.questions):
            self.question_label.config(text=self.questions[self.question_number])
            self.correct_option_index = ord(self.answers[self.question_number]) - ord('A')
            for i in range(4):
                self.option_buttons[i].config(text=self.options[self.question_number][i], bg="white")

    def check_answer(self, option_index):
        guess = chr(ord('A') + option_index)
        self.guesses.append(guess)

        if guess == self.answers[self.question_number]:
            self.score += 1
            self.root.config(bg="green")  # Correct answer background color
        else:
            self.root.config(bg="red")  # Wrong answer background color

        if self.question_number < len(self.questions) - 1:
            self.next_question()
        else:
            self.show_result()

    def next_question(self):
        self.question_number += 1
        self.update_question()

    def show_result(self):
        result = f"Your score is: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Result", result)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
