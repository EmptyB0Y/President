from tkinter import *
import webbrowser

def open__graven_channel():
    ("https://www.youtube.com/watch?v=jfKfPfyJRdk")
    
# first windows 
window = Tk()

childImage = None

def openNewWindow():
    newWindow = Toplevel(window)
    
    # sets the title of the
    newWindow.title("President")
    # sets the geometry of toplevel
    newWindow.geometry("1200x800")
    newWindow.minsize(1200, 800)
    newWindow.maxsize(1200, 800)
    newWindow.iconbitmap(r'img\imgTitle.ico')
    newWindow.config(background='#000')
    
    
     # A Label widget to show in toplevel
    Label( newWindow, text ="President or Trouffiant", font=('courrier', 30), bg='#128c0b', fg='#09423E').pack()
    img = PhotoImage(file="img/bg.png")
    canva2 = Canvas(newWindow, width=img.width() , height=img.height(), bd=-5, relief=FLAT )
    canva2.create_image(0, 0, anchor=NW, image=img)
    canva2.place(x=265,y=60)
    #add frame 
    frame = Frame(newWindow, bg='#128c0b', bd=3, relief=FLAT)
    
    
    player_button = Button(frame, text="Player 1",  font=('courrier', 30), bg='#128c0b', fg='#09423E', command=openNewWindow)
    player_button.pack( side = LEFT, expand = True, fill = BOTH)
    # player_button.pack(fill=X)
    
    player2_button = Button(frame, text="Player 2",font=('courrier', 30), bg='#128c0b', fg="red", command=openNewWindow)
    player2_button.pack(side = LEFT, expand = True, fill = BOTH)
    
    player3_button = Button(frame, text="Player 3",font=('courrier', 30), bg='#128c0b', fg="blue", command=openNewWindow)
    player3_button.pack(side = LEFT, expand = True, fill = BOTH )

    player4_button = Button(frame, text="Player 4", font=('courrier', 30), bg='#128c0b', fg="black", command=openNewWindow)
    player4_button.pack( side = RIGHT, expand = True, fill = BOTH)
    
    frame.pack()
    global childImage
    childImage = PhotoImage(file=path)
    
    
    
    
    
    

#skin window
window.title("President")
window.geometry("1200x800") #size of window
window.minsize(1200, 800)
window.maxsize(1200, 800)
window.iconbitmap(r'img\imgTitle.ico')

window.config(background='#000')



#////
img = PhotoImage(file="./img/bg.png")
canva = Canvas(window, width=img.width() , height=img.height(), bd=-5, relief=FLAT )
canva.create_image(0, 0, anchor=NW, image=img)
canva.place(x=265,y=60)


#add frame 
frame = Frame(window, bg='#128c0b', bd=3, relief=FLAT)
 
# add text
label_title = Label(frame, text="Welcom to game, President or Trouffiant", font=('courrier', 30), bg='#128c0b', fg='#09423E')
label_title.pack()

#Start button 
start_button = Button(frame, text="Party beggin",  font=('courrier', 30), bg='#128c0b', fg='#09423E', command=openNewWindow)
start_button.pack(fill=X)

#add
frame.pack()

# print window
window.mainloop() 