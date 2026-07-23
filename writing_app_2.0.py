from tkinter import *


TIMER = 5
remaining_time = 5
timer_id = None
countdown_id = None

def key_pressed(event):
    print("key pressed")
    restart_timer()

def time_ended():
    print("Too slow, everything has been erased!")
    text_box.delete('1.0',"end")

def restart_timer():
    global timer_id, countdown_id, remaining_time

    remaining_time = TIMER

    print("Timer started")

    # Cancel the previous erase timer
    if timer_id is not None:
        window.after_cancel(timer_id)

    # Cancel the previous countdown
    if countdown_id is not None:
        window.after_cancel(countdown_id)

    # Start a new erase timer
    timer_id = window.after(TIMER * 1000, time_ended)

    # Start a new countdown
    update_countdown()

def update_countdown():
    global remaining_time, countdown_id

    time_label.config(text=f"Time left: {remaining_time}")

    if remaining_time > 0:
        remaining_time -= 1
        countdown_id = window.after(1000, update_countdown)




window = Tk()
window.title("Writing App")
window.geometry("800x700")
window.configure(background="white")

top_label = Label(window,text='Start writing....\n'
                              'But remember, if you dont type anything for 5 seconds,'
                              '\nthe entire written content disappears forever ;-)',bg='white')
top_label.config(font=('Arial',15))
top_label.pack(pady=15)

text_box = Text(window,
                bg='white',
                width=80,
                height=20,)

text_box.bind("<Key>",key_pressed)
text_box.configure(font=('Arial',15),fg="grey")
text_box.pack(padx=10,pady=10)

time_label = Label(window,
                   text=f"Time left: {remaining_time}",
                   bg='white')
time_label.config(font=('Arial',15),fg="black")
time_label.pack(padx=10, pady=20)

window.mainloop()