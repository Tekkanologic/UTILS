'''
Simple script that merges two pdf files into a single file
'''

import os
from pyPDF2 import PdfFileMerger, PdfFileReader

PATH = " "
output = PdfFileMerger()

for file in os.listdir(PATH):
    file_path = os.path.join(PATH, file)
    if os.path.isfile(file_path):
        try:
            pdf_file = PdfFileReader(file)
            output.append(pdf_file)
        except IOError:
            pass

output.write("merged.pdf")