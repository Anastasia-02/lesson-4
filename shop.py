import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
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

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Откройте книгу
book = driver.find_element_by_css_selector("#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3")
book.click()

#Тест, что заголовок называется
text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-181 > div.summary.entry-summary > h1"), "HTML5 Forms"))

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Введите email и пароль для входа
email = driver.find_element_by_css_selector("#username")
email.send_keys("mail@mail.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("QwE15987+A0")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Откройте категорию "HTML"
html = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19.current-cat > a")
html.click()

#Тест, что отображается 3 товара
test = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19.current-cat > span")
test_checked = test.get_attribute("3")
if test_checked is not None:
    print("Отображается 3 товара")
else:
    print("Отображается не 3 товара")

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Введите email и пароль для входа
email = driver.find_element_by_css_selector("#username")
email.send_keys("mail@mail.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("QwE15987+A0")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Тест, что в селекторе выбран вариант сортировки от большего к меньшему
test = driver.find_element_by_css_selector("#content > form > select")
select = Select(test)
select.select_by_value("price-desc")
test_price = test.get_attribute("value")
if test_price == "price-desc":
    print ("В селекторе выбрана сортировка от большего к меньшему")
else:
    print("В селекторе не выбрана сортировка от большего к меньшему")

#Отсортируйте товары от большего к меньшему
select = driver.find_element_by_css_selector("#content > form > select > option:nth-child(6)")
select.click()

#Тест, что в селекторе выбран вариант сортировки от большего к меньшему
test = driver.find_element_by_css_selector("#content > form > select")
select = Select(test)
select.select_by_value("price-desc")
test_price = test.get_attribute("value")
if test_price == "price-desc":
    print ("В селекторе выбрана сортировка от большего к меньшему")
else:
    print("В селекторе не выбрана сортировка от большего к меньшему")

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[3]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Введите email и пароль для входа
email = driver.find_element_by_css_selector("#username")
email.send_keys("mail@mail.ru")
password = driver.find_element_by_css_selector("#password")
password.send_keys("QwE15987+A0")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Откройте книгу
book = driver.find_element_by_css_selector("#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.outofstock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3")
book.click()

#Тест, что содержимое старой цены ₹600.00
price = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span")
price_text = price.text
assert price_text == "₹600.00"

#Тест, что содержимое новой цены ₹450.00
price_new = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span")
price_new_text = price_new.text
assert price_new_text=="₹450.00"

#Явное ожидание и нажать на обложку книги
picture = driver.find_element_by_css_selector("#product-169 > div.images > a > img")
time.sleep(10)
picture.click()

#Явное ожидание и закрыть предпросмотр
close = driver.find_element_by_css_selector("body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a")
close.click()

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[4]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Добавьте в корзину книгу
book = driver.find_element_by_css_selector("#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.outofstock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.ajax_add_to_cart")
book.click()

#Тест, что возле корзины количество товаров "1 Item", а стоимость "₹180.00"
basket_count = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
basket_count_text = basket_count.text
assert basket_count_text=="1 Item"
basket_price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
basket_price_text = basket_price.text
assert basket_price_text=="₹180.00"

#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli")
basket.click()

#Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
time.sleep(5)
subtotal = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span")
subtotal_text = subtotal.text
assert subtotal_text=="₹180.00"

#Используя явное ожидание, проверьте что в Total отобразилась стоимость
time.sleep(5)
total = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span")
total_text = total.text
assert total_text == "₹194.00"

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[5]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()

#Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
driver.execute_script("window.scrollBy(0, 300);")
book_1 = driver.find_element_by_css_selector("#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.outofstock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.ajax_add_to_cart")
book_1.click()
time.sleep(5)
book_2 = driver.find_element_by_css_selector("#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.outofstock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.ajax_add_to_cart")
book_2.click()

#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli")
basket.click()

#Удалите первую книгу
time.sleep(5)
delete = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a")
delete.click()

#Нажмите на Undo (отмена удаления)
undo = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div.woocommerce-message > a")
undo.click()

#В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
quantity_check = quantity.get_attribute("3")

#Нажмите на кнопку "UPDATE BASKET"
update_basket = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button")
update_basket.click()

#тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
value = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
value_text = value.text
assert value_text == "3"

#Нажмите на кнопку "APPLY COUPON"
time.sleep(5)
apply_coupon = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button")
apply_coupon.click()

#тест, что возникло сообщение: "Please enter a coupon code."
message = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
message_text = message.text
assert message_text == "Please enter a coupon code."

#Переход на новую вкладку
driver.execute_script("window.open();")
window_after = driver.window_handles[6]
driver.switch_to.window(window_after)
driver.get("http://practice.automationtesting.in/")

#Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

#Добавьте в корзину книгу
book = driver.find_element_by_css_selector("#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.outofstock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.ajax_add_to_cart")
book.click()

#Перейдите в корзину
basket = driver.find_element_by_css_selector("#wpmenucartli")
basket.click()

#Нажмите "PROCEED TO CHECKOUT"
time.sleep(5)
proceed_to_checkout = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > div > a")
proceed_to_checkout.click()

#Заполните все обязательные поля
time.sleep(5)
first_name = driver.find_element_by_css_selector("#billing_first_name")
first_name.send_keys("Anastasia")
last_name = driver.find_element_by_css_selector("#billing_last_name")
last_name.send_keys("K")
email_adresses = driver.find_element_by_css_selector("#billing_email")
email_adresses.send_keys("mail@mail.ru")
phone = driver.find_element_by_css_selector("#billing_phone")
phone.send_keys("89120258651")
country = driver.find_element_by_css_selector("#s2id_billing_country")
country.click()
country_enter = driver.find_element_by_css_selector("#s2id_autogen1_search")
country_enter.send_keys("Russia")
country_check = driver.find_element_by_class_name("select2-input")
country_check.click()
address_street = driver.find_element_by_css_selector("#billing_address_1")
address_street.send_keys("Sadovaya")
address_apartament = driver.find_element_by_css_selector("#billing_address_2")
address_apartament.send_keys("12")
city = driver.find_element_by_css_selector("#billing_city")
city.send_keys("Saint Petersburg")
county = driver.find_element_by_css_selector("#billing_state")
county.send_keys("Saint Petersburg")
postcode = driver.find_element_by_css_selector("#billing_postcode")
postcode.send_keys("123456")

#Выберите способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_payments = driver.find_element_by_css_selector("#payment_method_cheque")
check_payments.click()

#Нажмите PLACE ORDER
place_order = driver.find_element_by_css_selector("#place_order")
place_order.click()

#Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
time.sleep(10)
message = driver.find_element_by_css_selector("#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received")
message_text = message.text
assert message_text == "Thank you. Your order has been received."

#Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
time.sleep(5)
payment_method = driver.find_element_by_css_selector("#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td")
payment_method_text = payment_method.text
assert payment_method_text == "Check Payments"