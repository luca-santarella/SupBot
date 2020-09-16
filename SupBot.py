#Made by Luca Santarella

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# add a delay so that all elements of 
# the webpage are loaded before proceeding 
import time  

#keyword and color to find desired aticle
keyword = "Camo Mesh"
color = "Black"

#section selected
section = "shirts"

#personal info
billing_name = "John Smith"
email = "johnsmith@gmail.com"
tel = "1234567891"
address = "Via dei Mille"
number = "1000"
city = "Pisa"
postcode = "56121"
country = "IT"
card_type = "visa" #must be lowercase
card_number = "1234 5678 9012 3456"
card_month = "01"
card_year = "2030"
cvv = "123"

# ChromeOptions allows us use the userdata of chrome 
# so that you don't have to sign in manually everytime. 
chropt = Options() 
	  
# adding userdata argument to ChromeOptions object 
chropt.add_argument("--user-data-dir=[insert-your-path-here]") 
	  
# Creating a Chrome webdriver object 
driver = webdriver.Chrome(executable_path ="/bin/chromedriver",options = chropt) 

#jump start to selected section
driver.get("https://www.superiornewyork.com/shop/all/"+section) 
		
#find the articles
elem_articles = []
elem_container = driver.find_element_by_id("container")
#elem_articles is a list containing every item listed on the website
elem_articles = elem_container.find_elements_by_class_name("inner-article")

#find article desired in the articles list using keyword and color provided
for elem in elem_articles:
	if (keyword in elem.text) and (color in elem.text):
		elem_desired_article = elem

#click on the article
elem_desired_article.click()

#give time to load (could be decreased)
time.sleep(1)

#find button to add to cart
elem_buttons = []
elem_buttons = driver.find_elements_by_css_selector(".button")

elem_button = elem_buttons[3]

elem_button.click()

time.sleep(1)

elem_checkout = driver.find_element_by_css_selector(".button.checkout")
#click on checkout
elem_checkout.click()

#send_keys() types directly into the input form
#elem_billing_name = driver.find_element_by_id("order_billing_name")
#elem_billing_name.send_keys(billing_name)

#driver executes a JS script that changes the value of the input form
driver.execute_script('document.getElementById("order_billing_name").value="'+billing_name+'";')

#elem_email = driver.find_element_by_id("order_email")
#elem_email.send_keys(email)

driver.execute_script('document.getElementById("order_email").value="'+email+'";')

#elem_tel = driver.find_element_by_id("order_tel")
#elem_tel.send_keys(tel)
driver.execute_script('document.getElementById("order_tel").value="'+tel+'";')

#elem_address = driver.find_element_by_id("bo")
#elem_address.send_keys(address)

driver.execute_script('document.getElementById("bo").value="'+address+'";')

#elem_number = driver.find_element_by_id("oba3")
#elem_number.send_keys(number)

driver.execute_script('document.getElementById("oba3").value="'+number+'";')

#elem_city = driver.find_element_by_id("order_billing_city")
#elem_city.send_keys(city)

driver.execute_script('document.getElementById("order_billing_city").value="'+city+'";')

#elem_postcode = driver.find_element_by_id("order_billing_zip")
#elem_postcode.send_keys(postcode)

driver.execute_script('document.getElementById("order_billing_zip").value="'+postcode+'";')

driver.execute_script('document.getElementById("order_billing_country").value="'+country+'";')

driver.execute_script('document.getElementById("credit_card_type").value="'+card_type+'";')

#elem_card_number = driver.find_element_by_id("cnb")
#elem_card_number.send_keys(card_number)
driver.execute_script('document.getElementById("cnb").value="'+card_number+'";')

driver.execute_script('document.getElementById("credit_card_month").value="'+card_month+'";')

driver.execute_script('document.getElementById("credit_card_year").value="'+card_year+'";')

driver.execute_script('document.getElementById("vval").value="'+cvv+'";')

time.sleep(15)
driver.close()



