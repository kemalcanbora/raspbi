from pdf_Read import pdfparser
from arxiv_f import get_information_arxiv
from send_mail import send_email
import os
from lex_sum import lex_summary
from pprint import pprint
from create_pdf import create_pdf_page
import pandas as pd

q_key="time series"
getart=get_information_arxiv(q_key=q_key)
q_key=q_key.replace(" ","_")
arr = os.listdir(q_key)

for i in range(len(arr)):
    pdfparser(data=q_key+"/"+arr[i],
              pdf_name=arr[i],
              dic_q_key=q_key)

arr_txt = os.listdir(q_key+"_txt")

liste=[]
pdf_link_lst=[]
for i,item in enumerate(arr):
    ozet=lex_summary(file=str(q_key+"_txt"+"/"+arr_txt[i]))
    pprint(ozet)
    pdf_link=str(q_key+"_txt"+"/"+arr_txt[i])
    liste.append(ozet)
    pdf_link_lst.append(pdf_link)
    print("-------")
#
dataframe=pd.DataFrame({"text":liste,
                        "pdf_link":pdf_link_lst,
                        })
print(dataframe)

create_pdf_page(full_name="deneme",address_parts=["kemalcanbora@gmail.com"],metin=dataframe)


send_email(
        gmail_user="tuulrik@gmail.com",
        gmail_pwd=" ",
        send_to="kemalcanbora@gmail.com",
        subject= q_key+" özetler",
        text=" Akademik özet geç ",
        path="form_letter.pdf"
        )
