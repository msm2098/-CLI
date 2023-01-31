from description import *
from collection import *
def menulist():
    while True:
        print("1:문제집 선택")
        print("2:문제 선택")
        print("3:문제 풀기")
        print("4:종료")
        index = int(input("선택:"))
        if(index==1):
            choose_collection()
        elif(index==2):
            show_problems()
            choose_page()
            show_des()
        elif(index==3):
            submit()
        elif(index==4):
            break;