import arxiv
import os,shutil

def get_information_arxiv(q_key,f_max_results):

    keys=arxiv.query(search_query=q_key,
                     max_results=f_max_results,
                    )

    q_key=q_key.replace(" ","_")
    if not os.path.exists(q_key):
        os.makedirs(q_key)
    liste_link=[]
    for i in range(len(keys)):
        # print(keys[i]["authors"])
        # print(keys[i]["pdf_url"])
        # print(keys[i]["title"])
        # print("----------")

        liste_link.append(keys[i]["pdf_url"])

        try:
            arxiv.download(keys[i])
            shutil.move(keys[i]["title"]+".pdf", q_key)
        except:
            pass
            os.remove(keys[i]["title"]+".pdf")


