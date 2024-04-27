import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, A):
        self.root = root
        self.root.title("Python Quiz Game")
        self.root.geometry("400x300")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London", "Rome"], "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "options": ["Mars", "Jupiter", "Saturn", "Earth"], "answer": "Jupiter"},
            {"question": "Which programming language is known as the 'language of the web'?", "options": ["Python", "Java", "HTML", "JavaScript"], "answer": "JavaScript"}
        ]
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda x=i: self.check_answer(x))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack(pady=5)

        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self, selected_option):
        selected_option_text = self.questions[self.current_question]["options"][selected_option]
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option_text == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Correct Answer!")
        else:
            messagebox.showerror("Incorrect", "Incorrect Answer!")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Quiz Finished! Your score is {self.score}")
            self.root.destroy()

        self.score_label.config(text=f"Score: {self.score}")

# Create the main Tkinter window
root = tk.Tk()
app = QuizApp(root)
root.mainloop()