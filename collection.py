from imlist import *
from session import *
from tabulate import tabulate

choose=0
def choose_collection():
    while True:
        print("1.POSCAT Summer Study1 : 1")
        print("2.POSCAT Summer Study2 : 2")
        print("3.POSCAT Summer Study3 : 3")
        pc = int(input("선택 : "))
        collectpagein =0
        if pc == 1:
            collectpagein = 131
            print("선택된 문제집 : POSCAT Summer Study1\n")
            break
        elif pc ==2:
            collectpagein=132
            print("선택된 문제집 : POSCAT Summer Study2\n")
            break
        elif pc ==3:
            collectpagein=133
            print("선택된 문제집 : POSCAT Summer Study3\n")
            break
        else:
            print("잘못된 입력..")
    global choose
    choose=collectpagein

def show_problems():
    global choose
    global page
    colurl="https://www.acmicpc.net/workbook/view/"+str(choose)
    colsession = session_class()
    colsession.update_session()
    collection_page=colsession.session.get(colurl)
    problems=collection_page.text
    table = pd.read_html(problems, header=0, encoding='utf-8')[0]
    tableset = table[['문제','문제 제목','정답 비율']]
    tabulate.WIDE_CHARS_MODE = False
    print(tabulate(tableset, headers='keys', tablefmt='fancy_grid', showindex=False,numalign='center')) 