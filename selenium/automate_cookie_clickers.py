from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# =========================================
cookie_id = "bigCookie"
language = "//div[@class='langSelectButton title' and @id='langSelect-EN']"
num_cookies = "//div[@id='cookies' and @class='title']"
product_price_prefix = "productPrice"
product_prefix = "product"
# =========================================


# --------------- Set the Chrome Driver path ---------------
PATH = "D:\\2024\\newGithub\\automateThings\\tools\\chromedriver.exe"


# --------------- Set the connection and go to the URL ---------------
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


# --------------- Wait for the website to load ---------------
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, language)))


# --------------- Find the element ---------------
lang = driver.find_element(By.XPATH, language)
lang.click()


# --------------- Wait for the website to load ---------------
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))

# --------------- Find the element ---------------
cookie = driver.find_element(By.ID, cookie_id)

while True: 
    cookie.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))
    # --------------- Take the cookies count ---------------
    cookies_count = driver.find_element(By.XPATH, num_cookies).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

    # --------------- Check four upgrades ---------------
    for i in range(4): 
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        # --------------- Check if product price is an integer or not ---------------
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        # --------------- Check if the cookies count is greater than the price or not ---------------
        if cookies_count >= product_price: 
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
