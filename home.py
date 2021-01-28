from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

#Проскрольте страницу на 600 пикселей вниз
driver.execute_script("window.scrollBy(0, 600);")

#Нажмите на название книги или на кнопку
name_book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
name_book.click()

#Нажмите на вкладку "Reviews"
reviews = driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a")
reviews.click()

#Поставьте 5 звезд
five_stars = driver.find_element_by_css_selector("#commentform > p.comment-form-rating > p > span > a.star-5")
five_stars.click()

#Заполните поле "Review" сообщением
message = driver.find_element_by_id("comment")
message.send_keys("Nice book!")

#Заполните поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("Anastasia")

#Заполите поле "Email"
email = driver.find_element_by_id("email")
email.send_keys("mail@mail.ru")

#Нажмите на кнопку
driver.execute_script("window.scrollBy(0, 600);")
submit = driver.find_element_by_css_selector("#submit")
submit.click()