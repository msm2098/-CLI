'''from imlist import *
from main import session
from description import url
def disting():
    dis=session.get(url)
    soup=BeautifulSoup(dis.content,'html.parser')
    print(soup.select("problem-label problem-label-ac"))'''