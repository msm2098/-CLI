from imlist import *

cookie_dict = {}
def reuse_cookie_test(url):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=options)
    
    driver.get(url)
    driver.maximize_window()
    print("백준 아이디 비번 입력")
    ID=str(input("ID :"))
    PW=str(input("PW :"))
    driver.find_element(By.NAME,'login_user_id').send_keys(ID)
    driver.find_element(By.NAME,'login_password').send_keys(PW)
    driver.find_element(By.XPATH,'//*[@id="submit_button"]').click()
    print(driver.get_cookies)
    
    _cookies = driver.get_cookies()
    global cookie_dict 
    for cookie in _cookies:
        cookie_dict [cookie['name'] ] = cookie['value']
    print(cookie_dict)
    
    session = requests.Session()
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    print("변경전헤더출력")
    print (session.headers)
    print("변경전쿠키출력")
    print(session.cookies)
    session.headers.update(headers)
    print("변경후헤더출력")
    print(session.headers)
    session.cookies.update(cookie_dict)
    print("변경후쿠키출력")
    print(session.cookies)
    
    res = session.get('https://www.acmicpc.net')
    soup = BeautifulSoup(res.text,'html.parser')
    with open ('test.txt','w',encoding='utf-8') as f:
        f.write(soup.text)
    with open ('cookiesabe.txt','w',encoding='utf-8') as f:
        f.write(str(cookie_dict))
    info = soup.find_all('a',id = 'username')
    print(info)
    #driver.quit()

reuse_cookie_test("https://www.acmicpc.net/modify")

