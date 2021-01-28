from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

#Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()

#Введите email для регистрации
email = driver.find_element_by_css_selector("#reg_email")
email.send_keys("mail@mail.ru")

#Введите пароль для регистрации
password = driver.find_element_by_css_selector("#reg_password")
password.send_keys("QwE15987+A0")

#Нажмите на кнопку
register = driver.find_element_by_css_selector("#customer_login > div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
register.click()

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()

#Введите email и пароль для входа
email = driver.find_element_by_css_selector("#username")
email.send_keys("mail@mail.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("QwE15987+A0")

#Нажмите на кнопку
login = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
login.click()

#Проверка, что на странице есть элемент "Logout" отсутствует
