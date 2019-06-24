"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to sunscreen  page
3) Select all items into cart
5) Verify the cart, if all are selected or not (by verifying the count)
6) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

#KEY POINT Select all items into cart
add_button_elements = driver.find_elements_by_xpath("//button[@class='btn btn-primary']")
length = len(add_button_elements)
#print(length)

#Click on every Add button in the list
for x in range(len(add_button_elements)):
   # print(add_button_elements[x])
    add_button_elements[x].click()
    time.sleep(2)

#check the text of the cart displayed on top right
cart_count = driver.find_element_by_xpath("//span[contains(text(),'item(s)')]").text
print(cart_count)

#get the count part by splitting the text
countpart =cart_count.split(None,1)
#print(countpart)

#if length of cart items match with the number of items added to cart text then all items are added to cart
if(length == int(countpart[0])):
    print("All items selected into cart")
else:
    print("Something is wrong")

time.sleep(2)

# Quit the browser window
driver.quit() 