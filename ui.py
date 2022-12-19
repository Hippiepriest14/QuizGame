from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR,
                                                     font=("Arial", 12, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.true, command=self.tru)
        self.button_true.grid(row=2, column=0)

        self.false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.false, command=self.fls)
        self.button_false.grid(row=2, column=1)

        self.label = Label(text=f"Score: 0", background=THEME_COLOR, fg="White")
        self.label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:

            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz!")
            self.canvas.config(bg="white")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def fls(self):
        self.feedback(self.quiz.check_answer("False"))

    def tru(self):
        self.feedback(self.quiz.check_answer("True"))

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500,self.get_next_question)
