# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--no-sandbox')
options.add_argument("--hide-scrollbars")
options.add_argument("disable-infobars")
options.add_argument('--disable-dev-shm-usage')
# How this scripts works?
# We have pre defined messages and a Image
# Which we will send via Keys
# The first task it performs after signing In
# is to search for contact whom we want to send message


# Here we will add all the contact numbers
# as the numbers name will be saved as number itself

# This can be a list of numbers, Which we will loop as object
target = "3099643"

# I need help here, I want this text to be in one message
# but each point to be on different lines,
# I tried using \n but that enters and send message
message = "Feeling bored at home, try this! • Earn 500 Rupees to 15,000 Rupees Monthly with cash bounces • Work from " \
          "anywhere(Remote) • Weekly payments via Easypaisaa, JazzCash or your Bank Account • No commitments • Work " \
          "at your own pace • No software installation or setup Required(You will work on Chrome browser) • Option to " \
          "choose between a range of small to big tasks • No hard Skills Required except know how to use a " \
          "computer/Laptop • Apply by emailing now using the template below\n "

# Same here, there are some points in this message
# where I need to it use \n and break line but 
# instead it sends the message
message0 = """Hello Snapthat, My Name is {Your Name Here}. I came across your add for data labeling tasks and I am 
interested to earn some extra money. I am a {Profession here/student}, I have a {computer/laptop} with Internet. I 
want to earn some extra money because {You reason here, can be anything, no need to overthink}. I have experience 
using these software on pcs: {any software name here, that you use, Windows or Os x operating systems are also 
softwares, again don't overthink} My contact number is: {You contact number} I will be waiting for a reply. Referred 
by Hassan Thank you, Regards, {Your Name} """

number_list = []

with open('num.txt', 'r') as file:
    for line in file.readlines():
        number_list.append(str(line).strip())

print(number_list)

# Driver to open a browser
# driver = webdriver.Firefox()
driver = webdriver.Chrome(options=options)
#
# # link to open WhatsApp
driver.get("https://web.whatsapp.com/")
#
# # 10 sec wait time to load
# # units in seconds
# # note this time is being used below also
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
input("Scan the QR code and then press Enter")


# searBoxPath = '//*[@id="input-chatlist-search"]'
# inputSearchBox = driver.find_element_by_class_name("ZP8RM")
# time.sleep(0.5)


def send_process(target_num):
    # click the search button to search contact
    inputSearchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div')
    time.sleep(1)
    inputSearchBox.click()
    time.sleep(1)

    inputSearchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    # inputSearchBox.clear()
    # inputSearchBox.send_keys(target[1:len(target) - 1])
    inputSearchBox.send_keys(target_num)
    print(f'Target Searched {target_num}')

    try:
        time.sleep(4)
        x_arg = '//span[contains(@class, "matched-text")]'
        # Select the target
        wait5.until(EC.presence_of_element_located((
            By.XPATH, x_arg
        )))
        driver.find_element_by_xpath(x_arg).click()
        print("Target Successfully Selected")
        time.sleep(2)
        # Pasting Image
        # Image must be in clipboard, this was the eassiest approach

        # Selecting the text box
        window = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        window.send_keys(Keys.META, 'v')
        time.sleep(2)

        # Selecting the send button
        windowpic = driver.find_element_by_xpath(
             '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        windowpic.click()
        # Select the Input Box
        # inp_xpath = '//div[contains(@class, "_13mgZ")]'
        # input_box = wait.until(EC.presence_of_element_located((
        # By.XPATH, inp_xpath)))
        # time.sleep(1)

        # Send message
        # target is contact name and message is message
        window.send_keys(message)
        time.sleep(1)
        window.send_keys(Keys.ENTER)
        window.send_keys(message0)
        time.sleep(1)
        window.send_keys(Keys.ENTER)
        print("Successfully Sent Message to : " + target + '\n')
    except Exception as error:
        print(f'Fail to select number ==> {target_num}')





for target_num in number_list:
    send_process(target_num)
