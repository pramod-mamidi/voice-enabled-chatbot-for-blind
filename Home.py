from tkinter import *
from tkinter.ttk import *
from speak import SpeakText
import tkinter
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
import nltk
nltk.download('stopwords')
chatbot=ChatBot('my_bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
from bot import bot_start
root = Tk()
root.title("Home")
root_color = "white"
root.configure(bg = root_color)
def thing():
    print("starting")
    bot_start(chatbot)

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
style = Style()
style.configure('TButton', background = root_color,highlightthickness = 0,bd = 0)
speech_btn=PhotoImage(file='last mike final.png')
logo=PhotoImage(file='envision.png')
style.map('TButton')
app=FullScreenApp(root)
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "WHITE BACKGROUND.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
lab=Label(root,image=logo)
lab.place(height=40,width=330,x=530,y=20)
btn = Button(root,image=speech_btn,command=thing)
btn.pack(pady=20)
btn.place(height=225,width=225,x=530,y=200)
root.mainloop()
