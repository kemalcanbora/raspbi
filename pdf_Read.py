from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io,os
import unicodedata


def pdfparser(data,pdf_name,dic_q_key):
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    try:
        PDFPage.get_pages(fp)

        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            data = retstr.getvalue()
            data = data.replace("diﬃculty","difficulty")
            data = unicodedata.normalize("NFKD", data)
        dic_q_key=dic_q_key.replace(" ","_")
        dic_q_key=dic_q_key+"_txt"

        if not os.path.exists(dic_q_key):
            os.makedirs(dic_q_key)

        pdf_name=pdf_name.replace(" ","_")
        pdf_name = pdf_name.replace(".pdf", ".txt")

        with open(dic_q_key+'/'+pdf_name, "w") as text_file:
            text_file.write(data)
    except:
        pass


