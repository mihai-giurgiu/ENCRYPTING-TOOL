import tkinter as tk
import AnotherCrypt
from decimal import Decimal 

HEIGHT = 700
WIDTH = 800


root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#669999')
frame.place(relx=0.5, rely =0.1, relwidth = 0.75, relheight= 0.5, anchor = 'n')

entry = tk.Entry(frame, font = 30)
entry.place(relwidth = 0.65, relheight= 0.1, rely = 0.05, relx = 0.02)

button = tk.Button(frame, text = "Encrypt password", font = "30", command = lambda: test_function(entry.get()))
button.place(relx = 0.69,rely = 0.05, relheight = 0.1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#c1d7d7')
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')


text = tk.Label(lower_frame,text= "", font = "30")
text.place(relwidth = 0.65, relheight= 0.1, rely = 0.05, relx = 0.02)

def test_function(entry):
   result = AnotherCrypt.encrypt(entry,"AesPassword")
   print("The entry is: ", result)
   text.configure(text=result)
   
root.mainloop()