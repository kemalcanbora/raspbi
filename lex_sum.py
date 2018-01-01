#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in
from pprint import pprint

doc = []

def lex_summary(file):
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary = summarizer(parser.document, 5) #Summarize the document with 5 sentences
    deneme=[]
    for sent in summary:
        deneme.append(str(sent))
    a=''.join(deneme)
    return a

# a='''/home/kb/PycharmProjects/raspbi/tensorflow_txt/TensorFlow Agents: Efficient Batched Reinforcement Learning in
#   TensorFlow.pdf.txt'''
# lex_summary(a)