import pyttsx3
from PyPDF2 import PdfReader

# Open the PDF file
book = open('oop.pdf', 'rb')
pdfReader = PdfReader(book)

# Get number of pages
pages = len(pdfReader.pages)
print(pages)

# Initialize text-to-speech engine
speaker = pyttsx3.init()

# Read from page 7 onwards
for num in range(7, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    if text:  # Check if text was extracted
        speaker.say(text)
        speaker.runAndWait()

