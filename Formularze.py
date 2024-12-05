import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

file= r"C:\\Users\neras\Desktop\OGŁOSZENIE\Python\ogloszenia\odswiez_ogl\Excel files\plik.xlsx"
sheet1 = pd.read_excel(file, sheet_name = 'ubrania_A_olx', usecols = "B:K")
sheet2 = pd.read_excel(file, sheet_name = 'Dane_log')
driver = webdriver.Chrome()
url  = sheet2.iloc[0,2] #wiersz 0, kolumna 2
passw = sheet2.iloc[0,1]
login = sheet2.iloc[0,0]
driver.get(url)
time.sleep(5)
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(login)
password_input.send_keys(passw)
time.sleep(5)
login_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(20)
for index, value in enumerate(sheet1, start=0):
        dodaj_ogloszenie_button = driver.find_element(By.CLASS_NAME, "css-w1ofum").click()
        time.sleep(15)
        value = sheet1.loc[index]
        title = driver.find_element(By.NAME, "title").send_keys(value['Tytuł'])
        print(index, value['Tytuł'], end= " ")
        time.sleep(5)
        photo1 = driver.find_element(By.XPATH, "//input[@id='1']").send_keys(value['ZD1'])
        print(value['ZD1'], end= " ")
        photo2 = driver.find_element(By.XPATH, "//input[@id='2']").send_keys(value['ZD2'])
        print(value['ZD2'], end=" ")
        photo3 = driver.find_element(By.XPATH, "//input[@id='3']").send_keys(value['ZD3'])
        print(value['ZD3'], end=" ")
        photo4 = driver.find_element(By.XPATH, "//input[@id='4']").send_keys(value['ZD4'])
        print(value['ZD4'], end=" ")
        photo5 = driver.find_element(By.XPATH, "//input[@id='5']").send_keys(value['ZD5'])
        print(value['ZD5'], end=" ")
        photo6 = driver.find_element(By.XPATH, "//input[@id='6']").send_keys(value['ZD6'])
        print(value['ZD6'], end=" ")
        photo7 = driver.find_element(By.XPATH, "//input[@id='7']").send_keys(value['ZD7'])
        print(value['ZD7'], end=" ")
        time.sleep(10)
        description = driver.find_element(By.ID, "description").send_keys(value['Opis'])  # przeslij opis
        driver.implicitly_wait(10)
        price_button = driver.find_element(By.XPATH, "//button[@data-testid='select-price']").click()
        price = driver.find_element(By.XPATH,"//input[@id='parameters.price.price']").send_keys(str(value['Cena']))
        print(value['Cena'],end= " ")
        time.sleep(2)
        button_state = driver.find_element(By.XPATH, "//button[@data-testid='dropdown-expand-button']").click()
        state = driver.find_element(By.XPATH, "//a[contains(text(), 'Używane')]").click()
        time.sleep(5)
        button_size = driver.find_element(By.XPATH, "//div[@data-cy='parameters.size']").click()
        size2 = driver.find_element(By.XPATH, "//a[contains(text(), '68')]").click()
        driver.implicitly_wait(10)
        button_gender = driver.find_element(By.XPATH, "//div[@data-cy='parameters.type']").click()
        girl = driver.find_element(By.XPATH, "//a[contains(text(), 'Dziewczęce')]").click()
        driver.implicitly_wait(10)
        auto_button = driver.find_element(By.XPATH, "//label[@class='switch__container css-1aye0mk']").click()
        driver.implicitly_wait(10)
        size_ship_button = driver.find_element(By.ID, "Band-M__toggle").click()
        driver.implicitly_wait(10)
        ship_orlen_button = driver.find_element(By.XPATH,"//input[@aria-label='RUCH package size M']").click()
        driver.implicitly_wait(10)
        ship_inpost_button = driver.find_element(By.XPATH,"//input[@aria-label='INPOST package size M']").click()
        driver.implicitly_wait(10)
        add_notice_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(15)
        dont_promote_button = driver.find_element(By.XPATH, "//button[@class='css-1e0wqje']").click()
        time.sleep(5)
        print()

