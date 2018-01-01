from pdf_Read import pdfparser
from arxiv_f import get_information_arxiv
from summary import summ
import os
from lex_sum import lex_summary

q_key="tensorflow"
# get_information_arxiv(q_key=q_key)
arr = os.listdir(q_key)
#
# for i in range(len(arr)):
#     pdfparser(data=q_key+"/"+arr[i],
#               pdf_name=arr[i],
#               dic_q_key=q_key+"_txt")


for i,item in enumerate(arr):
    ozet=lex_summary(file=str(q_key+"_txt"+"/"+arr[i]+".txt"))
    print(ozet)
    print("-------")