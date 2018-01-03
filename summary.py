from lexrank import LexRank
from lexrank.mappings import STOPWORDS
from path import Path


def summ(doc_dir_path,ozetlenecek_txt):
    myfile=ozetlenecek_txt
    documents = []
    documents_dir = Path(doc_dir_path)
    for file in documents_dir.files('*.txt'):
        with file.open(mode='rt', encoding='utf-8') as fp:
            documents.append(fp.readlines())
    lxr = LexRank(documents, stopwords=STOPWORDS['en'])

    with open (myfile, "r") as myfile:
        sentences = myfile.readlines()


    # sentences = nltk.sent_tokenize(sentences)
    summary = lxr.get_summary(sentences, summary_size=15, threshold=.1)
    return (summary)

city = 'Ribeir\ufb02\xa3o Preto'
# print (city.encode("iso-8859-1").decode("utf-8"))
# print(city.decode('utf-8').encode('cp850','replace').decode('cp850'))

import json
a=json.loads(city.read())
print(a)