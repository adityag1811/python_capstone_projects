#Using Tkinter and what you have learnt about building GUI applications with Python,
# build a desktop app that assesses your typing speed. Give the user some sample text
# and detect how many words they can type per minute.###

from tkinter import *
import time
import random
TIME = 20
timer = 20
timer_started = False

current_words = []
word_list = []
typed_list = []

score = 0

typing_words = [
    "cat", "dog", "sun", "sky", "car", "bus", "hat", "pen", "cup", "box",
    "map", "bag", "bed", "key", "run", "sit", "red", "top", "day", "sea",
    "toy", "fox", "cow","book", "tree", "home", "road", "door", "fish", "bird", "milk", "cake", "ball",
    "hand", "foot", "face", "hair", "game", "park", "ship", "boat", "rain", "snow",
    "wind", "fire", "star", "moon", "apple", "table", "chair", "house", "plant", "grass",
    "river", "beach", "bread", "water", "smile", "happy", "laugh", "light", "sound", "music",
    "dance", "dream", "heart", "green", "brown", "black", "white", "clean", "fresh", "sweet",
    "salad", "grape", "lemon", "mango", "peach", "onion", "carrot", "toast", "pizza", "pasta",
    "spoon", "plate", "glass", "clock", "watch", "phone", "mouse", "cable", "paper", "brush",
    "shirt", "pants", "shoes", "socks", "jacket", "towel", "soap", "beach", "field", "stone",
    "brick", "cloud", "storm", "chair", "couch", "floor", "frame", "photo", "drink", "juice",
    "sleep", "wrist", "elbow", "ankle", "voice", "quiet", "quick", "slow", "early", "later",
    "carry", "bring", "catch", "throw", "write", "read", "learn", "teach", "share", "thank",
    "trust", "smile","school", "teacher", "student", "picture", "library",
    "morning", "rainbow", "traffic", "blanket", "birthday",
    "computer", "keyboard", "backpack", "exercise", "building"
]

# User Interface Setup
window = Tk()
window.title("Check your Typing Speed!")
window.minsize(500, 500)

my_label = Label(window, text="Assess your typing speed!\nWe have given a bunch of words!\nType as many as you can within a minute to get your score!,\nRemember: Press Enter key after each word you have typed!", fg="black")
my_label.configure(font=("Arial", 15))
my_label.pack(padx=20, pady=20)

my_word = Label(window, text="Enter your word!", fg="black")

#Picking up random words from the list of words
# scoring the correct entries

def scorecard():
    global score
    for i in range(len(typed_list)):
        if typed_list[i] == current_words[i]:
            score += 1
    time_label.configure(text=f"Time : {TIME} seconds\n"
                              f"Total Words Typed : {len(typed_list)}\n"
                              f"Correct Words : {score}\n"
                              f"Wrong Words :{len(typed_list)-score}\n"
                              f"Accuracy : {(score/len(typed_list)*100):.2f}%\n"
                              f"Correct WPM : {score/TIME*60}"  )

# word selection
def word_selection():
    global current_words
    global word_list
    if len(typed_list) % 4 == 0:
        word_list = random.sample(typing_words,4)
        my_word.config(text=f"Word List : \n{' '.join(word_list)}", fg='black', font=("Arial", 15))
        my_word.pack(padx=20,pady=20)
        for words in word_list:
            current_words.append(words)
        print(current_words)

# capture entered words in a seperate list and displaying them

def save_words(events):
    global timer_started
    word = text_input.get().strip()
    if (
            word == ""
            or word == "Enter the word here...."
            or word == "Please enter a text before clicking spacebar...."
    ):
        text_input.delete(0, END)
        text_input.configure(fg="grey")
        text_input.insert(0,"Please enter a text before clicking spacebar....")
        return
    # if word in typed_list:
    #     text_input.delete(0, END)
    #     text_input.configure(fg="grey")
    #     text_input.insert(0, f"This word '{word}' has already been typed before....")
        return
    if not timer_started:
        countdown()
        timer_started = True
    typed_list.append(word)
    if len(typed_list) % 4 == 0:
        word_selection()
    text_input.delete(0, END)
    print(typed_list)

# setting up placeholders

def clear_placeholder(events):
    if text_input.get() == "Enter the word here....":
        text_input.delete(0, "end")
        text_input.configure(fg="black")



# countdown timer

def countdown():

    global timer
    if timer > 0:
        timer -= 1
        time_label.config(text=f"Timer : {timer}")
        if timer > 0:
            window.after(1000, countdown)
        else:
            time_label.config(text="Time is up!\nLet's fetch your scores!")
            text_input.config(state="disabled")
            scorecard()



word_selection()


text_input = Entry(window, width=50,fg="grey")
text_input.insert(0,"Enter the word here....")
text_input.bind("<FocusIn>", clear_placeholder)
text_input.bind("<space>", save_words)
text_input.pack(padx=20, pady=20)


time_label = Label(window, text=f"Timer: {timer}", fg="black")
time_label.pack(padx=20, pady=20)

window.mainloop()