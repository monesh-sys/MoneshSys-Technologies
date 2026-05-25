import PyPDF2

def read_pdf(pdf_path):

    pages = []

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

    return pages