from imlist import *
from loginf import cookie_dict,login
print("백준 CLI")
#user_id=input("ID :")
#user_pw=input("PW :")
if(cookie_dict == None):
    print("로그인이 되어있지 않습니다 로그인 하시겠습니까?")
    while True:
        
        answer=str(input("Y/N: "))
        if(answer=='y' or answer == 'Y'):
            login("https://www.acmicpc.net/modify")
            break
        elif(answer=="n" or answer == "N"):
            print("다른 기능을 사용하려면 로그인을 해야 합니다.")
            break
        else:
            print("잘못된 입력 입니다.")
            continue
        
else:
    print("ㅎㅇ")