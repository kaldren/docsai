from PyPDF2 import PdfReader

# Read PDF
reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)
page = reader.pages[0]
text = page.extract_text()
print (text)

# Send text to GPT to analyze
# Logic...

# Result