#Mandotory Modules
from tkinter import *
from gtts import gTTS
#System Compatability
import os
from tkinter.ttk import *

root=Tk()

#Outer Frame
frame1= Frame(root, bg="lightpink", height= "150")
frame1.pack(fill=X)

#Inner Frame
frame2=Frame(root, bg="hotpink", height="750")
frame2.pack(fill=X)

#Main Label
label=Label(frame1, text="Text to Speech", font="bold, 30", bg="lightpink")
label.place(x=180, y=70)

#Entry Box
entry = Entry(frame2, width=45, bd=4, font=14)
entry.place(x=130, y=52)
entry.insert(0, "")

#Language Entry
langvar = StringVar()
s=Combobox(root, textvariable=langvar, width=5)
s["values"]=("en.ca", "es", "fr-ca", "el", "hi", "ja", "ru")
#Translator
def play():
    language= s.get()
    
    #Saves the Entry
    myobj = gTTS(text=entry.get(), lang= language, slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")

#Submission Button
btn= Button(frame2, text="SUBMIT", width="15", pady=10, font="bold", command=play, bg= "purple")
btn.place(x=250, y=130)

root.title("Text_to_Speech_Converter")
root.geometry("650x550")

root.mainloop()