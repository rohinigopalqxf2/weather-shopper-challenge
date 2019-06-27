"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to moisturizer  page
3) Select all items into cart
5) Verify the amount and numbers in cart page
6) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

#KEY POINT Select all items into cart
add_button_elements = driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
length = len(add_button_elements)
#print(length)

#Click on every Add button in the list
for x in range(len(add_button_elements)):
   # print(add_button_elements[x])
    add_button_elements[x].click()
    #time.sleep(2)

#check the text of the cart displayed on top right
cart_count = driver.find_element_by_xpath("//span[contains(text(),'item(s)')]").text
print(cart_count)

#get the count part by splitting the text
countpart =cart_count.split(None,1)
#print(countpart)
time.sleep(2)
#navigate to cart page
driver.find_element_by_xpath("//button[@class='thin-text nav-link']").click()
time.sleep(2)
#print(driver.current_url)

#finding row length of the table for checkout
table = driver.find_element_by_xpath("//table[@class='table table-striped']")
rows = table.find_elements_by_xpath("//tbody/descendant::tr")

#print(len(rows))
#Total amount for checkout
total_rupees = driver.find_element_by_id("total").text
#print(total_rupees)

#if rows in table is equal to number of items added to cart as per previous page then test is pass else failed
if(len(rows) ==int(countpart[0])):
    print("Successfully add all items to cart and ready for checkout")
else:
   print("Failed  to add all items to cart for checkout")

# Quit the browser window
driver.quit() 