# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window


from tkinter.ttk import Progressbar
bar = Progressbar(window, length=200)


# Add a label with the text "Hello"
lbl = Label(window, text="Hello", font =("Arial Bold", 100))
firstlbl = Label(window, text="Hey", font =("Arial Bold", 50))
# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
firstlbl.grid(column=0, row=1)

btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=0)

btn = Button(window, text="Yes")
 
btn.grid(column=1, row=0)


chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Pick me!', var=chk_state)
 
chk.grid(column=0, row=0)

spin = Spinbox(window, from_=0, to=100, width=5)
 
spin.grid(column=1,row=2)

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 25
 
bar.grid(column=0, row=2)

menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='Jimmy')
 
menu.add_cascade(label='New', menu=new_item)
 
window.config(menu=menu)

txt = Entry(window,width=10)
 
txt.grid(column=1, row=1)

window.mainloop()     # Keep the window open
