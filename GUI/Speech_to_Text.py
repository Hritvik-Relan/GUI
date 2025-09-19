from tkinter import *
import speech_recognition
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

root=Tk()
root.title("Speech to Text")
root.geometry("800x400")

heading1= Label(root, text = "Voice Notepad", font = ("Cursive", 30, "bold"))
heading1.grid(row=0, column=1, padx=20, pady=20)

label1= Label(root, text="click button to record your speech")
label1.grid(row=1, column=1, padx=10)

output_text=Text(root, height=4, width=40)
output_text.grid(row=1, column=1, pady=20, padx=20)

def Translate():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Speak Anything")
        audio= r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            text="sorry, could not compute"
        output_text.delete(1.0, END)
        output_text.insert(END, text)
    
def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(output_text.get(1.0, END), file=fout)
    else:
        messagebox.showinfo("Warning, the file was not saved")
    
trans_btn = Button(root, text="CLICK on me!!... \n To start recording", command=Translate)
trans_btn.grid(row=1, column=0, pady=20, padx=20)

save_btn= Button(root, text="Save the text", command=save)
save_btn.grid(row=1, column=2, pady=10, columnspan=3)

root.mainloop()