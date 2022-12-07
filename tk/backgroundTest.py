from tkinter import Tk, Button, Canvas, PhotoImage
from PIL import Image, ImageTk
 
fenetre = Tk()
 
# sert a ne pas avoir la bande noir en haut et en bas de la page en fullscreen
fenetre.attributes('-fullscreen', True)
 
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
 
image = Image.open("img/bg.png") # imageTest fait 270 x 200
 
image = image.resize((w, h))
 
# print(image) # <PIL.Image.Image image mode=RGBA size=1920x1080 at 0x43D5AB0>
 
photo = ImageTk.PhotoImage(image)
 
# pour que le canvas n'ai pas de bourdure qui reste autour
can = Canvas(fenetre, highlightthickness=0)
 
can.create_image(0, 0, anchor='nw', image=photo)
 
can.pack(fill='both', expand=1)
 
Button(can, text="Quitter", command=fenetre.destroy).pack()
 
fenetre.mainloop()