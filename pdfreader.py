import pyttsx3
import PyPDF2
from tkinter.filedialog import*

book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages

for num in range(0,pages):
    page=pdfreader.getPage(num)		//read file
    text=page.extractText()	//extract data from pdfs
    player=pyttsx3.init()	//start
    player.say(text)        //It will speak
    player.runAndWait()