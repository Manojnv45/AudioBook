import pyttsx3
import PyPDF2
import pdftotext
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
book = open(file_path, 'rb')
pdfReader = pdftotext.PDF(book)

# fileName = input("Enter full file path")
# book = open(fileName, 'rb')
# pdfReader = pdftotext.PDF(book)

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 140)

start = int(input("Enter Page no where to start :"))
end = int(input("Enter Page no where to End :"))

for page in range(start, end):
    print(page)
    speaker.say(pdfReader[page])
    print(pdfReader[page])
    speaker.runAndWait()
    print('Hello')
