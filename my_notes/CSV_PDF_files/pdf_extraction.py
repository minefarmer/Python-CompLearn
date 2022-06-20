'''             EXTRACTING INFO FROM A PDF
I cna use PyPDF2 to extract metadata and some text from a PDF.
Current types of data that can be extracted.
    Author
    Creator
    Producer
    Subject
    Title
    Number of pages
'''
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
   # f-strings (f""") is used for string formating in this example.        
    txt = f"""
    Information about {pdf_path}:
    
    Author: {information.auther}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path ='AsusLaptop.pdf'
    extract_information(path)  # Did not work because I do not have Microsoft word installed.
    