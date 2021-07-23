#Dice simulator

#requirements
# 1 GUI interface tkinter
# 2 random lib
# 3 images for pillow library import PIL

from tkinter import *
import PIL
from PIL import ImageTk, Image
import random

root=Tk()

root.title('Dice App')

root.geometry('400x400')

root.config(bg='#a4a6a6')


#default image for app
DEFAULT='images/die1.PNG'

#all images list
diceImages=['images/die1.PNG','images/die2.PNG','images/die3.PNG','images/die4.PNG','images/die5.PNG','images/die6.PNG']

#function to change the image
def rolling():
    new_image=random.choice(diceImages)
    change_dice=ImageTk.PhotoImage(Image.open(new_image))
    image_label.configure(image=change_dice)
    image_label.image=change_dice
    root.update()

#labeling default image
myimage=ImageTk.PhotoImage(Image.open(DEFAULT))

image_label=Label(root,image=myimage)

image_label.pack(expand=True)

#rolling button
roll_btn=Button(root,text='Roll',width=20,command=rolling)
roll_btn.pack(pady=20)


#keybinding
root.bind('<q>',lambda x:root.destroy())


root.mainloop()
