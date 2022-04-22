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
checks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checks
    window.after_cancel(timer)
    reps = 0
    checks = ""
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps 
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%2==1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps ==8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    print("timer has started. Tic-Toc")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global checks
    #take current count [s] and format into time format
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min < 10 and count_sec<10:
        count_text = f"0{count_min}:0{count_sec}"
    elif count_sec<10:
        count_text = f"{count_min}:0{count_sec}"
    elif count_min < 10:
        count_text = f"0{count_min}:{count_sec}"
    else:
        count_text = f"{count_min}:{count_sec}"
    #update display
    canvas.itemconfig(timer_text, text=count_text)
    if count>0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start()
        if reps %2 ==0:
            checks += "✓"
            check_label.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_pic)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



start_button = Button(text="Start", command=start,  highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button =Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font= ("Arial", 50))
timer_label.grid(row=0, column=1)

check_label = Label(text="", fg=GREEN, bg=YELLOW, font=("Arial", 30, "bold"))
check_label.grid(row=3, column=1)






window.mainloop()