import arxiv
import os,shutil

def get_information_arxiv(q_key):
    keys=arxiv.query(search_query=q_key,max_results=3)

    print(keys)

    if not os.path.exists(q_key):
        os.makedirs(q_key)

    for i in range(len(keys)):
        print(keys[i]["authors"])
        print(keys[i]["pdf_url"])
        print(keys[i]["title"])
        print("----------")
        try:
            arxiv.download(keys[i])
            shutil.move(keys[i]["title"]+".pdf", q_key)
        except:
            os.remove(keys[i]["title"]+".pdf")
