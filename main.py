import pyttsx3
from PyPDF2 import PdfReadersz

# Open the PDF file
book = open('bo.pdf', 'rb')
pdfReader = PdfReader(book)

# Get the total number of pages in the PDF
pages = len(pdfReader.pages)
print("Total pages:", pages)

# Extract text from each page of the PDF
text = ""
for page in pdfReader.pages:
    text += page.extract_text()

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Say the extracted text aloud
speaker.say(text)
speaker.runAndWait()
'''
ekhane single page r loop comment kora ase
for page in range(4, 7):  # Pages are zero-indexed, so page 5 is at index 4
    text += pdfReader.pages[page].extract_text()m
'''
