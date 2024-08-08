import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By
import pyautogui 
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pyautogui.FAILSAFE = False

meeting_ID = ''
password = ''
name = ''
zoom_email_id = ''
zoom_password = ''
meeting_file = 'zoom_info.txt'
pass_file = 'credentials.txt'

def get_meeting_info():
    # takes in the meeting info and stores it into zoom_info file
    global meeting_ID, password, name
    name = input('ENTER YOUR NAME : ')
    meeting_ID = input('ENTER YOUR MEETING ID : ')
    password = input('ENTER YOUR MEETING PASSWORD : ')
    with open(meeting_file, 'w') as file:
        file.write(f"{name}\n{meeting_ID}\n{password}")
    return name, meeting_ID, password

def load_meeting_info():
    #loads the info from zoom_info file into the variables 
    global meeting_ID, password, name
    with open(meeting_file, 'r') as file:
        name = file.readline().strip()
        meeting_ID = file.readline().strip()
        password = file.readline().strip()
    return name, meeting_ID, password

def load_credentials():
    #loads the credentials from the credentials file into the variables 
    global zoom_email_id, zoom_password
    with open(pass_file, 'r') as file:
        zoom_email_id = file.readline().strip()
        zoom_password = file.readline().strip()
    return zoom_email_id, zoom_password

def get_credentials():
    # takes in the credentials from you and stores in the credentials file
    global zoom_email_id, zoom_password
    zoom_email_id = input("Enter your user ID: ")
    zoom_password = input("Enter your password: ")
    with open(pass_file, 'w') as file:
        file.write(f'{zoom_email_id}\n{zoom_password}')
    return zoom_email_id, zoom_password
def login_google():
# allows user to login vai google 
    global zoom_email_id, zoom_password , meeting_ID , password , name
    driver = webdriver.Chrome()
    driver.get('https://zoom.us/')
    sign_in_element = driver.find_element(By.XPATH, '//*[@id="black-topbar"]/div/ul/li[8]/a').click()

def non_signin_func():
    # joins zoom meeting without any credentials 
    try:
        global meeting_ID, password, name
        driver = webdriver.Chrome()
        driver.get('https://zoom.us/')
        join_element = driver.find_element(By.XPATH, '//*[@id="black-topbar"]/div/ul/li[6]/a').click() 
        id_element = driver.find_element(By.XPATH, '//*[@id="join-confno"]').send_keys(meeting_ID)
        join_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[2]/div/div[3]/form/div[3]/div').click()
        time.sleep(2)
        pyautogui.press("enter")
        launch = driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div').click()
        time.sleep(2)
        pyautogui.press('enter')
        browser_launch = driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a').click()
        time.sleep(2)
        driver.switch_to.frame("webclient")
        password_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
        name_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/input').send_keys(name)
        join_audio = driver.find_element(By.XPATH, '//*[@id="preview-audio-control-button"]').click()
        final_join = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/button').click()
        time.sleep(20)
        driver.close()
    except Exception as e:
        print(f"Error occurred: {e}")

def sign_in():
    try:
        global zoom_email_id, zoom_password , meeting_ID , password , name
        driver = webdriver.Chrome()
        driver.get('https://zoom.us/')
        sign_in_element = driver.find_element(By.XPATH, '//*[@id="black-topbar"]/div/ul/li[8]/a').click()
        zoom_email_element = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(zoom_email_id)
        zoom_pass_element = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(zoom_password)
        driver.find_element(By.XPATH, '//*[@id="js_btn_login"]').click()
        time.sleep(10)

        driver.find_element(By.XPATH , ' //*[@id="btnJoinMeeting"]').click()
        driver.find_element(By.XPATH , '//*[@id="join-confno"]').send_keys(meeting_ID)
        driver.find_element(By.XPATH , '//*[@id="btnSubmit"]').click()
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        driver.find_element(By.XPATH, '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div').click()
        time.sleep(2)
        pyautogui.press('enter')
        driver.find_element(By.XPATH , '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a').click()
        time.sleep(2)
        driver.switch_to.frame("webclient")
        driver.find_element(By.XPATH ,'//*[@id="input-for-pwd"]').send_keys(password)
        driver.find_element(By.XPATH , '//*[@id="root"]/div/div[1]/div/div[2]/button').click()

        time.sleep(50)
        driver.close()
    except Exception as e:
        print(f'Error occurred: {e}')

def is_meeting_info_present():
    return os.path.getsize(meeting_file) == 0

def is_credentials_info_present():
    return os.path.getsize(pass_file) == 0

def main():
    global meeting_ID, password, name, zoom_email_id, zoom_password
    print('''
           

 _                        _ _                                           
| | ____ _ _ __ _ __ ___ (_) | __    _______   ___  _ __ ___   ___ _ __ 
| |/ / _` | '__| '_ ` _ \| | |/ /   |_  / _ \ / _ \| '_ ` _ \ / _ \ '__|
|   < (_| | |  | | | | | | |   <     / / (_) | (_) | | | | | |  __/ |   
|_|\_\__,_|_|  |_| |_| |_|_|_|\_\___/___\___/ \___/|_| |_| |_|\___|_|   v.1
                                                 BY - BHAVYA NEGI
        



''')
    if is_meeting_info_present():
        get_meeting_info()
    else:
        answer = input('Meeting info already present. Do you wish to proceed with the same info? Y/N: ')
        if answer in ['Y', 'y']:
            load_meeting_info()


        else:
            get_meeting_info()
    
    if is_credentials_info_present():
        key = input('Do you wish to log in to your Zoom account? Y/N: ')
        if key in ['y', 'Y']:
            get_credentials()
            load_credentials
            sign_in()
        else:
           non_signin_func() 
            
    else:
        key2 = input('Do you wish to login into your zoom account ? Y/N : ')
        if key2 in ['y','Y']:
          key3 = input('CREDENTAILS FOUND , DO YOU WISH TO USE THE SAME ZOOM ACCOUNT? Y/N: ')
              
          if key3 in ['y' , 'Y']:
              load_credentials()
              sign_in()
          else:
              get_credentials()
              load_credentials()
              sign_in()
        else :
            non_signin_func()

if __name__ == "__main__":
    main()
