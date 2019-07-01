"""
AUTHOR: Rohini Gopal
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to sunscreen  page
3) Select  the most expensive product i.e sunscreen from the screen 
5) navigate to the cart page
6) Close the browser

"""
import time
from selenium import webdriver

#variables
list_price_most_expensive =[]
min_list =[]

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

#select product which is most expensive
def get_most_expensive_sunscreen():
        # # find the items which have aloe in the text
        price =0
        min_price =10000000

        #get all products from the page
        select_all = driver.find_elements_by_xpath("//div[contains(@class,'col-4')]")

        for i in range(0,len(select_all)):
                print(select_all[i].text)
                price = driver.find_elements_by_xpath("//*[contains(text(),'Price')]")
                split_price = price[i].text
                new_price = split_price.split('Price:',1)

                #Some price have Rs appended to it.So verifying and accordingly selecting the index
                if (new_price[1].find('Rs. ')!=-1):
                        new_price = new_price[1].split('Rs. ')
                else:
                        print(new_price[0])
                new_price = int(new_price[1])
                if(new_price >= min_price):
                        min_price = new_price
                list_price_most_expensive.append(new_price)
        return list_price_most_expensive


#click add for most expensive sunscreen           
def clickAdd_maxPrice_sunscreen(list_price_most_expensive):
        max_value = max(list_price_most_expensive)
        print(max_value)
        max_value_str = str(max_value)
        click_add = driver.find_element_by_xpath("//p[contains(text(),'"+max_value_str+"')]/following-sibling::button[@class='btn btn-primary']")
        click_add.click()    

#check if cart page is loaded     
def verify():
        if(driver.current_url =="https://weathershopper.pythonanywhere.com/cart"):
                print("Successfully add the item to cart")
        else:
                print("Test Failed Still on :" + driver.current_url)

#----START OF SCRIPT
if __name__=='__main__':
    get_most_expensive_sunscreen()
    
    print(list_price_most_expensive)

    clickAdd_maxPrice_sunscreen(list_price_most_expensive)

    
    #click on the cart
    cart_button = driver.find_element_by_xpath("//button[@onclick='goToCart()']").click()
    verify()


#Quit the driver
driver.quit()