from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --------------- Set the Chrome Driver path ---------------
PATH = "D:\\2024\\newGithub\\automateThings\\tools\\chromedriver.exe"

# --------------- Set the connection and go to the URL ---------------
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")

# --------------- Wait for the website to load ---------------
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# --------------- Find the element ---------------
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.clear()

# --------------- Enter the key ---------------
input_element.send_keys("tech with tim" + Keys.ENTER)


# --------------- Wait for the website to load ---------------
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

# --------------- Find the text with link and click ---------------
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()


time.sleep(10)

driver.quit()
