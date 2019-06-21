"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to weather shopper page
3) Read the temperature listed on the page
4)Depending on the temperature, choose to buy either moisturizers or sunscreens
5) Check the page title
6) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com ')


# Check if the title of the page is proper - navigate to page
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: Weather shopper page launched successfully")
else:
    print ("Failed: weather shopper page Title is incorrect") 

# List the temprature listed in the page
temp =driver.find_element_by_xpath("//span[@id='temperature']").text

time.sleep(2)
print("Temperature listed now is :" + temp)

#Split temp value from text
temp_value = temp.split(None , 1)
temp_number= int(temp_value[0])

#check if the temp is lower than 19 then buy moisturiser 
# if temp greater than 34 then buy sunscreens
# other do nothing

if(temp_number < 19):
    print("Selecting moisturiser")
    time.sleep(2)
    driver.find_element_by_link_text("Buy moisturizers").click()
    print("Selected Moisturiser.Page title is : "+ driver.title)
elif (temp_number > 34):
    print("selecting sunscreen")
    time.sleep(2)
    driver.find_element_by_link_text("Buy sunscreens").click()
    print("Selected Sunscreens.Page title is : "  + driver.title)
else:
    print("temperature is between 20 and 33 degree C")
    print("Still on Homepage :" + driver.title)


# Quit the browser window
driver.quit() 