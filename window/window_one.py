''' window one '''
import tkinter as tk

window_one = tk.Tk()
window_one.geometry('500x500')
window_one.resizable(False, False)

frame_one = tk.Frame(window_one, width=250, height=160, bg='blue')
frame_two = tk.Frame(window_one, width=250, height=160)
frame_three = tk.Frame(window_one, width=250, height=165)
frame_four = tk.Frame(window_one, width=100, height=165)
frame_five = tk.Frame(window_one, width=400, height=165)
frame_six = tk.Frame(window_one, width=100, height=165)

frame_one.grid(row=0, column=0)
frame_two.grid(row=0, column=1)
frame_three.grid(row=1, column=0)
frame_four.grid(row=1, column=1)
frame_five.grid(row=2, column=0)
frame_six.grid(row=2, column=1)
