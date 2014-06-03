from Tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    if self.slogan['text']=='Hello':
        self.slogan.config(text='ASSHOLE')
    else:
        self.slogan.config(text='Hello')

root = Tk()
app = App(root)
root.mainloop()