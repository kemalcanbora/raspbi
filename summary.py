from lexrank import LexRank
from lexrank.mappings import STOPWORDS
from path import Path
from pprint import pprint
import nltk
import  numpy
documents = []
documents_dir = Path('bitcoin predictions_txt')
import pandas as pd


for file in documents_dir.files('*.txt'):
    with file.open(mode='rt', encoding='utf-8') as fp:
        documents.append(fp.readlines())
lxr = LexRank(documents, stopwords=STOPWORDS['en'])

myfile="/home/kb/PycharmProjects/raspbi/bitcoin predictions_txt/A Survey on Security and Privacy Issues of Bitcoin.pdf.txt"
with open (myfile, "r") as myfile:
    sentences = myfile.readlines()


# sentences = nltk.sent_tokenize(sentences)
summary = lxr.get_summary(sentences, summary_size=10, threshold=.1)
pprint(summary)
