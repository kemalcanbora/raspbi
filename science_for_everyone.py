from pdf_Read import pdfparser
from arxiv_f import get_information_arxiv
import os

q_key="bitcoin predictions"
get_information_arxiv(q_key=q_key)
arr = os.listdir(q_key)

for i in range(len(arr)):
    pdfparser(data=q_key+"/"+arr[i],
              pdf_name=arr[i],
              dic_q_key=q_key+"_txt")