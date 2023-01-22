from imlist import *
from bs4 import BeautifulSoup as bs
from loginf import login,cookie_dict
from imlist import headers

loginurl="https://www.acmicpc.net/modify"
mainurl="https://www.acmicpc.net"

login(loginurl)
session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookie_dict)

res = session.get('https://www.acmicpc.net')
soup = BeautifulSoup(str(res.text),'html.parser')
with open ('logintest.txt','w',encoding='utf-8') as f:
    f.write(soup.text)