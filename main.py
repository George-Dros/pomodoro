from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="Timer",fg =PINK)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break, Good job!", fg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Take a breather", fg= GREEN)

    else:
        count_down(work_sec)
        title_label.config(text="Pomodoro, Go!", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps

    count_minute  = math.floor(count / 60)
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#Initialize window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=GREEN)


#Timer Label
title_label = Label(text="Timer", font=(FONT_NAME,24,"bold"),bg=GREEN, fg =PINK)
title_label.grid(row=0,column=1)

#Image
canvas = Canvas(width=200, height =224, bg=GREEN, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


#Buttons
button = Button(text="Start!",font=(FONT_NAME,12,"bold"),command=start_timer)
button.grid(row=2,column=0)

button = Button(text="Reset",font=(FONT_NAME,12,"bold"),command=timer_reset)
button.grid(row=2,column=2)

#Checkmarks
check_marks = Label(bg=GREEN)
check_marks.grid(row=3,column=1)

window.mainloop()