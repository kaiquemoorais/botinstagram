from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


username = ' Seu email ou telefone aqui ' 
password = ' Sua sena aqui '

url = 'https://instagram.com/'

chrome = Chrome(ChromeDriverManager().install())
chrome.get(url)

sleep(3)
chrome.find_element(By.NAME, 'username').send_keys(username)
chrome.find_element(By.NAME, 'password').send_keys(password)
chrome.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
sleep(11)
chrome.get(url + 'neymarjr/followers/')
sleep(5)

d = 1; t = 0; n = 2
path = lambda n: f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[{n}]/div/div'

while True:
    sleep(0.30)
    try: chrome.find_element(By.XPATH, path(n) + f'[{d}]/div[3]/button').click(); d += 1
    except: t += 1; sleep(1) 
    if t == 3:
       for z in range(1, 10):
          if chrome.find_element(By.XPATH, path(n) + f'[{d - z}]/div[3]/button').text == 'Seguindo':
             chrome.get(url + chrome.find_element(By.XPATH, path(n) + f'[{d - z}]/div[2]/div/div/div/span').text + '/followers/' ); break
       d = 2; n = 1; t = 0
       sleep(5)