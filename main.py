from imlist import *
from loginf import login
from menu import menulist
from session import session_class

print("백준 CLI")
#user_id=input("ID :")
#user_pw=input("PW :")
if(len(cookie_dict)==0):
    print("로그인이 되어있지 않습니다 로그인 하시겠습니까?")
    while True:
        
        answer=str(input("Y/N: "))
        if(answer=='y' or answer == 'Y'):
            
            login("https://www.acmicpc.net/modify")
            main_session=session_class()
            main_session.update_session()
            res = main_session.session.get('https://www.acmicpc.net')
            welcome = BeautifulSoup(res.content,"html.parser")
            welcome2=welcome.select_one(".username").get_text()
            print("환영합니다",welcome2,"님")
            break
        elif(answer=="n" or answer == "N"):
            print("다른 기능을 사용하려면 로그인을 해야 합니다.")
            continue
        else:
            print("잘못된 입력 입니다.")
            continue
menulist()