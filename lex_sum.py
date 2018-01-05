from summarize import summarize

def lex_summary_2(file_path):
    try:
        print(file_path)
        with open(file_path) as file:
            data=file.read()
        text = summarize(data,sentence_count=10, language='english')
        a = ''.join(text)
        return (a)
    except:
        pass
        # import sys
        # print("Unexpected error:", sys.exc_info()[0])



