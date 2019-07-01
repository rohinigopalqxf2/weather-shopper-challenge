"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to sunscreen  page
3) Select 2 items into cart .  First, select the least expensive sunscreen that is SPF-50
4) For your second sunscreen, select the least expensive sunscreen that is SPF-30. 
5) verify the cart count
6) Close the browser
"""
import time
from selenium import webdriver

#variables
list_price_spf_50 =[]
list_price_spf_30=[]
min_list =[]

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

#select product with SPF-50
def get_least_sunscreen_spf_50():
        price =0
        min_price =10000000
        #for items in aloe:
        spf_50 = driver.find_elements_by_xpath("//*[contains(text(),'SPF-50') or contains(text(),'spf-50')]")

        for i in range(0,len(spf_50)):
                print(spf_50[i].text)
                price = driver.find_elements_by_xpath("//*[contains(text(),'spf-50') or contains(text(),'SPF-50')]/following-sibling::p")
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
                list_price_spf_50.append(new_price)
        return list_price_spf_50

#select product with spf-30
def get_least_spf_30():
        price =0
        min_price = 100000

        #select items with SPF-30:
        spf_30 = driver.find_elements_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]")

        for i in range(0,len(spf_30)):
                print(spf_30[i].text)
                price = driver.find_elements_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p")
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
                list_price_spf_30.append(new_price)
        return list_price_spf_30

#click add for least expensive spf-50            
def clickAdd_minPrice_spf_50(list_price_spf_50):
        min_value = min(list_price_spf_50)
        min_value_str = str(min_value)
        click_add = driver.find_element_by_xpath("//p[contains(text(),'"+min_value_str+"')]/following-sibling::button[@class='btn btn-primary']")
        click_add.click()    

#click add for least expensive spf-30
def clickAdd_minPrice_spf_30(list_price_spf_30):
        min_value = min(list_price_spf_30)
        min_value_str = str(min_value)
        click_add = driver.find_element_by_xpath("//p[contains(text(),'"+min_value_str+"')]/following-sibling::button[@class='btn btn-primary']")
        click_add.click()                  

#check if cart page is loaded  
def verify():
        if(driver.current_url =="https://weathershopper.pythonanywhere.com/cart"):
                print("Successfully add the item to cart")
        else:
                print("Test Failed , still on page : "+ driver.current_url)

#----START OF SCRIPT
if __name__=='__main__':
    get_least_sunscreen_spf_50()
    get_least_spf_30()
    print(list_price_spf_30)
    print(list_price_spf_50)
    clickAdd_minPrice_spf_30(list_price_spf_30)
    clickAdd_minPrice_spf_50(list_price_spf_50)
    
    #click on the cart
    cart_button = driver.find_element_by_xpath("//button[@onclick='goToCart()']").click()
    verify()


#Quit the driver
driver.quit()