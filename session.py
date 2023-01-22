from imlist import *
from loginf import cookie_dict

session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookie_dict)

res = session.get('https://www.acmicpc.net')
soup = BeautifulSoup(str(res.text),'html.parser')
with open ('logintest.txt','w',encoding='utf-8') as f:
    f.write(soup.text)