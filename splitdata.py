import os
import shutil
import tkinter as tk
from PIL import Image, ImageTk

source_folder = "/run/user/1000/gvfs/sftp:host=192.168.18.190/home/umair/Desktop/Hamza/nimra/istock/istock_images1"
categories = ["Bed", "Other"]

for category in categories:
    category_path = os.path.join(source_folder, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

display_width = 600
display_height = 600

image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

image_index = 0

def move_to_category(event):
    global image_index
    image_file = image_files[image_index]
    image_path = os.path.join(source_folder, image_file)
    destination_path = os.path.join(source_folder, categories[current_category.get()], image_file)
    shutil.move(image_path, destination_path)
    image_index += 1
    show_next_image()

def show_next_image():
    if image_index < len(image_files):
        image_file = image_files[image_index]
        image_path = os.path.join(source_folder, image_file)

        img = Image.open(image_path)
        img = img.resize((display_width, display_height))

        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

root = tk.Tk()
root.title("Image Sorting")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame)
label.pack()

current_category = tk.IntVar()
current_category.set(0)

category_buttons = []

for i, category in enumerate(categories):
    button = tk.Radiobutton(frame, text=category, variable=current_category, value=i)
    button.pack()
    category_buttons.append(button)

root.bind("<Up>", lambda event: current_category.set((current_category.get() - 1) % len(categories)))
root.bind("<Down>", lambda event: current_category.set((current_category.get() + 1) % len(categories)))
root.bind("<Return>", move_to_category)

show_next_image()
root.mainloop()

print("Image sorting completed.")