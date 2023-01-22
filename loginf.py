from imlist import *
from bs4 import BeautifulSoup as bs
from imlist import headers
#from main import user_id,user_pw

cookie_dict = {}
def login(url):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=options)
    driver.get(url)
    ID='msm4754'
    PW='qwer0422'
    driver.find_element(By.NAME,'login_user_id').send_keys(ID)
    driver.find_element(By.NAME,'login_password').send_keys(PW)
    driver.find_element(By.XPATH,'//*[@id="submit_button"]').click()
    wait=WebDriverWait(driver,60)
    wait.until(EC.title_contains("정보 수정"))
    driver.get("https://www.acmicpc.net")
    _cookies=driver.get_cookies()
    global cookie_dict
    for cookie in _cookies:
        cookie_dict [cookie['name'] ] = cookie['value']

    driver.quit()