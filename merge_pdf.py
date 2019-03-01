import os
from PyPDF2 import PdfFileMerger

filepath = '/Users/test/Downloads/books'
pdfs = [filepath + "/"+ f for f in os.listdir(filepath)]

merger = PdfFileMerger()



for i in range(len(pdfs)):
    pdf = [x for x in pdfs if x.endswith(('_' +  str(i) + '.pdf'))][0]
    print (pdf)
    merger.append(open(pdf, 'rb'))



with open(os.path.join(filepath,'full_book.pdf'), 'wb') as fout:
    merger.write(fout)
