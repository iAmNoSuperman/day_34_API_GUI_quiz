from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}",
                           font=("Arial", 10, "bold"), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, background="white")
        self.quiz_question = self.question_canvas.create_text(150, 125, text="Quiz question goes here", width=280,
                                                              font=("Arial", 20, "italic"),
                                                              fill=THEME_COLOR)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.quiz_question, text=question_text)
        else:
            self.question_canvas.itemconfig(self.quiz_question, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
