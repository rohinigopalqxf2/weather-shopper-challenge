"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to moisturizer  page
3) Select 2 items into cart . First, select the least expensive mositurizer that contains Aloe. 
4) For your second moisturizer, select the least expensive moisturizer that contains almond.
5) check the cart page is loaded
6) Close the browser
"""
import time
from selenium import webdriver

#variables
list_price_aloe =[]
list_price_almond=[]
min_list =[]

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

#select product with Aloe
def get_least_aloe():
        # # find the items which have aloe in the text
        price =0
        min_price =10000000
        #for items in aloe:
        aloe = driver.find_elements_by_xpath("//*[contains(text(),'aloe') or contains(text(),'Aloe')]")

        for i in range(0,len(aloe)):
                print(aloe[i].text)
                price = driver.find_elements_by_xpath("//*[contains(text(),'aloe') or contains(text(),'Aloe')]/following-sibling::p")
                split_price = price[i].text
                new_price = split_price.split('Price:',1)

                #Some price have Rs appended to it.So verifying and accordingly selecting the index
                if (new_price[1].find('Rs. ')!=-1):
                        new_price = new_price[1].split('Rs. ')
                else:
                        print(new_price[0])
                new_price = int(new_price[1])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_aloe.append(new_price)
        return list_price_aloe

#select product with almond
def get_least_almond():
        price =0
        min_price = 100000
        #for items in almond:

        almond = driver.find_elements_by_xpath("//*[contains(text(),'almond') or contains(text(),'Almond')]")

        for i in range(0,len(almond)):
                print(almond[i].text)
                price = driver.find_elements_by_xpath("//*[contains(text(),'almond') or contains(text(),'Almond')]/following-sibling::p")
                split_price = price[i].text
                new_price = split_price.split('Price:',1)

                #Some price have Rs appended to it.So verifying and accordingly selecting the index
                if (new_price[1].find('Rs. ')!=-1):
                        new_price = new_price[1].split('Rs. ')
                else:
                        print(new_price[0])
                new_price = int(new_price[1])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_almond.append(new_price)
        return list_price_almond

#click add for least expensive aloe            
def clickAdd_minPrice_aloe(list_price_aloe):
        min_value = min(list_price_aloe)
        min_value_str = str(min_value)
        click_add = driver.find_element_by_xpath("//p[contains(text(),'"+min_value_str+"')]/following-sibling::button[@class='btn btn-primary']")
        click_add.click()    

#click add for least expensive almond
def clickAdd_minPrice_almond(list_price_almond):
        min_value = min(list_price_almond)
        min_value_str = str(min_value)
        click_add = driver.find_element_by_xpath("//p[contains(text(),'"+min_value_str+"')]/following-sibling::button[@class='btn btn-primary']")
        click_add.click()                  

#check if cart has 2 items in it.             
def verify():
        if(driver.current_url =="https://weathershopper.pythonanywhere.com/cart"):
                print("Successfully add the item to cart")
        else:
                print("Test Failed still on page : " +driver.current_url)
#----START OF SCRIPT
if __name__=='__main__':
    get_least_aloe()
    get_least_almond()
    
    clickAdd_minPrice_aloe(list_price_aloe)
    clickAdd_minPrice_almond(list_price_almond)

    #click on the cart
    cart_button = driver.find_element_by_xpath("//button[@onclick='goToCart()']").click()
    verify()


#Quit the driver
driver.quit()