import requests
from bs4 import BeautifulSoup as bs
login_url= "https://codeup.kr/login.php"
print("코드업")
ID=input("ID: ")
PW=input("PW: ")
login_info={"user_id":ID,"password":PW}
with requests.session() as s:
    login_req=s.post(login_url,data=login_info)
    print(login_req.status_code)

    get_myinfo=s.get("https://codeup.kr/userinfo.php?user="+str(ID))
    mod_info=s.get("https://codeup.kr/modifypage.php")
    soup=bs(mod_info.text,'html.parser')
    print(soup.text)
    '''soup=bs(get_myinfo.text,'html.parser')
    title=soup.select("body > main > div.container.mt-2 > blockquote")
    content=soup.select("body > main > div.container.mt-2 > div.row > div.col-md-12.col-lg-4")
    print(title[0].text)
    print(content[0].text)'''
    