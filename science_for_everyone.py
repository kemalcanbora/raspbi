from pdf_Read import pdfparser
from arxiv_f import get_information_arxiv
from send_mail import send_email
import os
from lex_sum import lex_summary_2
from pprint import pprint
from create_pdf import create_pdf_page
import pandas as pd

def main(q_key):
    get_information_arxiv(q_key=q_key,f_max_results=10)
    q_key=q_key.replace(" ","_")
    arr = os.listdir(q_key)

    for i in range(len(arr)):
        pdfparser(data=q_key+"/"+arr[i],
                  pdf_name=arr[i],
                  dic_q_key=q_key)

    arr_txt = os.listdir(q_key+"_txt")
    print(arr_txt)

    liste=[]
    pdf_link_lst=[]
    path_z=str(q_key+"_txt")

    for i,item in enumerate(arr_txt):
        ozet=lex_summary_2(file_path=path_z+"/"+arr_txt[i])
        print(ozet)
        pdf_link=str(q_key+"_txt"+"/"+arr_txt[i])
        liste.append(ozet)
        pdf_link_lst.append(pdf_link)
        print("-------")
    #
    dataframe=pd.DataFrame({"text":liste,
                            "pdf_link":pdf_link_lst,
                            })
    print(dataframe)

    create_pdf_page(full_name=q_key,address_parts=["kemalcanbora@gmail.com"],metin=dataframe)


    send_email(
            gmail_user="tuulrik@gmail.com",
            gmail_pwd="",
            send_to="kemalcanbora@gmail.com",
            subject= q_key+" özetler",
            text=" Akademik özet geç ",
            path="form_letter.pdf"
            )

main(q_key="sentiment analysis")