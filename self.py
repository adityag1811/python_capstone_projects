from tkinter import *
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter.filedialog import askopenfilename, asksaveasfilename,askdirectory

current_image = None

windows = Tk()
windows.title("Add watermark to images")
windows.minsize(400,400)

image_label = Label()
image_label.pack()

my_label = Label(windows,
                 text="Upload any image\n& add watermark to it!")
my_label.config(font=("Arial",15,"bold"))
my_label.pack(pady=(10,10))

def upload():
    global current_image
    open_file = askopenfilename()
    if not open_file:
        return
    current_image = Image.open(open_file)

    preview = current_image.copy()
    preview.thumbnail((400,400))

    tk_image = ImageTk.PhotoImage(preview)
    image_label.image = tk_image
    image_label.configure(image=tk_image)

    my_label.configure(text="Add the watermark\ntext in the box below!!")
    upload_button.pack_forget()
    watermark_entry.pack()
    watermark_button.pack(pady=(10,10))
    change_button.pack(pady=(5,5))
    watermark_entry.delete(0, END)
def watermark_text():
    global current_image

    if current_image is None:
        my_label.config(text="Please upload an image first!")
        return

    watermark_text = watermark_entry.get()
    draw = ImageDraw.Draw(current_image)
    draw.text((200,200),watermark_text,fill="white",font_size=100)

    preview = current_image.copy()
    preview.thumbnail((400,400))

    tk_image = ImageTk.PhotoImage(preview)
    image_label.image = tk_image
    image_label.config(image=tk_image,
                    pady=10)

    my_label.configure(text="Would you like to\nsave the file?")
    change_button.pack_forget()
    watermark_button.pack_forget()
    watermark_entry.pack_forget()
    save_button.pack(pady=(25,15))

def save_file():
    if current_image is None:
        return

    save_path = asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg"),
            ("All Files", "*.*")
        ]
    )

    if not save_path:
        return
    current_image.save(save_path)
    save_button.pack_forget()
    my_label.configure(text="Image file saved!!\nWould you like to watermark another image?")
    upload_button.pack(pady=(10,10))

upload_button = Button(text="Upload image!",
                       width= 15,
                       command=upload,
                       padx=15)

upload_button.pack()


watermark_entry = Entry(width=30)


watermark_button = Button(text="Watermark text!",
                          command=watermark_text)


save_button = Button(text="Save file!?",
                   command=save_file)

change_button = Button(text="Change Image!",
                     command=upload)





windows.mainloop()