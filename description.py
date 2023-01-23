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

    
    problem= descript.text
    problem2=problem[problem.find("problem-text"):]
    problem3=problem2[:problem2.find("</")]
    problem4=problem3[problem3.find("p>"):problem3.find("</")]
    print("문제:",problem3[23:problem3.find("</")])
    '''
    problemlen=len("problem-text")+5
    problem2n=(int(problem.find("<")))
    print("문제: ",problem2[problemlen:problem2n])
    print(problem)'''


