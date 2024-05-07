#Core	Metadata treatment, create and add comments.
from pathlib import Path
from pypdf import PdfReader, PdfWriter


#Pages processing	Split, rotate, remove, shuffle, dynamically watermark, and convert into images.
# Content processing	Extract tabular data, images, and hyperlinks, annotate text, redact text and parse text data.
# Document processing
# Merge multiple PDFs, convert PDF to other files types,
# compress, secure, crack, digitally sign, manipulate scanned PDF,
# compute the checksum, and pinpoint the difference between two PDFs.

class MyPDFReader:
    def __init__(self,file_name_arg='multilang.pdf'):
        folder = Path(__file__).parent.parent
        file_name = folder / f'data/{file_name_arg}'
        print(file_name)
        self.file = PdfReader(file_name)
        print(self.file)

    def get_page_count(self):
        return len(self.file.pages)

    def get_meta_data(self):
        return dict(self.file.metadata)

    def get_images(self):
        if self.file.pages:
            return self.file.pages[0].images





x = MyPDFReader('AutoCad_Diagram.pdf')

print(x.get_page_count())
print(x.get_meta_data())
print(len(x.get_images()))
