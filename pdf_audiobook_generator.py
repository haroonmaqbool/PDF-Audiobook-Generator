import pyttsx3
import PyPDF2
from tkinter import filedialog

book_path = filedialog.askopenfilename()

with open(book_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
