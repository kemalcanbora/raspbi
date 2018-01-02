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
