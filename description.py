from imlist import *
from session import session_class
page = 0
csrfkey = 'a'

def choose_page():
    global page
    choose=int(input("문제 선택 : "))
    page=choose

def show_des():
    global page
    url="https://www.acmicpc.net/problem/"+str(page)
    dessession = session_class()
    dessession.update_session()
    descript = dessession.session.get(url)
    title= descript.text
    titlelen=len("problem_title")+2
    title2=title[title.find("problem_title"):]
    title2n=(int(title2.find("<")))
    print(str(page)+"번 문제:",title2[titlelen:title2n])

    desc = BeautifulSoup(descript.content,"html.parser")
    problem4=desc.select_one("#problem_description").get_text()
    problem4=problem4.replace("\n","")
    problem4=problem4.replace("\t","")
    print("-----------------------------------문제-----------------------------------------")
    print(problem4)

    problem_input = BeautifulSoup(descript.content,"html.parser")
    problem_input2 = problem_input.select_one("#problem_input").get_text()
    problem_input2 = problem_input2.replace("\n",'')
    problem_input2 = problem_input2.replace("\t",'')
    print("\n-----------------------------------입력-----------------------------------------")
    print(problem_input2)

    problem_output = BeautifulSoup(descript.content,"html.parser")
    problem_output2 = problem_output.select_one("#problem_output").get_text()
    problem_output2 = problem_output2.replace("\n",'')
    problem_output2 = problem_output2.replace("\t",'')
    print("\n-----------------------------------출력-----------------------------------------")
    print(problem_output2)

    problem_exinput = BeautifulSoup(descript.content,"html.parser")
    problem_exinput2 = problem_exinput.select_one("#sample-input-1").get_text()
    problem_exinput2 = problem_exinput2.replace("\n",'')
    problem_exinput2 = problem_exinput2.replace("\t",'')
    print("\n-----------------------------------예제입력-------------------------------------")
    print(problem_exinput2)   

    problem_exoutput = BeautifulSoup(descript.content,"html.parser")
    problem_exoutput2 = problem_exoutput.select_one("#sample-output-1").get_text()
    problem_exoutput2 = problem_exoutput2.replace("\n",'')
    problem_exoutput2 = problem_exoutput2.replace("\t",'')
    print("\n-----------------------------------예제출력-------------------------------------")
    print(problem_exoutput2)
    print("\n--------------------------------------------------------------------------------")
    
    

def submit():
    global page
    global csrfkey
    submit_url="https://www.acmicpc.net/submit/"+str(page)
    subsess = session_class()
    subsess.update_session()
    sub_page=subsess.session.get(submit_url)
    sub=desc = BeautifulSoup(sub_page.content,"html.parser")

    ckey=sub.find('input', {'name': 'csrf_key'})['value']
    path="submit/"+str(page)+".cpp"
    with open(path, 'r') as f:
        code = f.read()
    csrfkey=ckey
    submit_data={'problem_id' : page , 
    'language' : 84 ,
    'code_open' : 'onlyaccepted',
    'source' : code,
    'csrf_key' : csrfkey
    }
    subsess.session.post(submit_url,submit_data)


