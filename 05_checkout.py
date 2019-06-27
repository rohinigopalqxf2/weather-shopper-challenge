"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to moisturizer  page
3) Select all items into cart
5) Verify the amount and numbers in cart page
6) checkout using test credit card
7) Close the browser
"""
import random
import time
import string
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

#function to create random string values which will be appended to email id to make it unique everytime
def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

#Function to add items to cart and do checkout action
def addingToCart_checkout():

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

    #click on pay with card button
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    
    #Switch to the iframe
    driver.switch_to.frame("stripe_checkout_app")

    #adding random values in the email id so that its unique everytime
    driver.find_element_by_xpath("//input[@type='email']").send_keys("tq"+randomStringwithDigitsAndSymbols()+ "@a.com")
    driver.find_element_by_xpath("//input[@type='tel']").send_keys("4242 4242 4242 4242")
    driver.find_element_by_xpath("//*[contains(@class,'Fieldset-input Textbox-control')][1]/following::*[contains(@placeholder,'MM / YY')]").send_keys("10/30")
    driver.find_element_by_xpath("//*[contains(@class,'Fieldset-input Textbox-control')][1]/following::*[contains(@placeholder,'CVC')]").send_keys("123")
    driver.find_element_by_xpath("//*[contains(@class,'Fieldset-input Textbox-control')][1]/following::*[contains(@placeholder,'ZIP Code')]").send_keys("123456")
    driver.find_element_by_xpath("//div[@class='Checkbox-tick']").click()
    driver.find_element_by_xpath("//*[contains(@class,'Fieldset-input Textbox-control')][1]/following::*[contains(@value,'+91')]").send_keys("9900378310")
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(@type,'submit')]").click()
    
    #switch back to the main window
    driver.switch_to.default_content()
    time.sleep(2)


#----START OF SCRIPT
if __name__=='__main__':
    addingToCart_checkout()

    #Adding wait for page to load completely
    time.sleep(5)
    #To check if payment was successfully done
    text = driver.current_url
    if(text =="https://weathershopper.pythonanywhere.com/confirmation"):
        print("Success : " + text)
    else:
        print("There is some problem : " + text)

# Quit the browser window
driver.quit() 