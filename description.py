from imlist import *
from session import session_class


def show_des():
    dessession = session_class()
    dessession.update_session()
    descript = dessession.session.get(url)
    title= descript.text
    titlelen=len("problem_title")+2
    title2=title[title.find("problem_title"):]
    title2n=(int(title2.find("<")))
    print(str(page)+"번 문제:",title2[titlelen:title2n])


