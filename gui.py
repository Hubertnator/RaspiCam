import tkinter as tk

win_width = 600
win_height = 400
filepath = ""

MainWin = tk.Tk()
MainWin.title("Raspi Security Cam")
MainCanvas = tk.Canvas(MainWin,width=600,height=90)
MainCanvas.create_text(300,15, text='Welcome to Raspi Security Cam.',font=('Calibri',22))
MainCanvas.create_text(300,45, text='Type file path of the video:',font=('Calibri',22))
MainCanvas.pack()

#MainMenu
menubar = tk.Menu(MainWin)

#input & label
file_input_label = tk.Label(MainWin, width=100, height=100, text="File path: ")

file_input_label.pack()
file_input = tk.Entry(MainWin,width=200,height=200)
file_input.pack()

file_input.insert(0,"helo")
