from tkinter import *
import webbrowser

def open__graven_channel():
    webbrowser.open_new("https://www.youtube.com/watch?v=jfKfPfyJRdk")

# first windows 
window = Tk()

#skin window
window.title("President")
window.geometry("960x800") #size of window
window.minsize(500, 500)
window.iconbitmap(r'img\imgTitle.ico')

window.config(background='#128c0b')

#Background 
# ↓ test amelioration Background
#/////////////////////////////////////////////////////////
#width = 300
#heigt = 300
#image = PhotoImage(file="bg.jpg").zoom(35).subsample(32)
#canvas = Canvas(window, width=width, height=height)
#canvas.create_image(width/2 , height/2, image)
#canvas.pack(expand=YES)
#/////////////////////////////////////////////////////////
#base d'intégration image
#↓ intégration image 
#photo = PhotoImage(file=r'img\bg.png')
#labelphoto = Label(window, image=photo)    
#labelphoto.pack()
#////
canva = Canvas(window, width=500, height=500)
img = PhotoImage(file="D:\\Bureau\\taffe\\projetPython\\President\\tk(pythonGraphique)\\img\\bg.png")
canva.create_image(140, 20, anchor=NW, image=img)
canva.place(x=0,y=0)

#add frame 
frame = Frame(window, bg='#128c0b', bd=3, relief=SUNKEN)
 
# add text
label_title = Label(frame, text="Welcom to game, President or Trouffiant", font=('courrier', 30), bg='#128c0b', fg='#09423E')
label_title.pack()

#Start button 
start_button = Button(frame, text="Party beggin",  font=('courrier', 30), bg='#128c0b', fg='#09423E', command=open__graven_channel)
start_button.pack(fill=X)

#add
frame.pack()

# print window
window.mainloop() 