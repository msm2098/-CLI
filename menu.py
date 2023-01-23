from description import show_des
def menulist():
    while True:
        print("1:문제집 선택")
        print("2:문제 선택")
        print("3:문제 풀기")
        print("4:종료")
        index = int(input("선택:"))
        if(index==1):
            pass
        elif(index==2):
            show_des()
        elif(index==3):
            pass
        elif(index==4):
            break;