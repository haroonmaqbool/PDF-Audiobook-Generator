import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

selected_file = askopenfilename()

pdf_reader = PyPDF2.PdfFileReader(selected_file)

num_pages = pdf_reader.numPages

for page_num in range(0, num_pages):
    page = pdf_reader.getPage(page_num)
    text = page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
