#imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#requried details --help from https://stackoverflow.com/users/5016547/joseph238
ser = Service(".\chromedriver")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#requried details END

#initilizing chrome
driver = webdriver.Chrome(service=ser, options=options)

#opening the link
driver.get('https://web.whatsapp.com/')

#this input statement will help in stopping the window until the main page is open(whatsaap)
input('Press enter after scanning')

#finding and clicking the element
text_box = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
button = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')

def message(text):#it will type the message
    text_box[0].send_keys(text)

def send():# it will press the enter key
    text_box[0].send_keys(u'\ue007')

#send messages
for i in range(300):
    message("happy new year bhai!!")
    send()
