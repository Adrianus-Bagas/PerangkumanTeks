import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from summarizer import Summarizer,TransformerSummarizer
GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")

window = Tk()
window.title("Perangkuman Teks")
window.geometry("800x500")
window.config(background='black')

def gpt():
    inp = inputtxt.get(1.0, "end-1c")
    full = ''.join(GPT2_model(inp, min_length=60))
    outputtxt.insert(END,full)

label1 = tk.Label(window, text = "Masukkan Teks",bg="black",fg="white")
label1.pack()

inputtxt = tk.Text(window,
                   height = 10,
                   width = 50)
  
inputtxt.pack()

b0=Button(text="Rangkum", width=12,bg='white',command=gpt)
b0.pack()

label2 = tk.Label(window, text = "Hasil Rangkuman",bg="black",fg="white")
label2.pack()

outputtxt = tk.Text(window,
                   height = 10,
                   width = 50)
  
outputtxt.pack()

window.mainloop()