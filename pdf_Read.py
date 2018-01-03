from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io,os,sys


def pdfparser(data,pdf_name,dic_q_key):
    print(data)
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    # try:
    PDFPage.get_pages(fp)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()
        data=data.replace("ﬁ","fi")
        data=data.replace("ﬃ","fi")
        data=data.replace("ﬀe","fi")
        data=data.replace("ﬀa","fi")
        data = data.replace("ﬀu", "fi")
        data = data.replace("diﬀerent", "different")
        data = data.replace("reﬂects", "reflects")
        data=data.replace("diﬃculty","difficulty")


    dic_q_key=dic_q_key.replace(" ","_")
    dic_q_key=dic_q_key+"_txt"

    if not os.path.exists(dic_q_key):
        os.makedirs(dic_q_key)

    pdf_name=pdf_name.replace(" ","_")
    pdf_name = pdf_name.replace(".pdf", ".txt")
    sistem=sys.stdout.encoding
    print(sistem)
    with open(dic_q_key+'/'+pdf_name, "w") as text_file:
        text_file.write(data.encode("latin-1").decode("utf-8"))
        # text_file.write(str(data.encode('utf-8')))

    # except:
    #     print("cevirme ")
    #     pass
