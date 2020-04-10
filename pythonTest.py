from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Main\\Desktop\\크롤링\\driver\\chromedriver.exe')

driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
