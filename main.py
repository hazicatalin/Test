import time

from selenium import webdriver


# This should work without any problem
def test1():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://politrip.com/account/sign-up")
    firstName = driver.find_element_by_id("first-name")
    lastName = driver.find_element_by_id("last-name")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("sign-up-password-input")
    confPassword = driver.find_element_by_id("sign-up-confirm-password-input")
    btn = driver.find_element_by_id(" qa_loader-button")

    firstName.send_keys('Andrei')
    time.sleep(1)
    lastName.send_keys('Popescu')
    time.sleep(1)
    email.send_keys('popescu_andrei@gmail.com')
    time.sleep(1)
    password.send_keys('PopAndrei123')
    time.sleep(1)
    confPassword.send_keys('PopAndrei123')
    time.sleep(1)
    btn.click()
    time.sleep(20)
    driver.quit()

#incorect email
def test2():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://politrip.com/account/sign-up")
    firstName = driver.find_element_by_id("first-name")
    lastName = driver.find_element_by_id("last-name")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("sign-up-password-input")
    confPassword = driver.find_element_by_id("sign-up-confirm-password-input")
    btn = driver.find_element_by_id(" qa_loader-button")

    firstName.send_keys('Andrei')
    time.sleep(1)
    lastName.send_keys('Popescu')
    time.sleep(1)
    email.send_keys('popescu_andrei')
    time.sleep(1)
    password.send_keys('PopAndrei123')
    time.sleep(1)
    confPassword.send_keys('PopAndrei123')
    time.sleep(1)
    btn.click()
    time.sleep(20)
    driver.quit()

#invalid first name and second name
def test3():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://politrip.com/account/sign-up")
    firstName = driver.find_element_by_id("first-name")
    lastName = driver.find_element_by_id("last-name")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("sign-up-password-input")
    confPassword = driver.find_element_by_id("sign-up-confirm-password-input")
    btn = driver.find_element_by_id(" qa_loader-button")

    firstName.send_keys('123')
    time.sleep(1)
    lastName.send_keys('23531')
    time.sleep(1)
    email.send_keys('popescu_andrei@gmail.com')
    time.sleep(1)
    password.send_keys('PopAndrei123')
    time.sleep(1)
    confPassword.send_keys('PopAndrei123')
    time.sleep(1)
    btn.click()
    time.sleep(20)
    driver.quit()

#password not matching
def test4():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://politrip.com/account/sign-up")
    firstName = driver.find_element_by_id("first-name")
    lastName = driver.find_element_by_id("last-name")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("sign-up-password-input")
    confPassword = driver.find_element_by_id("sign-up-confirm-password-input")
    btn = driver.find_element_by_id(" qa_loader-button")

    firstName.send_keys('Andrei')
    time.sleep(1)
    lastName.send_keys('Popescu')
    time.sleep(1)
    email.send_keys('popescu_andrei@gmail.com')
    time.sleep(1)
    password.send_keys('PopAndrei123')
    time.sleep(1)
    confPassword.send_keys('PopAndrei1234')
    time.sleep(1)
    btn.click()
    time.sleep(20)
    driver.quit()

#password not strong
def test5():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://politrip.com/account/sign-up")
    firstName = driver.find_element_by_id("first-name")
    lastName = driver.find_element_by_id("last-name")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("sign-up-password-input")
    confPassword = driver.find_element_by_id("sign-up-confirm-password-input")
    btn = driver.find_element_by_id(" qa_loader-button")

    firstName.send_keys('Andrei')
    time.sleep(1)
    lastName.send_keys('Popescu')
    time.sleep(1)
    email.send_keys('popescu_andrei@gmail.com')
    time.sleep(1)
    password.send_keys('popescuandrei')
    time.sleep(1)
    confPassword.send_keys('popescuandrei')
    time.sleep(1)
    btn.click()
    time.sleep(20)
    driver.quit()

def main():
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == "__main__":
    main()